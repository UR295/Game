import streamlit as st
import random
st.set_page_config(page_title="Rock_Paper_Scissor Game", page_icon="🎮")

def get_computer_move():
    moves = {1: "rock🪨", 2: "paper📃", 3: "scissor✂️"}
    return random.randint(1, 3), moves[random.randint(1, 3)]

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a draw!"
    elif (player_move == "rock🪨" and computer_move == "scissor✂️") or \
         (player_move == "paper📃" and computer_move == "rock🪨") or \
         (player_move == "scissor✂️" and computer_move == "paper📃"):
        return "You win!"
    else:
        return "Computer wins!"

st.title("Rock, Paper, Scissor Game!")
st.write("You are playing against the computer!")

name = st.text_input("Enter player name:")
if name:
    st.write(f"Welcome, {name}!")

player_move = st.selectbox ("Choose your move:", ["rock🪨", "paper📃", "scissor✂️"])
if st.button("Play"):
    player_choice = player_move.lower()
    computer_choice_num, computer_choice = get_computer_move()

    st.write(f"You chose: {player_choice.capitalize()}")
    st.write(f"Computer chose: {computer_choice.capitalize()}")

    result = determine_winner(player_choice, computer_choice)
    st.write(result)

st.write("Thanks for playing! 😁")

