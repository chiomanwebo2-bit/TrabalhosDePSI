# 🌟 Mini Projeto 3 - Gestor de uma Turma

# Create empty list to store students
students = []

while True:
    # Show menu
    print("\n📋 Menu:")
    print("1️⃣ Add student")
    print("2️⃣ Show all students")
    print("3️⃣ Search student")
    print("4️⃣ Edit student")
    print("5️⃣ Remove student")
    print("6️⃣ Count students")
    print("0️⃣ Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("🧑 Enter student name: ")
        number = input("🆔 Enter student number: ")
        age = input("🎂 Enter student age: ")
        students.append({"name": name, "number": number, "age": age})
        print("✅ Student added successfully!")

    elif option == "2":
        if not students:
            print("⚠️ No students registered yet!")
        else:
            print("\n📄 List of Students:")
            for s in students:
                print(f"Name: {s['name']}, Number: {s['number']}, Age: {s['age']}")

    elif option == "3":
        search_number = input("🔍 Enter student number to search: ")
        found = False
        for s in students:
            if s["number"] == search_number:
                print(f"📄 Found student - Name: {s['name']}, Age: {s['age']}")
                found = True
                break
        if not found:
            print("❌ Student not found!")

    elif option == "4":
        edit_number = input("✏️ Enter student number to edit: ")
        found = False
        for s in students:
            if s["number"] == edit_number:
                s["name"] = input("🧑 Enter new name: ")
                s["age"] = input("🎂 Enter new age: ")
                print("✅ Student updated!")
                found = True
                break
        if not found:
            print("❌ Student not found!")

    elif option == "5":
        remove_number = input("🗑️ Enter student number to remove: ")
        found = False
        for s in students:
            if s["number"] == remove_number:
                students.remove(s)
                print("✅ Student removed!")
                found = True
                break
        if not found:
            print("❌ Student not found!")

    elif option == "6":
        print(f"🔢 Total students: {len(students)}")

    elif option == "0":
        print("🏁 Exiting program. Goodbye!")
        break

    else:
        print("⚠️ Invalid option! Try again.")
