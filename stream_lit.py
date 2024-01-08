import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Fast Api Todo App")

def create_todo():
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        respone = requests.post(f"{BASE_URL}/todo/create/", json={"title": title, "description": description})
        if respone.status_code == 200:
            st.success("Todo Created Successfully")


def delete_todo():
    todo_id = st.number_input("Enter Todo Id")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todo/{todo_id}")
        if response.status_code == 200:
            st.success("Todo Deleted Successfully")


if __name__ == "__main__":
    create_todo()
    delete_todo()