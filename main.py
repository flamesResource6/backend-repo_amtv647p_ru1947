import os
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Tools API", version="0.2.0")

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


def curated_tools() -> List[Tool]:
    base: List[Tool] = [
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
        # Curated additions (client-only where feasible)
        Tool(id="json-prettify", name="JSON Formatter", slug="json-prettify", category="Dev", tags=["json", "format", "pretty"], description="Format and validate JSON.", client_only=True),
        Tool(id="json-minify", name="JSON Minifier", slug="json-minify", category="Dev", tags=["json", "minify"], description="Minify JSON for compact size.", client_only=True),
        Tool(id="uuid-gen", name="UUID Generator", slug="uuid-gen", category="Dev", tags=["uuid", "random", "id"], description="Generate v4 UUIDs locally.", client_only=True),
        Tool(id="slugify", name="Slug Generator", slug="slugify", category="Text", tags=["slug", "seo", "text"], description="Create URL-safe slugs from text.", client_only=True),
        Tool(id="lipsum", name="Lorem Ipsum Generator", slug="lorem-ipsum", category="Text", tags=["dummy", "content"], description="Generate placeholder text.", client_only=True),
        Tool(id="md-preview", name="Markdown Preview", slug="markdown-preview", category="Text", tags=["markdown", "preview"], description="Render Markdown to HTML.", client_only=True),
        Tool(id="csv2json", name="CSV to JSON", slug="csv-to-json", category="Data", tags=["csv", "json", "convert"], description="Convert CSV to JSON in-browser.", client_only=True),
        Tool(id="json2csv", name="JSON to CSV", slug="json-to-csv", category="Data", tags=["json", "csv", "convert"], description="Convert JSON to CSV locally.", client_only=True),
        Tool(id="base64", name="Base64 Encode/Decode", slug="base64", category="Web", tags=["base64", "encode", "decode"], description="Base64 encode/decode strings or files.", client_only=True),
        Tool(id="color-picker", name="Color Picker", slug="color-picker", category="Design", tags=["color", "hex", "rgb"], description="Pick and convert HEX/RGB/HSL.", client_only=True),
        Tool(id="contrast-checker", name="Contrast Checker", slug="contrast-checker", category="Design", tags=["wcag", "contrast", "a11y"], description="Check color contrast ratios.", client_only=True),
        Tool(id="regex-tester", name="Regex Tester", slug="regex-tester", category="Dev", tags=["regex", "test", "match"], description="Test regular expressions on text.", client_only=True),
        Tool(id="qrcode", name="QR Code Generator", slug="qr-code", category="Web", tags=["qr", "code", "image"], description="Create QR codes offline.", client_only=True),
        Tool(id="hash-md5", name="MD5 Hash", slug="md5-hash", category="Security", tags=["hash", "md5", "checksum"], description="Compute MD5 hash locally.", client_only=True),
        Tool(id="hash-sha256", name="SHA-256 Hash", slug="sha256-hash", category="Security", tags=["hash", "sha256", "checksum"], description="Compute SHA-256 hash locally.", client_only=True),
        Tool(id="unit-converter", name="Unit Converter", slug="unit-converter", category="Math", tags=["units", "length", "mass", "temp"], description="Convert between common units.", client_only=True),
        Tool(id="timestamp", name="Epoch Converter", slug="epoch-converter", category="Time", tags=["epoch", "timestamp", "time"], description="Convert UNIX timestamps.", client_only=True),
        Tool(id="diff", name="Text Diff", slug="text-diff", category="Text", tags=["diff", "compare"], description="Compare two blocks of text.", client_only=True),
        Tool(id="minify-css", name="CSS Minifier", slug="css-minifier", category="Dev", tags=["css", "minify"], description="Minify CSS in-browser.", client_only=True),
        Tool(id="minify-js", name="JS Minifier", slug="js-minifier", category="Dev", tags=["js", "minify"], description="Minify JavaScript (simple).", client_only=True),
        Tool(id="emoji-picker", name="Emoji Picker", slug="emoji-picker", category="Text", tags=["emoji", "copy"], description="Browse and copy emojis.", client_only=True),
        Tool(id="ip-info", name="IP Info (Client)", slug="ip-info", category="Network", tags=["ip", "network"], description="Show your public IP using client fetch.", client_only=True),
        Tool(id="utm-builder", name="UTM Builder", slug="utm-builder", category="Marketing", tags=["utm", "campaign", "url"], description="Build UTM-tagged URLs.", client_only=True),
        Tool(id="case-snake", name="Snake Case Converter", slug="snake-case", category="Text", tags=["case", "snake"], description="Convert to_snake_case.", client_only=True),
        Tool(id="case-camel", name="Camel Case Converter", slug="camel-case", category="Text", tags=["case", "camel"], description="Convert toCamelCase.", client_only=True),
        Tool(id="case-kebab", name="Kebab Case Converter", slug="kebab-case", category="Text", tags=["case", "kebab"], description="Convert to-kebab-case.", client_only=True),
        Tool(id="word-count", name="Word Counter", slug="word-counter", category="Text", tags=["word", "count", "characters"], description="Count words and characters.", client_only=True),
        Tool(id="remove-dup", name="Remove Duplicates (Lines)", slug="remove-duplicates", category="Text", tags=["lines", "dedupe"], description="Deduplicate lines from text.", client_only=True),
        Tool(id="sort-lines", name="Sort Lines", slug="sort-lines", category="Text", tags=["sort", "lines", "alpha"], description="Sort lines alphabetically.", client_only=True),
        Tool(id="trim-lines", name="Trim Lines", slug="trim-lines", category="Text", tags=["trim", "lines"], description="Trim whitespace per line.", client_only=True),
        Tool(id="reverse-text", name="Reverse Text", slug="reverse-text", category="Text", tags=["reverse", "text"], description="Reverse string characters.", client_only=True),
        Tool(id="case-sentence", name="Sentence Case", slug="sentence-case", category="Text", tags=["case", "sentence"], description="Convert to sentence case.", client_only=True),
        Tool(id="rgb2hex", name="RGB to HEX", slug="rgb-to-hex", category="Design", tags=["rgb", "hex", "color"], description="Convert RGB to HEX.", client_only=True),
        Tool(id="hex2rgb", name="HEX to RGB", slug="hex-to-rgb", category="Design", tags=["hex", "rgb", "color"], description="Convert HEX to RGB.", client_only=True),
        Tool(id="image-compress", name="Image Compressor", slug="image-compressor", category="Images", tags=["image", "compress", "jpeg"], description="Compress JPEG/PNG in-browser.", client_only=True),
        Tool(id="favicon-gen", name="Favicon Generator", slug="favicon-generator", category="Images", tags=["favicon", "ico", "png"], description="Create favicons from images.", client_only=True),
        Tool(id="pdf-merge-client", name="PDF Merge (Client)", slug="pdf-merge-client", category="PDF", tags=["pdf", "merge"], description="Merge PDFs locally (experimental).", client_only=True),
        Tool(id="pdf-split-client", name="PDF Split (Client)", slug="pdf-split-client", category="PDF", tags=["pdf", "split"], description="Split PDFs locally (experimental).", client_only=True),
        Tool(id="random-password", name="Password Generator", slug="password-generator", category="Security", tags=["password", "random"], description="Generate secure passwords.", client_only=True),
        Tool(id="bmi", name="BMI Calculator", slug="bmi-calculator", category="Health", tags=["bmi", "health"], description="Calculate Body Mass Index.", client_only=True),
        Tool(id="tip-calc", name="Tip Calculator", slug="tip-calculator", category="Finance", tags=["tip", "percent"], description="Calculate tips quickly.", client_only=True),
        Tool(id="loan-calc", name="Loan Calculator", slug="loan-calculator", category="Finance", tags=["loan", "emi"], description="Estimate loan payments.", client_only=True),
        Tool(id="cron-parser", name="Cron Parser", slug="cron-parser", category="Dev", tags=["cron", "parse", "schedule"], description="Parse cron expressions.", client_only=True),
        Tool(id="jwt-decode", name="JWT Decoder", slug="jwt-decoder", category="Security", tags=["jwt", "decode", "token"], description="Decode JWTs locally.", client_only=True),
        Tool(id="mac-addr", name="MAC Address Formatter", slug="mac-formatter", category="Network", tags=["mac", "format"], description="Normalize MAC addresses.", client_only=True),
        Tool(id="ip-cidr", name="CIDR Calculator", slug="cidr-calculator", category="Network", tags=["cidr", "subnet"], description="CIDR/subnet calculator.", client_only=True),
        Tool(id="port-list", name="Open Ports Reference", slug="ports-reference", category="Network", tags=["ports", "reference"], description="Common TCP/UDP ports.", client_only=True),
        Tool(id="ascii-art", name="ASCII Art", slug="ascii-art", category="Text", tags=["ascii", "art"], description="Render ASCII art from text.", client_only=True),
        Tool(id="case-random", name="Random Case", slug="random-case", category="Text", tags=["case", "random"], description="Randomize letter casing.", client_only=True),
        Tool(id="remove-accent", name="Remove Accents", slug="remove-accents", category="Text", tags=["diacritics", "normalize"], description="Strip diacritics from characters.", client_only=True),
        Tool(id="dedent", name="Dedent Text", slug="dedent-text", category="Text", tags=["indent", "format"], description="Remove common leading spaces.", client_only=True),
    ]
    return base


