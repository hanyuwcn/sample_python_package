from content import generate_content

def write_to_dict(content):
    dict = {}
    dict[content] = generate_content(content)

    return dict