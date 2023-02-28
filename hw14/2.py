from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
import requests
app = FastAPI()

url = "http://127.0.0.1:8000/"
class UserIn(BaseModel):
    email: str
    username: str
    password: str


class UserOut(BaseModel):
    email: str
    username: str


@app.post("/home", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def show_user(user: UserIn):
    if user.username == "admin":
        r = requests.post(url, data={"message": "error500"})
        print(r.status_code)
        raise HTTPException(detail="username cant be admin", status_code=status.HTTP_400_BAD_REQUEST)

    return user

# except Exception as exep:
# logging.error("cant create user")
# return exep