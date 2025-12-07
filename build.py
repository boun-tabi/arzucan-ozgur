import json
import markdown
from jinja2 import Template

def build():
    try:
        # 1. Load Data
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: data.json not found.")
        return

    # 2. Helper function to render markdown safely
    def md_filter(text):
        if not text: return ""
        return markdown.markdown(text)

    # 3. Process fields only if they exist
    if 'basics' in data and 'bio' in data['basics']:
        data['basics']['bio'] = md_filter(data['basics']['bio'])
    
    # Safely iterate over lists only if they exist
    if 'news' in data and isinstance(data['news'], list):
        for item in data['news']:
            if 'text' in item:
                item['text'] = md_filter(item['text'])

    if 'projects' in data and isinstance(data['projects'], list):
        for proj in data['projects']:
            if 'summary' in proj:
                proj['summary'] = md_filter(proj['summary'])

    if 'publications' in data and isinstance(data['publications'], list):
        for pub in data['publications']:
            if 'authors' in pub:
                pub['authors'] = md_filter(pub['authors'])

    # 4. Load Template
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print("❌ Error: template.html not found.")
        return

    # 5. Render
    template = Template(template_content)
    # Jinja2 treats missing variables as "undefined" (False in if-statements) by default
    output_html = template.render(**data)

    # 6. Save
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output_html)
    
    print("✅ Academic Website generated successfully!")

if __name__ == "__main__":
    build()
