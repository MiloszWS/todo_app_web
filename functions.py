import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w"):
        pass

FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """To jest przyklad docstringu, mozna to helpowac"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    """ogolnie to __name__ jest rowna temu co ja uruchamia
    jak odpale to przez maina to bedzie functions a jak odpale
    wewnatrz tego to bedzie main"""