from fastapi import FastAPI
from .router import user, item
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
origins = [
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(item.router)


def api_main():

    uvicorn.run("api.api_server:app", host="localhost", port=80, reload=True, log_level="info")