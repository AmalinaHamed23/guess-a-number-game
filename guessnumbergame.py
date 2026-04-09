import streamlit as st
import random

# Page config
st.set_page_config(page_title="Guess A Number Game", page_icon="🎯")

st.title("🎯 Guess A Number Game")
st.header ("I will pick a number between 1 and 50. Try to guess it!")
st.write("Challenge yourself to guess the correct number in 5 Attempts!")

name = st.text_input ('What is Your Name?')
if name:
    st.success (f'Hye **{name}**. Are you ready? ')


# Initialize session state (only run once)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 50)

if "attempt" not in st.session_state:
    st.session_state.attempt = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Show attempt
st.write(f"Attempt: {st.session_state.attempt} / 5")

# Input
guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

# Submit button
if st.button("Submit Guess") and not st.session_state.game_over:

    # Correct guess
    if guess == st.session_state.number:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempt} attempts!")
        st.session_state.game_over = True

    else:
        # Increase attempt
        st.session_state.attempt += 1

        # Give hint
        if guess > st.session_state.number:
            st.warning("Too high! ⬆️")
        else:
            st.warning("Too low! ⬇️")

        # Check if out of attempts
        if st.session_state.attempt > 5:
            st.error(f"😢 Game Over! The number was {st.session_state.number}")
            st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        st.session_state.number = random.randint(1, 50)
        st.session_state.attempt = 1
        st.session_state.game_over = False