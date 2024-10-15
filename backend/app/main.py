from fastapi import FastAPI

app = FastAPI()

# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Welcome to my receipt collection FastAPI app"}

# Add another route for handling receipts (example)
@app.get("/receipts/")
def read_receipts():
    return {"receipts": ["Soup", "Salad", "Pasta"]}
