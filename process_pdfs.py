import os
import sys
import argparse
import json
import logging
from pathlib import Path

# Setup paths to import from platform/src
current_dir = os.path.dirname(os.path.abspath(__file__))
platform_dir = os.path.join(current_dir, 'platform')
sys.path.append(platform_dir)

try:
    import config
    from src.pdf_extractor import extract_text_from_pdf
    from src.ai_service import process_pdf_text
    from src.markdown_converter import convert_json_to_markdown
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure you are running this script from the root of the BenchmarkCards-main directory.")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def validate_api_key():
    if config.OPENAI_API_KEY == "your_openai_api_key_here":
        # Try to get from environment variable
        env_key = os.environ.get("OPENAI_API_KEY")
        if env_key:
            config.OPENAI_API_KEY = env_key
            logger.info("Using OpenAI API key from environment variable.")
        else:
            logger.warning("OpenAI API key is set to default placeholder in config.py and not found in environment.")
            logger.warning("AI processing will likely fail. Please update platform/config.py or set OPENAI_API_KEY env var.")

def process_single_pdf(pdf_path: Path, output_dir: Path, model: str):
    logger.info(f"Processing {pdf_path.name}...")
    
    try:
        # 1. Extract text
        text = extract_text_from_pdf(str(pdf_path))
        if not text.strip():
            logger.warning(f"No text extracted from {pdf_path.name}. Skipping.")
            return

        # 2. Process with AI
        logger.info(f"Extracting structured data using {model}...")
        card_data = process_pdf_text(text, model=model)
        
        # 3. Save JSON
        json_filename = pdf_path.stem + ".json"
        json_path = output_dir / "json" / json_filename
        json_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(card_data, f, indent=2)
        logger.info(f"Saved JSON to {json_path}")

        # 4. Convert to Markdown
        md_content = convert_json_to_markdown(card_data)
        
        # 5. Save Markdown
        md_filename = pdf_path.stem + ".md"
        md_path = output_dir / "markdown" / md_filename
        md_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        logger.info(f"Saved Markdown to {md_path}")
        
    except Exception as e:
        logger.error(f"Failed to process {pdf_path.name}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Process PDF benchmark papers into JSON and Markdown cards.")
    parser.add_argument("input_dir", help="Directory containing PDF files")
    parser.add_argument("--output_dir", default="output", help="Directory to save output (default: output)")
    parser.add_argument("--model", default="gpt-4o-mini", help="OpenAI model to use (default: gpt-4o-mini)")
    
    args = parser.parse_args()
    
    input_path = Path(args.input_dir)
    output_path = Path(args.output_dir)
    
    if not input_path.exists():
        logger.error(f"Input directory {input_path} does not exist.")
        sys.exit(1)
        
    validate_api_key()
    
    pdf_files = list(input_path.glob("*.pdf"))
    if not pdf_files:
        logger.warning(f"No PDF files found in {input_path}")
        return

    logger.info(f"Found {len(pdf_files)} PDF files to process.")
    
    for pdf_file in pdf_files:
        process_single_pdf(pdf_file, output_path, args.model)
        
    logger.info("Batch processing complete.")

if __name__ == "__main__":
    main()
