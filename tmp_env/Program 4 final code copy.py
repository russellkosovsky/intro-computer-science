from graphics import *
import time

def caesar_cipher(text, key):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':  
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char  
    return result

def flashing_welcome(win):
    welcome_text = Text(Point(200, 50), "WELCOME!")
    welcome_text.setSize(24)
    colors = ["red", "blue", "green", "purple", "orange"]
    
    for _ in range(6):  
        welcome_text.setTextColor(colors[_ % len(colors)])
        welcome_text.draw(win)
        time.sleep(0.3)
        welcome_text.undraw()

    welcome_text.setTextColor("black")
    welcome_text.draw(win)

def choose_mode(win):
    file_button = Rectangle(Point(100, 150), Point(200, 180))
    file_button.setFill("lightgray")
    file_button.draw(win)
    Text(Point(150, 165), "File").draw(win)

    message_button = Rectangle(Point(220, 150), Point(320, 180))
    message_button.setFill("lightgray")
    message_button.draw(win)
    Text(Point(270, 165), "Message").draw(win)

    exit_button = Rectangle(Point(150, 200), Point(250, 230))
    exit_button.setFill("lightgray")
    exit_button.draw(win)
    Text(Point(200, 215), "Exit").draw(win)

    output_text = Text(Point(200, 220), "")
    output_text.draw(win)

    while True:
        click = win.getMouse()
        if 100 < click.getX() < 200 and 150 < click.getY() < 180:  # File button
            output_text.setText("Choose File: Dracula or Gatsby")
            return "file"
        elif 220 < click.getX() < 320 and 150 < click.getY() < 180:  # Message button
            output_text.setText("Enter Message Directly")
            return "message"
        elif 150 < click.getX() < 250 and 200 < click.getY() < 230:  # Exit button
            win.close()
            exit()

def load_file(filename):
    try:
        with open(filename + ".txt", "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    
###############################
def main():
    win = GraphWin("Caesar Cipher", 400, 300)
    
    flashing_welcome(win)

    Text(Point(100, 90), "Message:").draw(win)
    input_box = Entry(Point(250, 90), 30)
    input_box.draw(win)

    Text(Point(100, 130), "Key:").draw(win)
    key_box = Entry(Point(250, 130), 5)
    key_box.draw(win)

    encode_button = Rectangle(Point(100, 170), Point(200, 200))
    encode_button.setFill("lightgray")
    encode_button.draw(win)
    Text(Point(150, 185), "Encode").draw(win)

    decode_button = Rectangle(Point(220, 170), Point(320, 200))
    decode_button.setFill("lightgray")
    decode_button.draw(win)
    Text(Point(270, 185), "Decode").draw(win)

    # Exit Button: Below the encode and decode buttons
    exit_button = Rectangle(Point(150, 230), Point(250, 260))  # Exit button position
    exit_button.setFill("lightgray")
    exit_button.draw(win)
    Text(Point(200, 245), "Exit").draw(win)

    output_text = Text(Point(200, 280), "")
    output_text.draw(win)


 
    while True: # not supposed to use while true because its an infinite loop which can often cause issues
    # instead it should be: while not 150 < click.getX() < 250 and 230 < click.getY() < 260:  # Exit button
    
        click = win.getMouse()
        key = key_box.getText()

        if key.isdigit():
            key = int(key)
            message = input_box.getText()

            if 100 < click.getX() < 200 and 170 < click.getY() < 200:  # Encode button
                output_text.setText(caesar_cipher(message, key))
            elif 220 < click.getX() < 320 and 170 < click.getY() < 200:  # Decode button
                output_text.setText(caesar_cipher(message, -key))
        ################################################################################
        # Wouldnt need this chunk anymore
        elif 150 < click.getX() < 250 and 230 < click.getY() < 260:  # Exit button
            win.close()  # Close the window
            return  # Exit the main loop and terminate the program
        ################################################################################
        else:
            output_text.setText("Invalid Key!")

    win.close()

main()
