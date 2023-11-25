from fastapi import FastAPI
from routers.router import router as api_router
from routers.socket import socket as api_socket
import uvicorn

app = FastAPI()

app.include_router(api_router)
app.include_router(api_socket)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
    # uvicorn main:app --port 5000 --host '0.0.0.0' --reload
