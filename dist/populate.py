import argparse
from jinja2 import Template
import json

def populate_html(dashboard_id, name):
    app_args = {
        "text": "Hello " + name
    }

    app_json = json.dumps(app_args, indent=4)

    with open("template.html","r") as file:
        template = Template(file.read())

    html = template.render(data=app_json, dashboard="Test", dashboard_id=dashboard_id)

    with open(f"{dashboard_id}.html", 'w') as output_file:
        output_file.write(html)


parser = argparse.ArgumentParser(description='Output HTML with name')
parser.add_argument('dashboard_id', type=str)
parser.add_argument('name', type=str)

args = parser.parse_args()

populate_html(args.dashboard_id, args.name)