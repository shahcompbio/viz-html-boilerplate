import os
import errno

def merge_files():
    with open(os.path.join("build", "index.html"),"r") as file:
        html = file.read()

    js_txt = open(os.path.join("build", "static/js/main.js"), 'r').read()
    css_txt = open(os.path.join("build", "static/css/main.css"), 'r').read()

    ## Not sure why but new version was complaining if the JS script wasn't at the bottom of the page
    html = html.replace('<script defer="defer" src="/static/js/main.js"></script>', "")
    html = html.replace('</body>', f"<script>{js_txt}</script></body>")
    html = html.replace('<link href="/static/css/main.css" rel="stylesheet">', f"<style>{css_txt}</style>")

    output_filename = os.path.join("dist", 'template.html')
    if not os.path.exists(os.path.dirname(output_filename)):
        try:
            os.makedirs(os.path.dirname(output_filename))
        except OSError as exc: 
            if exc.errno != errno.EEXIST:
                raise
    with open(output_filename, 'w') as output_file:
        output_file.write(html)

merge_files()