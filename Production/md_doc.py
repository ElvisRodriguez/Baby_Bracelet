'''
Helper method to convert markdown file into a str parsable by
dash_core_components
'''

def markdown():
    '''
        Description:
            Opens a markdown file and converts it into a string.
        Args:
            None.
        Exceptions Raised:
            None.
        Returns:
            String representation of markdown file.
    '''
    md_file = []
    with open('assets/template.md', 'r') as file:
        md_file.extend(file.readlines())
    md_file = ''.join(md_file)
    return md_file
