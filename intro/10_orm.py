import requests
from datetime import datetime, date

BASE_URL = (
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={yyyymmdd}&json"
)

class NbuRate:
    def __init__(self, j: dict | None = None):
        self.r030 = j["r030"] if j else None
        self.txt = j["txt"] if j else None
        self.rate = j["rate"] if j else None
        self.cc = j["cc"] if j else None
        self.exchangedate = j["exchangedate"] if j else None

    def __str__(self):
        return "%s (%s): %s ₴ on %s" % (self.txt, self.cc, self.rate, self.exchangedate)


class NbuData:
    def __init__(self, url: str):
        self.url = url
        request = requests.get(url, timeout=15)
        request.raise_for_status()
        response = request.json()
        self.rates = [NbuRate(j) for j in response]

    def size(self):
        return len(self.rates)

    def get_by_cc(self, fragment: str) -> NbuRate | None:
        return next((r for r in self.rates if r.cc == fragment.upper()), None)

    def filter(self, fragment: str):
        f = fragment.upper()
        return (r for r in self.rates if f in r.cc or f in r.txt.upper())


def _parse_user_date(s: str) -> date | None:
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%Y%m%d"):
        try:
            return datetime.strptime(s.strip(), fmt).date()
        except ValueError:
            pass
    return None


def _ensure_past(d: date) -> bool:
    return d < date.today()


def _to_api_format(d: date) -> str:
    return d.strftime("%Y%m%d")


def get_valid_date_url() -> str:
    while True:
        s = input("Enter the date [DD.MM.YYYY or YYYY-MM-DD or YYYYMMDD]: ")
        d = _parse_user_date(s)
        if not d:
            print("Invalid date format. Please try again.")
            continue
        if not _ensure_past(d):
            print("The date must be from the past. Please try again.")
            continue
        yyyymmdd = _to_api_format(d)
        url = BASE_URL.format(yyyymmdd=yyyymmdd)
        try:
            nbu = NbuData(url)
        except Exception as e:
            print("Failed to load rates. Please try again. Error:", e)
            continue
        if nbu.size() == 0:
            print("No rates found for this date. Please enter another date.")
            continue
        return url


def main():
    url = get_valid_date_url()
    nbu = NbuData(url)
    print("Successful loaded rates:", nbu.size())
    fragment = input("Enter currency code or part of name to search: ")
    results = list(nbu.filter(fragment))
    if results:
        print(*results, sep="\n")
    else:
        print("Not found :(")


if __name__ == "__main__":
    main()
