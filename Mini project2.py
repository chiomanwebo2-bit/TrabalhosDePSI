# Mini Projeto 2 – Gestor de Nomes

names = []

def show_title():
    print("\n==============================")
    print("   👤 NAME MANAGER SYSTEM 👤")
    print("==============================")

def show_menu():
    print("\nChoose an option:")
    print("1. Add a name")
    print("2. Remove a name")
    print("3. List all names")
    print("4. Search for a name")
    print("5. Exit")
    print("6. Count names 🔢")
    print("7. Show first and last name 🧠")
    print("8. Check if list is empty 📭")
    print("9. Sort names alphabetically 🔠")

def add_name():
    name = input("Enter a name to add: ").strip()

    if name.isalpha():
        names.append(name)
        print(f"✅ '{name}' added successfully!")
    else:
        print("❌ Invalid name. Use letters only.")

def remove_name():
    name = input("Enter a name to remove: ").strip()

    if name in names:
        names.remove(name)
        print(f"🗑️ '{name}' removed successfully.")
    else:
        print("❌ Name not found.")

def list_names():
    if not names:
        print("📭 No names stored yet.")
    else:
        print("\n📋 List of names:")
        for i, name in enumerate(names, start=1):
            print(f"{i}. {name}")

def search_name():
    name = input("Enter a name to search: ").strip()

    if name in names:
        print(f"🔍 Yes! '{name}' is in the list.")
    else:
        print(f"❌ '{name}' is not in the list.")

# 🔢 Option B
def count_names():
    print(f"🔢 Total number of names: {len(names)}")

# 🧠 Option C
def first_last_name():
    if not names:
        print("📭 The list is empty.")
    else:
        print(f"🧠 First name: {names[0]}")
        print(f"🧠 Last name: {names[-1]}")

# 📭 Option D
def check_empty():
    if not names:
        print("📭 The name list is empty.")
    else:
        print("✅ The name list is not empty.")

# 🔠 Option E
def sort_names():
    if not names:
        print("📭 No names to sort.")
    else:
        names.sort()
        print("🔠 Names sorted alphabetically!")

def main():
    show_title()

    while True:
        show_menu()
        choice = input("Option: ")

        if choice == "1":
            add_name()
        elif choice == "2":
            remove_name()
        elif choice == "3":
            list_names()
        elif choice == "4":
            search_name()
        elif choice == "5":
            print("\n👋 Goodbye! Program closed.")
            break
        elif choice == "6":
            count_names()
        elif choice == "7":
            first_last_name()
        elif choice == "8":
            check_empty()
        elif choice == "9":
            sort_names()
        else:
            print("❌ Invalid option. Try again.")


main()
