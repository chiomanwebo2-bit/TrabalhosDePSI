# Ask how many notes the user wants to enter
n = int(input("How many notes do you want to enter? "))

notes = []

# Read the notes
for i in range(n):
    note = float(input(f"Enter note {i + 1}: "))
    notes.append(note)

# Menu loop
while True:
    print("/n===== MENU =====")
    print("1. Show all notes")
    print("2. Show highest grade")
    print("3. Show lowest grade")
    print("4. Show average")
    print("5. Show number of notes")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        print("All notes:", notes)

    elif choice == "2":
        print("Highest grade:", max(notes))

    elif choice == "3":
        print("Lowest grade:", min(notes))

    elif choice == "4":
        average = sum(notes) / len(notes)
        print("Average:", average)

    elif choice == "5":
        print("show number of notes:", len(notes))
    else:
        print("Exit, program ended sucessfully")
        break


