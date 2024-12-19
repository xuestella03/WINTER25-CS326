import requests
import os

def main():
    os.chdir(os.environ['GITHUB_WORKSPACE'])

    direct_download_link = requests.get("https://script.google.com/macros/s/AKfycbw9_jMc5xNXhbqdaWWTxtGj95T_MFYOP019lbJl3Rfqzu8V1YMen-qXe6vB9coJSdpx/exec")
    response = requests.get(direct_download_link.content.decode())
    questions = response.json()

    TEMPLATE = """<div style="height: 100%; width: 100%;"><iframe src="{FORM_URL}?embedded=true" width="80%" height="100%" frameborder="0" marginheight="0" marginwidth="0" style="margin-left: 10%; margin-right: 10%;">Loading…</iframe></div>"""

    # Loop through questions
    for question in questions:
        markdown = question['slides']
        key = question['key']
        markdown_path = os.path.join('lectures/', markdown)  # Adjust the path as needed

        # Check if markdown file exists
        if not os.path.exists(markdown_path):
            print(f'Markdown "{markdown}" not found')
            continue

        # Read markdown line by line
        with open(markdown_path, 'r') as f:
            lines = f.readlines()

        # Find line number of question
        line = None
        for i, l in enumerate(lines):
            if key in l:
                line = i

                # clear all lines until next <!--s--> tag.
                while i + 1 < len(lines) and lines[i+1].strip() != '<!--s-->':
                    lines.pop(i+1)

                break

        if line is None:
            print(f'Question "{key}" not found in markdown "{markdown}"')
            continue

        # Insert question after line number.
        lines.insert(line+1, TEMPLATE.format(FORM_URL=question['formURL']))

        # Save the new markdown with inserted line.
        with open(markdown_path, 'w') as f:
            f.writelines(lines)

if __name__ == '__main__':
    main()
    print("Questions added successfully")