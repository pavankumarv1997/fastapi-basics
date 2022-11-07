import uvicorn
from fastapi import FastAPI
from utilities.mysql import Mysql


app = FastAPI()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@app.get('/')
def index():
    print("Hello world!")


@app.get('/hello')
def hello():
    result = Mysql().select_query("select * from admin")
    print(result)
    return "hello"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8000,workers=1)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
