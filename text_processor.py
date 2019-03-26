import re


def get_paragraph_from_file(file_path=None):
    """
    params: file_path(string) A valid location of file
    return: The whole file in string format
    """
    if not file_path:
        file_path = 'paragraph.txt'
    paragraph = ''
    # Opeing paragraph.txt file and read the whole file
    with open(file_path, 'r') as text_file:
        # String into variable paragraph
        paragraph = text_file.read().replace('\n', '')
    return paragraph


def remove_special_char(text):
    """
    params: text(str) A string text
    return: A stripped string after removing special character
    """
    # Replace special character
    stripped = re.sub('[^\w\s]', ' ', text)
    stripped = re.sub('_', ' ', stripped)

    # Change white space(tab) into one space
    stripped = re.sub('\s+', ' ', stripped)
    stripped = stripped.strip()
    return stripped

def make_list_of_lower_word(paragraph):
    """
    params: paragraph (string) A simple string after process
    return: A List for further process 
    """
    return [p.lower() for p in paragraph.split()]

