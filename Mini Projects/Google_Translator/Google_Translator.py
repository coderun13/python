from deep_translator import GoogleTranslator

def translate_text(text, target_lang='en'):
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        
        translation = translator.translate(text)
        
        print(f"\n--- Translation Result ---")
        print(f"Original: {text}")
        print(f"Translated ({target_lang}): {translation}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Python Google Translator (Python 3.13 Compatible)")
    user_text = input("Enter text: ")
    
    # Common codes: 'es' (Spanish), 'fr' (French), 'hi' (Hindi), 'de' (German)
    target = input("Enter target language code (e.g., 'es', 'hi', 'en'): ") or 'en'
    
    translate_text(user_text, target)