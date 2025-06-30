import time

def print_slowly(text, delay=0.05):
    """Prints text slowly, like dialogue."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def welcome_and_get_name():
    """Handles the initial welcome and gets the player's name."""
    player_name = ""
    print_slowly("Professor Hoot: Hooooo! Welcome, young adventurer!")
    time.sleep(0.5)
    print_slowly("Professor Hoot: I am Professor Hoot, and I'm thrilled to guide you on a magical journey into the world of Python!")
    time.sleep(0.5)

    while not player_name.strip():
        player_name_prompt = "Professor Hoot: First, what should I call you? "
        print_slowly(player_name_prompt, delay=0.03)
        player_name = input()
        if not player_name.strip():
            print_slowly("Professor Hoot: Oh, don't be shy! Every great adventurer has a name.")

    print_slowly(f"Professor Hoot: A pleasure to meet you, {player_name}!")
    return player_name

def chapter_1_learn_print(player_name):
    """Teaches the print() command."""
    print_slowly("\n--- Chapter 1: The First Magic Word ---")
    time.sleep(0.5)
    print_slowly("Professor Hoot: Today, we'll learn our very first 'magic word' in Python.")
    print_slowly("Professor Hoot: It's called `print()`.")
    time.sleep(0.5)
    print_slowly("Professor Hoot: This magic word lets us display any message on the screen, like telling Python to announce something out loud!")
    print_slowly("Professor Hoot: To use it, you type `print()` and put your message inside the parentheses, surrounded by quotation marks.")
    print_slowly("Professor Hoot: Like this: `print(\"Your message here\")`")
    print_slowly("Professor Hoot: The quotation marks (either `\"\"` or `''`) tell Python that this is a piece of text, or what we call a **string** of characters.")
    time.sleep(1)

    print_slowly("\nProfessor Hoot: Let's try it! Can you help me greet our lovely forest?")
    target_message = "Hello, Forest!"
    print_slowly(f"Professor Hoot: I want to say: {target_message}")

    attempts = 0
    correct_command_dbl_quotes = f"print(\"{target_message}\")"
    correct_command_sgl_quotes = f"print('{target_message}')"

    common_mistakes = {
        f"print({target_message})": "Professor Hoot: So close! Remember, text messages (we call them strings) need to be wrapped in quotation marks like `\"Hello, Forest!\"`.",
        f"print \"{target_message}\"": "Professor Hoot: Almost! In this version of Python's magic, the message needs to be inside the parentheses, like `print(\"Your message here\")`.",
        f"Print(\"{target_message}\")": "Professor Hoot: Careful now, Python's magic words are case-sensitive. The magic word is `print` in all lowercase."
    }

    while attempts < 3:
        prompt = f"Professor Hoot ({player_name}, your turn): "
        print_slowly(prompt, delay=0.03)
        user_input = input().strip() # Strip here to catch leading/trailing whitespace on the whole command

        if user_input == correct_command_dbl_quotes or user_input == correct_command_sgl_quotes:
            print_slowly("Professor Hoot: Wonderful! You've done it!")
            print_slowly("------------------------------------")
            print_slowly(">>> Python Output:")
            print_slowly(f">>> {target_message}")
            print_slowly("------------------------------------")
            time.sleep(0.5)
            print_slowly(f"Professor Hoot: See, {player_name}? You made Python speak! That's the power of `print()`.")
            print_slowly("Professor Hoot: You're a natural Python magician!")
            print_slowly("Professor Hoot: For mastering your first magic word, `print()`, you've earned the 'Chatty Owlet Badge'! Hoo-ray!")
            return True # Chapter success
        else:
            attempts += 1
            found_specific_feedback = False
            # Check common mistakes first
            for mistake_pattern, feedback in common_mistakes.items():
                # A more robust check might be needed for complex patterns, but this is okay for now.
                if user_input.lower() == mistake_pattern.lower() and mistake_pattern.startswith("Print("): # Case-insensitive check only for Print command itself
                     print_slowly(feedback)
                     found_specific_feedback = True
                     break
                elif user_input == mistake_pattern:
                    print_slowly(feedback)
                    found_specific_feedback = True
                    break

            if not found_specific_feedback:
                # Check if user just typed the message
                if user_input.lower() == target_message.lower():
                    print_slowly(f"Professor Hoot: That's the message we want to print! But we need to tell Python *to print* it using the `print()` magic word, like `{correct_command_dbl_quotes}`.")
                    found_specific_feedback = True
                elif not user_input.startswith("print("):
                     print_slowly(f"Professor Hoot: Hmm, that doesn't look like a print command. Remember, it starts with `print(...)`.")
                     found_specific_feedback = True


            if not found_specific_feedback:
                print_slowly("Professor Hoot: Hmm, that doesn't seem to be the right magic spell.")

            if attempts < 3:
                print_slowly(f"Professor Hoot: Let's try that again. Remember: `{correct_command_dbl_quotes}`")
            else:
                print_slowly(f"Professor Hoot: Don't worry, {player_name}! Learning takes practice.")
                print_slowly(f"Professor Hoot: The correct magic spell was: {correct_command_dbl_quotes}")
                print_slowly("------------------------------------")
                print_slowly(">>> Python Output (if correct):")
                print_slowly(f">>> {target_message}")
                print_slowly("------------------------------------")
                print_slowly("Professor Hoot: We'll get plenty more chances to practice!")
                return False # Chapter failure/completion without full success

    return False # Should be unreachable if loop finishes, but as a fallback

# Main game execution
if __name__ == "__main__":
    player_name = welcome_and_get_name()

    if chapter_1_learn_print(player_name):
        print_slowly(f"\nProfessor Hoot: That's all for our first lesson with `print()`, {player_name}. Well done!")
        print_slowly("Professor Hoot: Come back soon to learn how Python remembers things in Chapter 2!")
    else:
        print_slowly(f"\nProfessor Hoot: Even though we hit a little snag, you learned a lot about `print()`, {player_name}!")
        print_slowly("Professor Hoot: Don't hesitate to try again or join me for Chapter 2 when you're ready!")

# Basic structure for Chapter 1: print() - Refactored
# - Welcome and get name (separate function)
# - Explain print() in chapter_1_learn_print
# - Task: print("Hello, Forest!")
# - Feedback: Correct, or specific hints for common errors (missing quotes, wrong case for print, missing print command)
# - Standardized simulated output
# - Max attempts for the task
# - Concluding message for chapter and game session
#
# Future improvements:
# - More sophisticated input parsing/error checking for varied user inputs.
# - Storing game state (which chapter the player is on for multi-session play).
# - More interactive elements/choices.
# - Clearer separation of game logic and story content (e.g., moving dialogue to a separate structure/file).
# - Robust help system.