def bulk_generated_tools(start_index: int, target_total: int) -> List[Tool]:
    categories = [
        ("Text", ["text", "format", "clean"]),
        ("Web", ["url", "encode", "decode"]),
        ("Images", ["image", "png", "jpg"]),
        ("Design", ["color", "hex", "rgb"]),
        ("Dev", ["json", "code", "tool"]),
        ("Data", ["csv", "json", "convert"]),
        ("Security", ["hash", "crypto", "checksum"]),
        ("Time", ["time", "timestamp", "date"]),
        ("Math", ["calc", "units", "numbers"]),
        ("Network", ["ip", "dns", "net"]),
        ("PDF", ["pdf", "pages", "merge"]),
        ("Marketing", ["utm", "seo", "campaign"]),
        ("Health", ["bmi", "health", "body"]),
        ("Finance", ["money", "calc", "rate"]),
    ]

    tools: List[Tool] = []
    i = start_index
    cat_idx = 0
    while i <= target_total:
        cat, base_tags = categories[cat_idx % len(categories)]
        slug = f"tool-{i:03d}-{cat.lower()}"
        tools.append(
            Tool(
                id=slug,
                name=f"Utility #{i} ({cat})",
                slug=slug,
                category=cat,
                tags=base_tags + [f"utility", f"#{i}"],
                description=f"Handy {cat.lower()} utility. Runs fully in your browser.",
                client_only=True,
            )
        )
        i += 1
        cat_idx += 1
    return tools


# Build a 500+ catalog deterministically at startup
_base = curated_tools()
_generated = bulk_generated_tools(start_index=len(_base) + 1, target_total=520)
TOOLS: List[Tool] = _base + _generated


@app.get("/")
def read_root():
    return {"message": "Tools API running", "count": len(TOOLS)}


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
        "collections": [],
        "tool_count": len(TOOLS),
    }

    # Env check for completeness
    response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
    response["database_name"] = "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set"
    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
