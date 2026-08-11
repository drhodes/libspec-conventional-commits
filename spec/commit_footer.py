'''
Feature Specification for Commit Footers Section
'''

from .err import Feat


class CommitFooter(Feat):
    '''
    One or more footers MAY be provided at the bottom of a conventional commit message.

    - Footers MUST begin one blank line after the commit body (or one blank line after description if no body is present).
    - Each footer entry follows a format inspired by the git trailer convention.
    - Providing footers is OPTIONAL, unless a breaking change is communicated exclusively via footer ('BREAKING CHANGE:').
    '''
