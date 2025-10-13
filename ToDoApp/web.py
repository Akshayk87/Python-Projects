import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("To-Do App")
# st.subheader("This is my todo app.")
# st.write("This app is to increase your productivity.")
st.date_input("Today is ", value = "today", key = "date", format="DD-MM-YYYY")


for index, todo in enumerate(todos):
    # checkbox = st.checkbox(todo, key=todo)
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # del st.session_state[todo]
        # del st.session_state[f"todo_{index}"]
        key = f"todo_{index}"
        if key in st.session_state:
            st.session_state.pop(key)
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')