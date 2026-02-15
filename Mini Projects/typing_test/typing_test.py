# The Logic
# Display a random sentence to the user.
# Start the timer the moment they press Enter.
# Calculate the time difference once they finish typing.
# Compare their input to the original sentence to check for accuracy.

import time
import random

def typing_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile programming language for beginners.",
        "Practice makes perfect when learning how to code.",
        "Typing fast is a skill that requires consistency."
    ]
    
    # Pick a random sentence
    target_text = random.choice(sentences)
    
    print("\n--- Typing Speed Test ---")
    print("Type the following sentence exactly as shown:")
    print(f"\n\"{target_text}\"\n")
    
    input("Press ENTER when you are ready to start...")
    
    start_time = time.time() # Record start time
    user_input = input("\nStart typing: ")
    end_time = time.time()   # Record end time
    
    # Calculate results
    time_taken = end_time - start_time
    words = len(target_text.split())
    wpm = (words / time_taken) * 60
    
    # Check Accuracy
    if user_input == target_text:
        accuracy = 100
    else:
        # Simple accuracy: correct characters / total characters
        correct_chars = sum(1 for i, j in zip(user_input, target_text) if i == j)
        accuracy = (correct_chars / len(target_text)) * 100

    print("\n-------------------------")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print("-------------------------")

if __name__ == "__main__":
    typing_test()