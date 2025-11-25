import os
import tempfile
import json # Import json for returning dict
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import Dict, Any # Import typing hints

import config
from src.pdf_extractor import extract_text_from_pdf
from src.ai_service import process_pdf_text
from src.templates import HTML_TEMPLATE
from src.markdown_converter import convert_json_to_markdown # Import the converter


app = FastAPI(title="PDF Extractor")
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_form():
    return HTML_TEMPLATE


@app.get("/search", response_class=HTMLResponse)
async def search_page():
    search_path = os.path.join(config.STATIC_DIR, "search.html")
    if os.path.exists(search_path):
        with open(search_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Search page not found", 404


@app.post("/extract/")
async def extract_pdf(
    file: UploadFile = File(...), 
    model: str = Form("gpt-4o-mini"),
    api_key: str = Form(None)
) -> Dict[str, Any]: # Update return type hint
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Uploaded file must be a PDF")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name
    
    try:
        pdf_text = extract_text_from_pdf(temp_file_path)
        
        if not pdf_text:
            raise HTTPException(status_code=400, detail="Could not extract text from the PDF")
        
        # Process with AI to get JSON object
        json_result = process_pdf_text(pdf_text, model, api_key)
        
        # Convert JSON object to Markdown string
        markdown_result = convert_json_to_markdown(json_result)

        # Return both results
        return {
            "json_result": json_result, 
            "md_result": markdown_result
        }
    
    finally:
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)


@app.get("/view", response_class=HTMLResponse)
async def view_page():
    view_path = os.path.join(config.STATIC_DIR, "view.html")
    if os.path.exists(view_path):
        with open(view_path, "r", encoding="utf-8") as f:
            return f.read()
    return "View page not found", 404


# Path to the JSON directory (relative to platform/)
JSON_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'BenchmarkCards_JSON')

@app.get("/api/card/{filename}")
async def get_card_json(filename: str):
    if ".." in filename or "/" in filename or "\\" in filename:
         raise HTTPException(status_code=400, detail="Invalid filename")
    
    file_path = os.path.join(JSON_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Card not found")
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/card/{filename}/markdown")
async def get_card_markdown(filename: str):
    if ".." in filename or "/" in filename or "\\" in filename:
         raise HTTPException(status_code=400, detail="Invalid filename")
    
    file_path = os.path.join(JSON_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Card not found")
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        md_content = convert_json_to_markdown(json_data)
        return {"content": md_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
