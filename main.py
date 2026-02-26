from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello, AI backend world!"
    }

@app.get("/about")
def about():
    return {
        "name": "Abdullah",
        "goal": "AI Engineer"
    }

@app.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "square": number * number
    }