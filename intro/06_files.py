def write_file(filename: str = "file.txt") -> None:
    file = None
    try:
        file = open(filename, mode="w", encoding="utf-8")
        file.write("Hello, World!\n")
        file.write("Привет, мир!\n")
        file.flush()
    except OSError as err:
        print("File write error:", err)
    else:
        print("File written successfully")
    finally:
        if file != None:
            file.close()


def write_file2(filename: str = "file2.txt") -> None:
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("Hello, World!\n")
            file.write("Привет, мир!\n")
            file.flush()
    except OSError as err:
        print("File write error:", err)
    else:
        print("File written successfully")


def read_file(filename: str = "file.txt") -> None:
    try:
        with open(filename, encoding="utf-8") as file:
            # print(file.read())
            for line in file:
                # print(line.strip())
                print(line)
                print("---")
    except OSError as err:
        print("File write error:", err)
    else:
        print("File read successfully")


def read_ini(filename: str = "db.ini") -> dict:
    res = {}
    with open(filename, encoding="utf-8") as file:
        for line in file:
            if line.startswith("#"):
                continue
            line = line.split("#")[0]
            if not ":" in line:
                continue
            pair = line.split(":", 1)
            # res[pair[0]] = pair[1][:-1]
            res[pair[0].strip()] = pair[1].strip()
    return res


def read_ini2(filename: str = "db.ini") -> dict:
    with open(filename, encoding="utf-8") as file:
        return {
            # k: v[:-1]
            k: v
            for k, v in (
                map(str.strip, line.split("#")[0].split(":", 1))
                for line in file
                if ":" in line
            )
        }


def main():
    try:
        print(read_ini())
        print(read_ini2())
    except OSError as err:
        print(err)


if __name__ == "__main__":
    main()
