from spellchecker import SpellChecker

def autocorrect_text(text):
    spell = SpellChecker()

    words = text.split()
    corrected_words = []

    for word in words:
        # Remove punctuation for better checking
        cleaned_word = ''.join(filter(str.isalnum, word))
        
        # Find the closest matching word
        corrected_word = spell.correction(cleaned_word)
        
        # Append the corrected word or the original word if no correction is found
        corrected_words.append(corrected_word if corrected_word else word)

    return " ".join(corrected_words)

if __name__ == "__main__":
    input_text = input("Enter text: ")
    corrected_text = autocorrect_text(input_text)
    print("Corrected text:", corrected_text) 