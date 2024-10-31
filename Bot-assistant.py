def input_error(func):
    # Декоратор для обробки помилок введення користувача
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
    return inner

@input_error
def add_contact(args, contacts):
    # Додає контакт у словник
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Змінює існуючий контакт
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    # Показує номер телефону за ім'ям контакту
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    # Показує всі контакти
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input):
    # Розбиває введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    # Основна функція програми
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        # Основний цикл програми
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "welcome":
            print("Welcome to the assistant bot!")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
