import streamlit as st
import random

st.set_page_config(page_title="Rock_Paper_Scissor Game", page_icon="🎮")

def get_computer_move():
    moves = {1: "rock🪨", 2: "paper📃", 3: "scissor✂️"}
    choice_num = random.randint(1, 3)
    return choice_num, moves[choice_num]

def determine_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return "It's a draw!"
    elif (player1_move == "rock🪨" and player2_move == "scissor✂️") or \
         (player1_move == "paper📃" and player2_move == "rock🪨") or \
         (player1_move == "scissor✂️" and player2_move == "paper📃"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

st.title("Rock, Paper, Scissor Game!")

mode = st.radio("Choose Game Mode:", ("Single Player (vs Computer)", "Multiplayer"))

if mode == "Single Player (vs Computer)":
    st.write("You are playing against the computer!")
    
    name = st.text_input("Enter player name:")
    if name:
        st.write(f"Welcome, {name}!")

    player_move = st.selectbox("Choose your move:", ["rock🪨", "paper📃", "scissor✂️"])
    
    if st.button("Play"):
        player_choice = player_move.lower()
        computer_choice_num, computer_choice = get_computer_move()

        st.write(f"You chose: {player_choice.capitalize()}")
        st.write(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(player_choice, computer_choice)
        st.write(result)

elif mode == "Multiplayer":
    st.write("Multiplayer Mode - Two players can play against each other!")

    # Player 1
    player1_name = st.text_input("Enter Player 1 name:")
    if player1_name:
        st.write(f"Welcome, {player1_name}!")

    player1_move = st.selectbox("Player 1, choose your move:", ["rock🪨", "paper📃", "scissor✂️"], key='player1_move')

    # Player 2
    player2_name = st.text_input("Enter Player 2 name:")
    if player2_name:
        st.write(f"Welcome, {player2_name}!")

    player2_move = st.selectbox("Player 2, choose your move:", ["rock🪨", "paper📃", "scissor✂️"], key='player2_move')

    if st.button("Play"):
        if not player1_name or not player2_name:
            st.write("Please enter both player names.")
        else:
            st.write(f"{player1_name} chose: {player1_move}")
            st.write(f"{player2_name} chose: {player2_move}")

            result = determine_winner(player1_move, player2_move)
            st.write(result)

st.write("Thanks for playing! 😁")
