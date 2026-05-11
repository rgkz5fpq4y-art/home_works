import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    cleaned_text = re.sub(r'<[^>]+>', '', html)
    lines = cleaned_text.splitlines()
    filtred_lines = [line.strip() for line in lines if line.strip()]
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(filtred_lines))
delete_html_tags('draft.html')

