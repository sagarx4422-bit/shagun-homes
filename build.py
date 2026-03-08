import os

base_dir = r"C:\Users\Sagar\Downloads\shagun homes"

def read(filename):
    path = os.path.join(base_dir, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def write(filename, content):
    path = os.path.join(base_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

css = read('_shared_css.html')
nav = read('_shared_nav.html')
footer = read('_shared_footer.html')
js = read('_shared_js.html')

def build_page(page_files, output_filename, title, description, body_class=""):
    meta = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="Shagun Homes">
<meta property="og:type" content="website">
<link rel="icon" href="logo.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
{css}
</head>
<body class="{body_class}">
{nav}
"""
    body = ""
    for pf in page_files:
        body += read(pf)
    
    end = f"""
{footer}
{js}
</body>
</html>"""

    write(output_filename, meta + body + end)
    print(f"Built {output_filename}")

# Build Index
build_page(['_page_index_1.html', '_page_index_2.html'], 'index.html', 
    'Home — Shagun Homes', 
    'Find premium 1 BHK & 2 BHK flats in Kalyan East and Dombivali. Legally verified. Free consultation with Ajay Patil.',
    body_class="transparent-nav")

# Build Properties
build_page(['_page_properties.html'], 'properties.html',
    'All Properties — Shagun Homes',
    'Explore our curated list of 1 BHK & 2 BHK properties in Kalyan East, Kalyan West, and Dombivali.')

# Build Single Property
build_page(['_page_property.html'], 'property.html',
    'Luxuria Heights — Shagun Homes | 1 & 2 BHK Flats',
    'Explore Luxuria Heights in Kalyan East. View premium 1 & 2 BHK flats with legal certification, pricing, and floor plans.')

# Build About Us
build_page(['_page_about.html'], 'about.html',
    'About Us — Shagun Homes | Ajay Patil Property Consultant',
    'Learn about Shagun Homes and Ajay Patil, your trusted property consultant in Kalyan with over 12 years of experience.')

# Build Contact Us
build_page(['_page_contact.html'], 'contact.html',
    'Contact Us — Shagun Homes | Free Site Visit',
    'Get in touch with Ajay Patil to book a free site visit or consultation for properties in Kalyan and Dombivali.')
