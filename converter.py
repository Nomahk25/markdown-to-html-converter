import sys
import os

def md_to_html_line(line):
    line = line.strip()
   
    if line.startswith('### '):
        return '<h3>' + line[4:] + '</h3>'
    elif line.startswith('## '):
        return '<h2>' + line[3:] + '</h2>'
    elif line.startswith('# '):
        return '<h1>' + line[2:] + '</h1>'
    
    line = line.replace('**', '<b>').replace('**', '</b>')  # simplified
   
    line = line.replace('*', '<i>').replace('*', '</i>')    # simplified
    
    if line.startswith('- '):
        return '<li>' + line[2:] + '</li>'
   
    if line:
        return '<p>' + line + '</p>'
    return ''

def md_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    html_lines = ['<html>', '<body>']
    in_list = False

    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(md_to_html_line(line))
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(md_to_html_line(line))

    if in_list:
        html_lines.append('</ul>')

    html_lines.extend(['</body>', '</html>'])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_lines))

    print(f'Converted {input_file} to {output_file}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py input.md output.html")
    else:
        md_to_html(sys.argv[1], sys.argv[2])
