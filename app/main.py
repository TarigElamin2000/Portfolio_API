from fastapi import FastAPI
from schema import Create_User

app = FastAPI()


@app.get("/")
def Root():
    return {"message": "Hello There" }

@app.post("/user")
def CreateUser(New_User : Create_User):
    print(type(New_User))
    return {**New_User.dict()}

