import json
from typing import Any, Dict, List, Optional, Union
import re

def safe_get(obj: Any, *keys: Union[str, int], default: Any = None) -> Any:
    """Safely navigate nested dictionaries/lists."""
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int) and 0 <= key < len(current):
            current = current[key]
        else:
            return default
    return current

def format_item_markdown(data: Any, depth: int = 0) -> str:
    """Recursively formats a dictionary or list into Markdown list items."""
    md = ''
    indent = '  ' * depth

    if isinstance(data, dict):
        for key, value in data.items():
            formatted_key = key.replace('_', ' ').title()
            # Check for None, N/A, empty string
            if value is None or value == 'N/A' or (isinstance(value, str) and not value.strip()):
                 md += f"{indent}- **{formatted_key}**: Not Applicable\n"
            elif isinstance(value, (dict, list)):
                 # If value is a complex type, start a new list item for the key
                 md += f"{indent}- **{formatted_key}**:\n"
                 md += format_item_markdown(value, depth + 1) # Recurse for the complex value
            else:
                 # Simple value on the same line as the key
                 md += f"{indent}- **{formatted_key}**: {value}\n"

    elif isinstance(data, list):
        if not data:
             # This case should ideally be handled by the caller for the key-list pair
             # but as a fallback for lists directly passed, treat as empty
             md += f"{indent}- Not Applicable\n"
        else:
            for item in data:
                if isinstance(item, (dict, list)):
                    # If item is complex, start a new list item marker and recurse
                    md += f"{indent}- \n" # Add a list item marker
                    md += format_item_markdown(item, depth + 1) # Recurse for the complex item
                else:
                    # Simple list item
                    md += f"{indent}- {item}\n"

    return md

def convert_json_to_markdown(json_data: Dict[str, Any]) -> str:
    """
    Converts the BenchmarkCard JSON structure into a Markdown string suitable for rendering.
    Assumes the input is already a Python dictionary matching the schema.
    """
    if not json_data:
        return "# Error: No data provided\n"

    md_lines = []

    title = safe_get(json_data, "benchmark_details", "name", default="Benchmark Card")
    md_lines.append(f"# {title}")
    md_lines.append("") # Blank line

    sections_order = [
        "benchmark_details",
        "purpose_and_intended_users",
        "data",
        "methodology",
        "targeted_risks",
        "ethical_and_legal_considerations",
    ]

    section_titles = {
        "benchmark_details": "📊 Benchmark Details",
        "purpose_and_intended_users": "🎯 Purpose and Intended Users",
        "data": "💾 Data",
        "methodology": "🔬 Methodology",
        "targeted_risks": "⚠️ Targeted Risks",
        "ethical_and_legal_considerations": "🔒 Ethical and Legal Considerations",
    }

    for section_key in sections_order:
        if section_key in json_data and json_data[section_key]:
            md_lines.append(f"## {section_titles[section_key]}")
            md_lines.append("") # Blank line

            section_data = json_data[section_key]

            # Use the recursive formatter for the contents of each section
            md_lines.append(format_item_markdown(section_data, 0).strip())
            md_lines.append("") 

    cleaned_lines = []
    last_line_blank = True 
    for line in md_lines:
        is_current_line_blank = not line.strip()
        if is_current_line_blank and last_line_blank:
            continue 
        cleaned_lines.append(line)
        last_line_blank = is_current_line_blank

    return "\n".join(cleaned_lines).strip()

