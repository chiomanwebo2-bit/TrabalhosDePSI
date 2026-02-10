# 🌟 Mini Projeto 3 - Gestor de uma Turma (Python)

students = []

# 🔤 Function to read a valid name
def read_name():
    while True:
        name = input("🧑 Enter student name: ")
        if name.isalpha():
            return name
        else:
            print("❌ Invalid name! Use letters only.")

# 🔢 Function to read a valid number
def read_number(message):
    while True:
        value = input(message)
        if value.isdigit():
            return value
        else:
            print("❌ Invalid input! Use numbers only.")

# ➕ Add student
def add_student():
    name = read_name()
    number = read_number("🆔 Enter student number: ")
    age = read_number("🎂 Enter student age: ")
    students.append({"name": name, "number": number, "age": age})
    print("✅ Student added successfully!")

# 📄 Show all students
def show_students():
    if not students:
        print("⚠️ No students registered!")
    else:
        for s in students:
            print(f"Name: {s['name']}, Number: {s['number']}, Age: {s['age']}")

# 🔍 Search student
def search_student():
    number = read_number("🔍 Enter student number: ")
    for s in students:
        if s["number"] == number:
            print(f"📄 Found: {s['name']} - Age {s['age']}")
            return
    print("❌ Student not found!")

# ✏️ Edit student
def edit_student():
    number = read_number("✏️ Enter student number: ")
    for s in students:
        if s["number"] == number:
            s["name"] = read_name()
            s["age"] = read_number("🎂 Enter new age: ")
            print("✅ Student updated!")
            return
    print("❌ Student not found!")

# 🗑️ Remove student
def remove_student():
    number = read_number("🗑️ Enter student number: ")
    for s in students:
        if s["number"] == number:
            students.remove(s)
            print("✅ Student removed!")
            return
    print("❌ Student not found!")

# 🔤 Sort students alphabetically
def sort_students():
    students.sort(key=lambda s: s["name"])
    print("🔠 Students sorted alphabetically!")

# 🔁 Main menu loop
while True:
    print("\n📋 Menu:")
    print("1️⃣ Add student")
    print("2️⃣ Show all students")
    print("3️⃣ Search student")
    print("4️⃣ Edit student")
    print("5️⃣ Remove student")
    print("6️⃣ Count students")
    print("7️⃣ Sort students A–Z")
    print("0️⃣ Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_student()
    elif option == "2":
        show_students()
    elif option == "3":
        search_student()
    elif option == "4":
        edit_student()
    elif option == "5":
        remove_student()
    elif option == "6":
        print(f"🔢 Total students: {len(students)}")
    elif option == "7":
        sort_students()
    elif option == "0":
        print("🏁 Program ended. Goodbye!")
        break
    else:
        print("⚠️ Invalid option!")

