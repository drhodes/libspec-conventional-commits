'''
Specification for Footer Value Parsing and Termination
'''

from .err import Req


class FooterValue(Req):
    '''
    A footer's value follows the token and separator.

    - A footer value MAY contain spaces and newlines (multi-line footer values).
    - Parsing of a footer value MUST terminate when the next valid footer token/separator pair is observed.
    '''
