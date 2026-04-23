import streamlit as st

st.title("AI Problem Solving Assignment")

st.header("Tic-Tac-Toe AI")
st.write("This project implements Tic-Tac-Toe using Minimax algorithm.")

if st.button("Show Tic-Tac-Toe Info"):
    st.write("AI always plays optimal moves.")

st.header("Evacuation Planner")
st.write("This project simulates evacuation using BFS.")

if st.button("Show Evacuation Steps"):
    steps = [
        "(3, 0, 'L')",
        "(1, 2, 'R')",
        "(2, 1, 'L')",
        "(0, 3, 'R')"
    ]
    for step in steps:
        st.write(step)
