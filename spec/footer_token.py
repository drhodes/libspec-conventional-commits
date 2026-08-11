'''
Specification for Footer Token
'''

from .err import Req


class FooterToken(Req):
    '''
    A footer's token MUST identify the metadata trailer type.

    - Tokens MUST use '-' in place of whitespace characters (e.g., 'Reviewed-by', 'Signed-off-by', 'Refs').
    - Using '-' for spaces helps differentiate footer tokens from standard body paragraphs.
    - An exception is made for 'BREAKING CHANGE', which MAY be used as a token containing a space.
    - 'BREAKING-CHANGE' is also allowed and synonymous with 'BREAKING CHANGE'.
    '''
