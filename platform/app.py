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


@app.post("/extract/")
async def extract_pdf(file: UploadFile = File(...), model: str = Form("gpt-4o-mini")) -> Dict[str, Any]: # Update return type hint
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
        json_result = process_pdf_text(pdf_text, model)
        
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
