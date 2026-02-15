import pywhatkit as kit
import cv2 #using this to see my result

def text_to_handwriting(text, filename="assignment.png"):
    try:
        print("Converting text... please wait.")
        
        # rgb parameter sets the ink color (0, 0, 138 is a nice dark blue ink)
        kit.text_to_handwriting(text, save_to=filename, rgb=(0, 0, 138))
        
        print(f"Success! Your assignment is saved as {filename}")
        
        # Optional: Show the image immediately
        img = cv2.imread(filename)
        cv2.imshow("Handwritten Assignment", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    my_text = """
    Python is an interpreted, high-level and general-purpose programming language. 
    Python's design philosophy emphasizes code readability with its notable use 
    of significant whitespace. Its language constructs and object-oriented 
    approach aim to help programmers write clear, logical code for small and 
    large-scale projects.
    """
    
    text_to_handwriting(my_text)