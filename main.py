from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

usuarios = [
    {
        "UserName": "cahtget",
        "Password": "caihdsda"
    },
    {
        "UserName": "cahtget",
        "Password": "caihdsda"
    },
    {
        "UserName": "cahtget",
        "Password": "caihdsda"
    }
]

@app.get("/user/all/")
def list_all_users():
    return usuarios

@app.get("/user/{id_user}")
def view_one_user_id(id_user: str):
    for i in usuarios:
        if i['UserName'] == id_user:
            return i
    return {"Message": "User does'nt exist"}
        

'''@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}'''