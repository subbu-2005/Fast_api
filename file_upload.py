from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

# Create "uploads" folder if not exists
os.makedirs("uploads", exist_ok=True)

# -----------------------------------------
# 1. Upload file and show details + log
# -----------------------------------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    print(f"✅ File received: {file.filename}")
    print(f"📦 Size: {len(contents)} bytes")
    print(f"📄 Type: {file.content_type}")

    return {
        "status": "success",
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }


# -----------------------------------------
# 2. Upload + SAVE file + log
# -----------------------------------------
@app.post("/save-file")
async def save_file(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"uploads/{file.filename}"

    # Save file
    with open(file_path, "wb") as f:
        f.write(contents)

    print(f"💾 File saved successfully!")
    print(f"📁 Saved at: {file_path}")

    return {
        "status": "success",
        "message": "File saved successfully!",
        "saved_as": file.filename,
        "file_path": file_path
    }
