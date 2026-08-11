'''
Specification for Footer Value Parsing and Termination
'''

from libspec import Requirement


class FooterValue(Requirement):
    '''
    A footer's value follows the token and separator.

    - A footer value MAY contain spaces and newlines (multi-line footer values).
    - Parsing of a footer value MUST terminate when the next valid footer token/separator pair is observed.
    '''
