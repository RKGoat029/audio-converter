from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React default
        "http://localhost:5173",  # Vite default
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    value: str

@app.post("/submit")
async def receive_data(data: InputData):
    print(f"Received value: {data.value}")
    # You can process the data here or save it to DB, etc.
    return {"message": f"Value '{data.value}' received successfully!"}

app.include_router(router)