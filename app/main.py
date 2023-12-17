from fastapi import FastAPI
from enum import Enum



class ModleName(str, Enum):
    Tarig = "Tarig"
    Jafar = "Jafar"
    Saad = "Saad"

app = FastAPI()


@app.get("/{MemberName}")
def Root(MemberName:ModleName):
    return {"message": {MemberName} }

