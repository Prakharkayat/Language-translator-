from googletrans import Translator, LANGUAGES

def translate_text(text, src_language='auto', dest_language='en'):
    """
    Translates the given text from the source language to the destination language.
    
    Parameters:
    - text (str): The text to be translated.
    - src_language (str): The source language code (default is 'auto' to auto-detect).
    - dest_language (str): The destination language code (default is 'en' for English).
    
    Returns:
    - str: The translated text.
    """
    translator = Translator()
    translated = translator.translate(text, src=src_language, dest=dest_language)
    return translated.text

def main():
    print("Language Translator")
    print("Available languages:")
    for code, lang in LANGUAGES.items():
        print(f"{code}: {lang}")
    
    text = input("Enter the text you want to translate: ")
    
    src_language = input("Enter the source language code (e.g., 'en' for English, 'es' for Spanish, 'fr' for French, 'auto' for auto-detect): ")
    
    dest_language = input("Enter the destination language code (e.g., 'en' for English, 'es' for Spanish, 'fr' for French): ")
    
    if src_language not in LANGUAGES.keys() and src_language != 'auto':
        print("Invalid source language code.")
        return
    
    if dest_language not in LANGUAGES.keys():
        print("Invalid destination language code.")
        return
    
    translated_text = translate_text(text, src_language, dest_language)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
