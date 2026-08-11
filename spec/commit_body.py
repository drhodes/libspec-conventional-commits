'''
Feature Specification for Commit Body
'''

from .err import Feat


class CommitBody(Feat):
    '''
    An optional commit body provides detailed contextual information about the code changes.

    - The body MUST begin exactly one blank line after the short description header.
    - The body is free-form and MAY consist of any number of newline-separated paragraphs.
    - Providing a commit body is OPTIONAL.
    '''
