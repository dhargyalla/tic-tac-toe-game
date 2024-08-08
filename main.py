# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return 'this is a good day'
#
# if __name__ == '__main__':
#     app.run()


# main.py

from morse_code import text_to_morse

def main():
    # Example: Getting user input and converting it to Morse code
    user_input = input("Enter text to convert to Morse code: ")
    morse_output = text_to_morse(user_input)
    print(f"Morse Code: {morse_output}")

if __name__ == "__main__":
    main()
