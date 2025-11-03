import json

data1 = """{
    "x": 10,
    "y": 0.123,
    "w": 1.2e-2,
    "t": true,
    "f": false,
    "n": null,
    "arr": [1, 2, "3"],
    "o": {
        "s": "hello",
        "u": "Привет",
        "date": "2025-10-29"
    },
    "b": 12345678901234567890123456789012345678901234567890,
    "c": "аббабабаб",
    "p": 0.12345678901234567890123456789012345678901234567890
}"""

data2 = """[
    10, 1.23, "String", {"x": 10}
]"""


def main():
    j = json.loads(data1)
    print(type(j), j)
    print("-------------------------------------")
    j2 = json.loads(data2)
    print(type(j2), j2)
    print("-------------------------------------")
    try:
        with open("07_json.json", mode="w", encoding="utf-8") as fp:
            j_str = json.dump(j, fp, ensure_ascii=False, indent=4)
        print(type(j_str), j_str)
    except OSError as err:
        print("File write error:", err)
    print("-------------------------------------")
    try:
        with open("07_json.json", encoding="utf-8") as fp:
            j3 = json.load(fp)
        print(type(j3), j3)
    except OSError as err:
        print("File read error:", err)
    except json.JSONDecodeError as err:
        print("JSON Decode Error:", err)
    print("-------------------------------------")
    try:
        with open("07_json_err.json", encoding="utf-8") as fp:
            j4 = json.load(fp)
        print(type(j4), j4)
    except OSError as err:
        print("File error:", err)
    except json.JSONDecodeError as err:
        print("JSON Decode Error:", err)


if __name__ == "__main__":
    main()
