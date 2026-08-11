'''
Edge Case Specification for Multi-Paragraph Body vs Footer Boundaries
'''

from libspec import EdgeCase


class MultilineFooterBoundary(EdgeCase):
    '''
    Edge Case: Disambiguating Multi-Paragraph Bodies from Footers

    What happens when a commit message has multiple paragraphs and trailer-like tokens?
    '''

    def boundary_condition(self):
        return "A multi-paragraph commit body contains lines formatted with words followed by colons."

    def error_scenario(self):
        return "Parser must distinguish body text from footers by checking if token uses hyphenation (or uppercase BREAKING CHANGE) and valid separator (': ' or ' #') following a blank line."
