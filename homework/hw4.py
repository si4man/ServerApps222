import json
from datetime import datetime

LOG_FILE = "log.json"
PROGRAM_NAME = "exec logger"

def times_word(n: int) -> str:
    return "time" if n == 1 else "times"

def load_log() -> dict:
    try:
        with open(LOG_FILE, encoding="utf-8") as fp:
            data = json.load(fp)
        if not isinstance(data, dict):
            raise json.JSONDecodeError("[Error] Root is not object", "", 0)
        if "program" not in data or "execMoments" not in data or not isinstance(data["execMoments"], list):
            raise json.JSONDecodeError("[Error] Invalid structure", "", 0)
        return data
    except OSError:
        return {"program": PROGRAM_NAME, "execMoments": []}
    except json.JSONDecodeError:
        return {"program": PROGRAM_NAME, "execMoments": []}

def save_log(data: dict) -> None:
    try:
        with open(LOG_FILE, mode="w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
    except OSError as err:
        print("[Error] File write error:", err)

def current_time_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    data = load_log()
    moments = data.get("execMoments", [])
    count = len(moments)
    if count > 0:
        joined = '", "'.join(moments)
        print(f'[Log] The program was previously run {count} {times_word(count)} at "{joined}"')
    else:
        print("[Log] The program was not run before")
    now = current_time_str()
    moments.append(now)
    data["program"] = PROGRAM_NAME
    data["execMoments"] = moments
    save_log(data)

if __name__ == "__main__":
    main()
