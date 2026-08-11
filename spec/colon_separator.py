'''
Specification for Terminal Colon and Space Separator
'''

from .err import Req


class ColonSeparator(Req):
    '''
    A terminal colon followed immediately by a space (': ') is REQUIRED after the type/scope prefix.

    - Format: '<type>[optional scope][optional !]: '
    - The space after the colon is MANDATORY before the description text begins.
    - Example valid: 'feat: add feature'
    - Example invalid: 'feat:add feature' (missing space after colon)
    '''
