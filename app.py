import streamlit as st

st.title("SHL Assessment Recommender")

query = st.text_input("Enter your requirement")

if st.button("Get Recommendations"):
    # call your agent logic here
    from app.agent import get_recommendations
    
    result = get_recommendations(query)
    
    st.write(result)

    