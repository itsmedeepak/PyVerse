from time import time

def count_errors(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    errors = 0

    for i in range(len(original_words)):
        if i >= len(typed_words) or original_words[i] != typed_words[i]:
            errors += 1

    # count extra typed words as errors
    if len(typed_words) > len(original_words):
        errors += len(typed_words) - len(original_words)

    return errors

def typing_speed(typed_words, elapsed_time):
    # speed in words per minute
    speed_wpm = (len(typed_words.split()) / elapsed_time) * 60
    return round(speed_wpm, 2)

def elapsed_time(start, end):
    return round(end - start, 2)

if __name__ == '__main__':
    prompt = ("Python is a high-level, general-purpose programming language. "
              "Its design philosophy emphasizes code readability with the use of significant indentation. "
              "Python is dynamically-typed and garbage-collected. "
              "It supports multiple programming paradigms, including structured, object-oriented and functional programming.")

    while True:
        print("\nType the following prompt:\n")
        print(prompt, "\n")
        input("Press Enter when ready to start...")

        start_time = time()
        typed_input = input("\nStart typing here: ")
        end_time = time()

        total_time = elapsed_time(start_time, end_time)
        speed = typing_speed(typed_input, total_time)
        errors = count_errors(prompt, typed_input)

        print("\n--- Results ---")
        print(f"Total time elapsed: {total_time} seconds")
        print(f"Your typing speed: {speed} words per minute")
        print(f"Total errors: {errors}")

        retry = input("\nDo you want to try again? (y/n): ").lower()
        if retry != 'y':
            print("Thanks for playing! 👋")
            break
