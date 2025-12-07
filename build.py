#!/usr/bin/env python3
"""
Build script for generating the academic website.
Merges data from data.json with template.html to produce index.html.
"""

import json
from jinja2 import Template
import markdown

def load_data(filepath='data.json'):
    """Load and return data from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please create a data.json file.")
        return None

def render_markdown(text):
    """Convert markdown text to HTML."""
    if text is None:
        return ""
    return markdown.markdown(text, extensions=['extra'])

def process_markdown_fields(data):
    """Process markdown in specific fields of the data."""
    # Process bio
    if 'basics' in data and 'bio' in data['basics']:
        data['basics']['bio'] = render_markdown(data['basics']['bio'])

    if 'basics' in data and 'short_bio' in data['basics']:
        data['basics']['short_bio'] = render_markdown(data['basics']['short_bio'])

    # Process news items
    if 'news' in data:
        for item in data['news']:
            if 'text' in item:
                item['text'] = render_markdown(item['text'])

    # Process project summaries
    if 'projects' in data:
        for project in data['projects']:
            if 'summary' in project:
                project['summary'] = render_markdown(project['summary'])

    # Process publication authors
    if 'publications' in data:
        for pub in data['publications']:
            if 'authors' in pub:
                pub['authors'] = render_markdown(pub['authors'])

    return data

def build_site():
    """Build the website by merging data with template."""
    # Load data
    data = load_data()
    if data is None:
        return False

    # Process markdown fields
    data = process_markdown_fields(data)

    # Load template
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print("Error: template.html not found.")
        return False

    # Create Jinja2 template and render
    template = Template(template_content)
    html_output = template.render(**data)

    # Write output
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)

    print("Successfully generated index.html")
    return True

if __name__ == '__main__':
    build_site()
