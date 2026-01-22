# ==========================================
# PSI Mini Project 1
# Acronym Generator
# ==========================================

from datetime import datetime


def generate_acronym(phrase):
    """
    Generates an acronym from a given phrase.
    """
    words = phrase.split()
    acronym = ""

    for word in words:
        if word.isalpha():
            acronym += word[0]

    return acronym.upper()


def show_menu():
    print("\n====== ACRONYM GENERATOR ======")
    print("1. Generate Acronym")
    print("2. View History")
    print("3. Exit")
    print("===============================")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            phrase = input("Enter a phrase: ").strip()

            if not phrase:
                print("Input cannot be empty.")
                continue

            acronym = generate_acronym(phrase)
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            history.append((phrase, acronym, time))
            print("Generated Acronym:", acronym)

        elif choice == "2":
            if not history:
                print("No history available.")
            else:
                print("\n--- HISTORY ---")
                for i, item in enumerate(history, start=1):
                    print(f"{i}. {item[0]} → {item[1]} ({item[2]})")


        elif choice == "3":
            print("Program ended.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
