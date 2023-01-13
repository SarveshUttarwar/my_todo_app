import streamlit as st
import functions
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("this is my todo app.")
st.write("this app is to increase your productivity.")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="add new todo....",on_change=add_todo, key = 'new_todo')
print("hello")

st.session_state
