import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)

def add_data(task):
    supabase.table("your_table_name").insert({"column1": task, "column2": "value2"}).execute()

def get_todo():
    data = supabase.table("your_table_name").select("*").execute()
    return data.data

task = st.text_input("Enter a task")
if st.button("Add Task"):
    if task:
        add_data(task)
        st.success("Task added successfully!")
    else:
        st.error("Please enter a task")

st.header("Todo List")
todos = get_todo()
if todos:
    for todo in todos:
        st.write(todo["column1"])
else:    
    st.write("No tasks found")