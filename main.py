from fastapi import FastAPI

app = FastAPI()

@app.get("/hello ord")
async def root():
    return {"message": "teste2 World"}