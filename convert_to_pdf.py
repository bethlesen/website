#!/usr/bin/env python3
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# Read the markdown file
with open('/home/user/website/website-specification.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
md = markdown.Markdown(extensions=['extra', 'toc', 'tables'])
html_content = md.convert(md_content)

# Create a complete HTML document with styling
html_doc = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Website Specification Document</title>
    <style>
        @page {{
            size: Letter;
            margin: 0.75in;
            @bottom-right {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 9pt;
                color: #666;
            }}
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{
            font-size: 24pt;
            margin-top: 24pt;
            margin-bottom: 12pt;
            page-break-after: avoid;
            color: #1a1a1a;
            border-bottom: 2px solid #333;
            padding-bottom: 6pt;
        }}
        h2 {{
            font-size: 18pt;
            margin-top: 18pt;
            margin-bottom: 10pt;
            page-break-after: avoid;
            color: #1a1a1a;
            border-bottom: 1px solid #666;
            padding-bottom: 4pt;
        }}
        h3 {{
            font-size: 14pt;
            margin-top: 14pt;
            margin-bottom: 8pt;
            page-break-after: avoid;
            color: #2a2a2a;
        }}
        h4 {{
            font-size: 12pt;
            margin-top: 12pt;
            margin-bottom: 6pt;
            page-break-after: avoid;
            color: #2a2a2a;
        }}
        p {{
            margin-bottom: 10pt;
            text-align: justify;
        }}
        ul, ol {{
            margin-bottom: 10pt;
            padding-left: 24pt;
        }}
        li {{
            margin-bottom: 4pt;
        }}
        code {{
            background-color: #f5f5f5;
            padding: 2pt 4pt;
            font-family: "Courier New", monospace;
            font-size: 10pt;
            border-radius: 2pt;
        }}
        pre {{
            background-color: #f5f5f5;
            padding: 10pt;
            border-left: 3pt solid #ccc;
            overflow-x: auto;
            margin-bottom: 10pt;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 10pt;
        }}
        th, td {{
            border: 1pt solid #ddd;
            padding: 6pt;
            text-align: left;
        }}
        th {{
            background-color: #f5f5f5;
            font-weight: bold;
        }}
        blockquote {{
            border-left: 3pt solid #ccc;
            margin-left: 0;
            padding-left: 12pt;
            color: #666;
            font-style: italic;
        }}
        hr {{
            border: none;
            border-top: 1pt solid #ccc;
            margin: 18pt 0;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        strong {{
            font-weight: bold;
        }}
        em {{
            font-style: italic;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Convert HTML to PDF
font_config = FontConfiguration()
html = HTML(string=html_doc, base_url='/home/user/website/')
html.write_pdf('/home/user/website/website-specification.pdf', font_config=font_config)

print("PDF generated successfully: /home/user/website/website-specification.pdf")
