import pyfiglet

def generate_ascii_art(phrase, filename):
    ascii_art = pyfiglet.figlet_format(phrase)
    print(ascii_art)
    with open(filename, 'w') as file:
        file.write(ascii_art)

if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    filename = input("Enter the output filename: ")
    generate_ascii_art(phrase, filename)
    print(f"ASCII art saved to {filename}")

