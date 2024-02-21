from fastapi import FastAPI

app= FastAPI()

@app.get('/')
async def Home():
    return {"main":"Hello from the main world"}