'''
Specification for Commit Description
'''

from .err import Req


class CommitDescription(Req):
    '''
    A short description MUST immediately follow the colon and space after the type/scope prefix.

    - The description is a short summary of the code changes made in the commit.
    - Example: 'fix: array parsing issue when multiple spaces were contained in string'
    - The description MUST NOT be empty.
    '''
