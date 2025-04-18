import streamlit as st
import random
from hangman_words import word_list
from hangman_art import stages, logo

# Setup initial game state
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.correct_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False

# Display logo
st.title("💀 Hangman Game")
st.text(logo)

# Show current lives and hangman stage
st.markdown(f"### ❤️ Lives left: {st.session_state.lives}/6")
st.text(stages[st.session_state.lives])

# Display the current word progress
display = ""
for letter in st.session_state.chosen_word:
    if letter in st.session_state.correct_letters:
        display += letter
    else:
        display += "_"

st.markdown(f"### Word to guess: `{display}`")

# Input guess from user
if not st.session_state.game_over:
    guess = st.text_input("Guess a letter: ").lower()

    if guess:
        if guess in st.session_state.correct_letters:
            st.warning(f"You already guessed '{guess}'")
        elif guess in st.session_state.chosen_word:
            st.session_state.correct_letters.append(guess)
            st.success(f"'{guess}' is in the word!")
        else:
            st.session_state.correct_letters.append(guess)
            st.session_state.lives -= 1
            st.error(f"'{guess}' is NOT in the word. You lose a life.")

        # Recalculate display after guess
        display = ""
        for letter in st.session_state.chosen_word:
            if letter in st.session_state.correct_letters:
                display += letter
            else:
                display += "_"

        if "_" not in display:
            st.balloons()
            st.success("YOU WIN! 🎉")
            st.session_state.game_over = True

        if st.session_state.lives == 0:
            st.error(f"YOU LOSE! The word was `{st.session_state.chosen_word}` 😵")
            st.session_state.game_over = True

# Reset button
if st.session_state.game_over:
    if st.button("🔁 Play Again"):
        st.session_state.chosen_word = random.choice(word_list)
        st.session_state.correct_letters = []
        st.session_state.lives = 6
        st.session_state.game_over = False
