# ascii_art.py
<h1>Why this project?</h1>
<p>Sometimes you just need some nostalgia, so you need some kickass ascii_art!</p>

    # imports
    import pyfiglet

    # The brains, it thinks up the art
    def generate_ascii_art(phrase, filename):
        ascii_art = pyfiglet.figlet_format(phrase)
        print(ascii_art)
        with open(filename, 'w') as file:
            file.write(ascii_art)

    # The mouth, it asks and speaks(provides the art)
    if __name__ == "__main__":
        phrase = input("Enter a phrase: ")
        filename = input("Enter the output filename: ")
        generate_ascii_art(phrase, filename)
        print(f"ASCII art saved to {filename}")

<h1>How does it look like?</h1>

    _    ____   ____ ___ ___      _    ____ _____ _ 
   / \  / ___| / ___|_ _|_ _|    / \  |  _ \_   _| |
  / _ \ \___ \| |    | | | |    / _ \ | |_) || | | |
 / ___ \ ___) | |___ | | | |   / ___ \|  _ < | | |_|
/_/   \_\____/ \____|___|___| /_/   \_\_| \_\|_| (_)

<p>So you can use this to make some cool old school art.</p>

<h3>ToDo-List</h3>
<li>Color</li>
<li>Better save support</li>
<li>Background Color support</li>
 

