from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def sum_values(d: dict):
    s = sum(d.values())
    return s


"""sample example """

# {"thing":"money"} ==> {"iphone 13: 1000"}
