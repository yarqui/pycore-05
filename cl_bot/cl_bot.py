from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return "Error: Incorrect number of arguments."

    return inner


def parse_input(user_input: str):
    cmd, *args = user_input.strip().casefold().split()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict):
    if len(args) < 2:
        raise IndexError

    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args: list, contacts: dict):
    if len(args) < 2:
        raise IndexError

    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return f"Contact {name} updated"


@input_error
def show_phone(args: list, contacts: dict):
    if not len(args) == 1:
        raise IndexError

    name = args[0]

    if name not in contacts:
        raise KeyError

    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts: dict):
    if not contacts:
        return "No contacts found."

    return "".join(f"\n{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match (command):
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
