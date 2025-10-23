# Винятки
def throw():        # Створення винятку - raise
    raise ValueError    # Частіше вживається термін Error

def main():
    try:
        throw()
    except ValueError:
        print("ValueError detected")
        return
    except TypeError as err:
        print(err)
    except:
        print("Unknown Error detected")
    else:
        print("Else block")
    finally:
        print("Finally block")

if __name__ == '__main__':
    main()
