import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Nadezhda Evdokimova")
    content = """
    My name is Nadya. Enthusiastic and detail-oriented entry-level Python developer with a passion for creating
     efficient and scalable software solutions. I have successfully completed projects that 
     demonstrate my ability to design and implement clean, maintainable code while continuously seeking opportunities
      to expand my knowledge.
    """
    st.info(content)

st.write("Below you can find some of the apps I have build in Python. Feel free to contact me.")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
