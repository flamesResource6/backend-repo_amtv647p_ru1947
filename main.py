import os
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Tools API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tool(BaseModel):
    id: str
    name: str
    slug: str
    category: str
    tags: List[str]
    description: str
    client_only: bool = True

# Initial catalog (we can grow this list)
TOOLS: List[Tool] = [
    Tool(
        id="text-case",
        name="Text Case Converter",
        slug="text-case",
        category="Text",
        tags=["text", "case", "uppercase", "lowercase"],
        description="Convert text to UPPERCASE, lowercase, Title Case, and more — all in your browser.",
        client_only=True,
    ),
    Tool(
        id="url-encoder",
        name="URL Encoder / Decoder",
        slug="url-encoder",
        category="Web",
        tags=["url", "encode", "decode"],
        description="Encode or decode URLs safely without sending data to a server.",
        client_only=True,
    ),
    Tool(
        id="image-resizer",
        name="Image Resizer",
        slug="image-resizer",
        category="Images",
        tags=["image", "resize", "compress", "png", "jpg"],
        description="Resize and compress images locally in your browser.",
        client_only=True,
    ),
]

@app.get("/")
def read_root():
    return {"message": "Tools API running"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}

@app.get("/api/tools", response_model=List[Tool])
def list_tools(q: Optional[str] = None, category: Optional[str] = None):
    items = TOOLS
    if category:
        items = [t for t in items if t.category.lower() == category.lower()]
    if q:
        ql = q.lower()
        items = [
            t for t in items
            if ql in t.name.lower()
            or ql in t.description.lower()
            or any(ql in tag.lower() for tag in t.tags)
        ]
    return items

@app.get("/test")
def test_database():
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Used",
        "database_url": None,
        "database_name": None,
        "connection_status": "No DB needed for client-only tools",
        "collections": []
    }

    # Env check for completeness
    response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
    response["database_name"] = "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set"
    return response

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
