# ============================================================
# ACRONYM GENERATOR
# ============================================================
import re

class AcronymGenerator:
    """
    A class that generates acronyms from user-input phrases.
    It handles validation, formatting, and advanced string processing.
    """

    def __init__(self, phrase):
        self.phrase = phrase

    def validate_input(self):
        """
        Validates that the input is not empty and contains alphabetic characters.
        """
        if not self.phrase or not re.search(r"[A-Za-z]", self.phrase):
            raise ValueError("Invalid input: Please enter a valid phrase.")

    def generate(self):
        """
        Generates an acronym by extracting the first letter of each word.
        """
        words = re.findall(r"[A-Za-z]+", self.phrase)
        acronym = ''.join(word[0] for word in words)
        return acronym.upper()


def main():
    print("=" * 50)
    print("           ACRONYM GENERATOR")
    print("=" * 50)

    while True:
        try:
            user_input = input("Enter a word or phrase: ").strip()

            generator = AcronymGenerator(user_input)
            generator.validate_input()

            result = generator.generate()
            print("\nGenerated Acronym:", result)
            break

        except ValueError as error:
            print("Error:", error)
            print("Please try again.\n")


# Program entry point
if __name__ == "__main__":
    main()


