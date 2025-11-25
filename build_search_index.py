import os
import json
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def extract_search_fields(card_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extracts relevant fields for search indexing."""
    details = card_data.get("benchmark_details", {})
    purpose = card_data.get("purpose_and_intended_users", {})
    risks = card_data.get("targeted_risks", {})
    
    return {
        "name": details.get("name", "Unknown"),
        "overview": details.get("overview", ""),
        "domains": details.get("domains", []),
        "languages": details.get("languages", []),
        "tasks": purpose.get("tasks", []),
        "risk_categories": risks.get("risk_categories", []),
        # Store a simplified version for display/filtering
        "id": details.get("name", "Unknown").lower().replace(" ", "-") # Simple ID generation
    }

def build_index(json_dir: Path, output_file: Path):
    logger.info(f"Scanning {json_dir} for JSON benchmark cards...")
    
    index_data = []
    json_files = list(json_dir.glob("*.json"))
    
    if not json_files:
        logger.warning(f"No JSON files found in {json_dir}")
        return

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            search_entry = extract_search_fields(data)
            # Add the filename as a reference
            search_entry["filename"] = json_file.name
            
            index_data.append(search_entry)
            logger.debug(f"Indexed {json_file.name}")
            
        except Exception as e:
            logger.error(f"Error processing {json_file.name}: {e}")

    logger.info(f"Indexed {len(index_data)} cards.")
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2)
    
    logger.info(f"Search index saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Build a search index from JSON benchmark cards.")
    parser.add_argument("json_dir", help="Directory containing JSON benchmark card files")
    parser.add_argument("--output", default="platform/static/search_index.json", help="Output path for search index JSON (default: platform/static/search_index.json)")
    
    args = parser.parse_args()
    
    json_path = Path(args.json_dir)
    output_path = Path(args.output)
    
    if not json_path.exists():
        logger.error(f"JSON directory {json_path} does not exist.")
        return

    build_index(json_path, output_path)

if __name__ == "__main__":
    main()
