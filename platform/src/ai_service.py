import json
from openai import OpenAI
from fastapi import HTTPException
from src.models import BenchmarkCard
import config


client = OpenAI(api_key=config.OPENAI_API_KEY)


def process_pdf_text(text: str, model: str = "gpt-4o-mini") -> dict:
    schema = BenchmarkCard.model_json_schema()
    
    prompt = f"""
    Please analyze the following document and extract key information to create a structured output.
    Be precise and factual - only include information clearly stated in the text.
    For any information not available in the document, use "N/A".
    You may return lists for fields that have multiple items.
    Do NOT make assumptions or guesses.
    
    Return your response as a valid JSON object with the following structure:
    
    {schema}

    Remember:
    1. Only include information directly stated in the paper
    2. Use "N/A" or empty lists rather than making assumptions
    3. Keep the structure exact - don't add or remove fields
    4. Format as valid JSON
    
    Document content:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a specialized data extraction assistant focused on documents. Your task is to extract only factual, explicitly stated information and organize it according to a specific schema."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        result_json = json.loads(response.choices[0].message.content)
        return result_json
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing with AI: {str(e)}")