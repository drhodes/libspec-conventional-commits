'''
Feature Specification for Commit Header Structure
'''

from .err import Feat


class CommitHeader(Feat):
    '''
    The first line of a conventional commit message is the header.

    Structure:
      <type>[optional scope][optional !]: <description>

    Rules:
    - MUST start with a valid type (noun).
    - MAY include a scope enclosed in parentheses.
    - MAY include a '!' breaking change marker before the colon.
    - MUST include a terminal colon and space (': ').
    - MUST include a short description summary immediately following the colon and space.
    '''
