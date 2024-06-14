from graphics import *
import random

def create_widgets(win):
    global guess_entry, guess_button, result_text, restart_button, guess_button_rect, restart_button_rect

    # Set background color
    background_color = 'lightgrey'
    win.setBackground(background_color)

    title = Text(Point(250, 50), "High Low Game")
    title.setSize(20)
    title.draw(win)

    info = Text(Point(250, 100), "I'm thinking of a number between 1 and 100.")
    info.setSize(14)
    info.draw(win)
    
    guess_entry = Entry(Point(250, 150), 10)
    guess_entry.setFill(background_color)
    guess_entry.setSize(14)
    guess_entry.draw(win)
    
    guess_button = Text(Point(250, 200), "Guess")
    guess_button.setSize(14)
    guess_button.draw(win)
    guess_button_rect = Rectangle(Point(200, 185), Point(300, 215))
    guess_button_rect.draw(win)
    
    result_text = Text(Point(250, 250), "")
    result_text.setSize(16)
    result_text.draw(win)

    restart_button = Text(Point(250, 300), "Play Again")
    restart_button.setSize(14)
    restart_button.draw(win)
    restart_button_rect = Rectangle(Point(200, 285), Point(300, 315))
    restart_button_rect.draw(win)

def check_guess():
    global num_guesses
    guess = guess_entry.getText()
    
    if not guess.isdigit():
        result_text.setText("Please enter a valid number.")
        result_text.setTextColor("red")
    else:
        guess = int(guess)
        if guess < 1 or guess > 100:
            result_text.setText("Please enter a number between 1 and 100.")
            result_text.setTextColor("red")
        else:
            num_guesses += 1
            if guess < secret_number:
                result_text.setText(f"{guess} < ? Try again.")
                result_text.setTextColor("blue")
            elif guess > secret_number:
                result_text.setText(f"{guess} > ? Try again.")
                result_text.setTextColor("blue")
            else:
                result_text.setText(f"Congratulations! You guessed the number {secret_number} "
                                    f"in {num_guesses} guesses!")
                result_text.setTextColor("green")
                guess_button.setText("Disabled")
                guess_button_rect.setOutline("grey")
    
    guess_entry.setText("")

def restart_game():
    global secret_number, num_guesses
    secret_number = random.randint(1, 100)
    num_guesses = 0
    result_text.setText("")
    guess_button.setText("Guess")
    guess_button_rect.setOutline("black")

def main():
    global secret_number, num_guesses, guess_button_rect, restart_button_rect, win
    win = GraphWin("High Low Game", 500, 400)
    
    secret_number = random.randint(1, 100)
    num_guesses = 0
    
    create_widgets(win)
    
    while True:
        click_point = win.getMouse()
        if guess_button_rect.getP1().getX() <= click_point.getX() <= guess_button_rect.getP2().getX() and \
           guess_button_rect.getP1().getY() <= click_point.getY() <= guess_button_rect.getP2().getY():
            check_guess()
        elif restart_button_rect.getP1().getX() <= click_point.getX() <= restart_button_rect.getP2().getX() and \
             restart_button_rect.getP1().getY() <= click_point.getY() <= restart_button_rect.getP2().getY():
            restart_game()

if __name__ == "__main__":
    main()
