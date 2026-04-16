from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import predict, store, results

app = FastAPI(title="AI Navigation Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router)
app.include_router(store.router)
app.include_router(results.router)


@app.get("/")
def home():
    return {"message": "Backend is running"}