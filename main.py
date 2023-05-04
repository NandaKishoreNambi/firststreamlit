import streamlit as st
import random
import keyboard

st.title(":blue[Explore with Satwik] :black_heart:")
st.write("This app is a test for you to explore! Please enter your name below to get started.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! ")
    "Your test has started...! Mark the Correct Answers :sunglasses:"

    score = 0
    question1 = st.radio("1.What is the spelling of number 3 ?", ('Three', 'Nanda', 'Hari', 'Two'))
    question2 = st.radio("2.What is the special occasion on 26th Jan ?",
                         ('None of the above', 'Republic day', "Gandhi's Birthday", 'Independance day'))
    question3 = st.radio("3.Who is the prime minister of india ?",
                         ('Narendra modi', 'Rakesh jujunwala', 'Nirav modi', 'Satwik nadella'))
    question4 = st.radio("4.What is the capital of Telangana ?", ('Hyderabad ', 'Mumbai', 'Bombay', 'Delhi'))
    if question1 == 'Three':
        score += 1
    if question2 == 'Republic day':
        score += 1
    if question3 == 'Narendra modi':
        score += 1
    if question4 == 'Hyderabad':
        score += 1
    end = st.button("Click here to end the test ")
    if end:
        if score >= 3:
            st.write(name, 'your score was good enough')
        if score < 3:
            st.write(name, 'your score was not that great')
            st.write("Try to take the test again ")
            st.button("Refresh ")
            if st.button:
                keyboard.press_and_release('ctrl+f5')




