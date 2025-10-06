from fastapi import FastAPI

app = FastAPI(title="AI Interview Coach")


@app.get("/")
async def root():
    return {"message": "Welcome to the AI Interview Coach API"}