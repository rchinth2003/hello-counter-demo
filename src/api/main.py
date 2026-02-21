from fastapi import FastAPI
from threading import Lock

app = FastAPI(title="HelloCounter API")

# simple in-memory counter with lock for thread-safety
_counter = 0
_lock = Lock()


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.post("/counter")
def increment_counter():
    global _counter
    with _lock:
        _counter += 1
        return {"counter": _counter}


@app.get("/")
def root():
    return {"status": "ok"}
