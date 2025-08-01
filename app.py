import streamlit as st
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

# Set page config
st.set_page_config(
    page_title="AutoCorrect App",
    page_icon="✨",
    layout="centered"
)

# Add title and description
st.title("✨ AutoCorrect App")
st.markdown("""
This app helps you correct spelling mistakes in your text. 
Simply type or paste your text below and see the corrected version!
""")

# Create text input
user_input = st.text_area("Enter your text here:", height=150)

# Add a button to trigger the correction
if st.button("Correct Text"):
    if user_input:
        # Show a spinner while processing
        with st.spinner("Correcting text..."):
            corrected_text = autocorrect_text(user_input)
            
            # Display the results in two columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Original Text")
                st.write(user_input)
            
            with col2:
                st.subheader("Corrected Text")
                st.write(corrected_text)
    else:
        st.warning("Please enter some text to correct!") 