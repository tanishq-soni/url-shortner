"""URL Shortener Hack"""
import json
import os
import shutil


def main():
    """Main Function"""
    html = "<html><script>window.location.replace('{url}');</script></html>"

    with open('links.json') as f:
        links = json.load(f)

    shutil.rmtree('dist', ignore_errors=True)
    os.mkdir('dist')

    with open('dist/CNAME', 'w') as f:
        f.write('tanishq-soni.github.io/url-shortner')

    for link in links:
        html_document = html.format(url=link['url'])
        file_path = f"dist/{link['name']}.html"

        with open(file_path, 'w') as f:
            f.write(html_document)


if __name__ == "__main__":
    main()
