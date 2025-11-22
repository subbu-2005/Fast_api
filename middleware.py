from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

app = FastAPI()

# ========== MIDDLEWARE (This runs before and after your route) ==========
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("🔵 Request came in!")
        response = await call_next(request)
        print("🟢 Response sent out!")
        return response

app.add_middleware(LoggingMiddleware)

# ========== YOUR ROUTE ==========
@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}