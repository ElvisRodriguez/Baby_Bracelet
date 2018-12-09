'''
Helper method to convert markdown file into a parsable string for Dash module.
'''

import os

def stringify_file(file_path='assets/template.md'):
    '''Opens a markdown file and converts it into a string.

    Args:
        file_path: string representing path to markdown file.
    Exceptions Raised:
        None.
    Returns:
        String of markdown file data.
    '''
    md_file = []
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            md_file.extend(file.readlines())
        md_file = ''.join(md_file)
        return md_file
    return ''
