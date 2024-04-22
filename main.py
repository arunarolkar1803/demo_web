import streamlit as st

st.title("Welcome to the Legend World")
name=st.text_input("Enter Your Name: ")
fname=st.text_input("Enter Father Name:")
address=st.text_area("Enter Your Address: ")
classdata=st.selectbox("Select Your Class : ",(1,2,3,4,5))

btn=st.button("Sava")
if btn:
    st.markdown(f"""
            Name : {name}
            Father Name: {fname}
            Address : {address}
            Class: {classdata}""")