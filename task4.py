def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Please enter your username"
        
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone

    return "Contact updated"

@input_error
def display_info(contacts):
    if not contacts:
        return "Contacts list is empty"
    
    return [f"{name}: {phone}" for name,phone in contacts.items()]

@input_error
def show_phone(args,contacts):
   name = args[0]

   return contacts[name]
    
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def main():

    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(display_info(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()