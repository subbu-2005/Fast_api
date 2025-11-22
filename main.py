from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from bson import ObjectId
from pymongo import AsyncMongoClient
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import json

app = FastAPI()


# ========== ADD MIDDLEWARE HERE ==========
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("🔵 Request came in!")
        print(f"   Method: {request.method}")
        print(f"   Path: {request.url.path}")

        response = await call_next(request)

        print("🟢 Response sent out!")
        print(f"   Status Code: {response.status_code}")

        return response


app.add_middleware(LoggingMiddleware)
# =========================================

# Connect to MongoDB (async client)
client = AsyncMongoClient("mongodb+srv://fast:fast@cluster0.osr2phu.mongodb.net/")
db = client["mydatabase"]
collection = db["items"]


@app.on_event("startup")
async def startup_db():
    try:
        # Ping the server
        ping = await db.command("ping")
        if ping.get("ok") == 1:
            print("✅ Successfully connected to MongoDB")
        else:
            print("❌ Failed to ping MongoDB:", ping)
    except Exception as e:
        print("❌ Error connecting to MongoDB on startup:", e)


# Pydantic model for item
class Item(BaseModel):
    name: str
    price: float


# POST method – create item
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def mcreate_item(item: Item):
    item_dict = item.dict()
    result = await collection.insert_one(item_dict)
    created = await collection.find_one({"_id": result.inserted_id})

    response_data = {
        "id": str(created["_id"]),
        "name": created["name"],
        "price": created["price"],
    }

    print(f"📤 Response Data: {response_data}")

    return response_data

# GET method – read all items
# @app.get("/items/")
# async def get_items():
#     items = []
#     cursor = collection.find({"price": {"$gt": 40}})
#     async for doc in cursor:
#         items.append({
#             "id": str(doc["_id"]),
#             "name": doc.get("name"),
#             "price": doc.get("price"),
#         })
#     return items

# PUT (update) method – commented out for now
# @app.put("/items/{item_id}")
# async def update_item(item_id: str, item: Item):
#     if not ObjectId.is_valid(item_id):
#         raise HTTPException(status_code=400, detail="Invalid ID")
#     result = await collection.update_one(
#         {"_id": ObjectId(item_id)},
#         {"$set": {"name": item.name, "price": item.price}}
#     )
#     if result.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Item not found")
#     updated = await collection.find_one({"_id": ObjectId(item_id)})
#     return {
#         "id": str(updated["_id"]),
#         "name": updated["name"],
#         "price": updated["price"],
#     }

# DELETE method – commented out for now
# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(item_id: str):
#     if not ObjectId.is_valid(item_id):
#         raise HTTPException(status_code=400, detail="Invalid ID")
#     result = await collection.delete_one({"_id": ObjectId(item_id)})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return