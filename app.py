import streamlit as st

st.header("Tic-Tac-Toe AI")
st.write("This project implements Tic-Tac-Toe using Minimax algorithm.")

if st.button("Show Tic-Tac-Toe Info"):
    st.write("Algorithm: Minimax")
    st.write("AI evaluates all possible moves.")
    st.write("Chooses the best move to win or draw.")
    st.write("AI never loses.")
    
    st.subheader("Sample Board")
    st.text("""
X | O | X
O | X | O
X |   | O
""")

st.header("Evacuation Planner")
st.write("This project simulates evacuation using BFS.")

if st.button("Show Evacuation Steps"):
    steps = [
        "(3, 0, 'L')",
        "(1, 2, 'R')",
        "(2, 1, 'L')",
        "(0, 3, 'R')"
    ]

    st.subheader("Steps:")
    for i, step in enumerate(steps):
        st.write(f"Step {i+1}: {step}")
