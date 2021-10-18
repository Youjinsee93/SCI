import markdown


def markdown_to_html(md_text):
    html = markdown.markdown(md_text)
    return html
