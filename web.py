import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    #specyficzny typ danych streamlit, coś jak słownik wczytujemy key i dostajemy wartość pary
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To Do App")
st.subheader("My To Do App")
st.write("My To Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: #jezeli zaznaczamy
        todos.pop(index) #usuwamy z listy
        functions.write_todos(todos) #aktualizujemy liste
        del st.session_state[todo] #usuwamy stan sesji obecny aby odswiezyc
        st.rerun() #odświeza strone

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")