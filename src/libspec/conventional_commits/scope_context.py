'''
Specification for Commit Scope Context
'''

from libspec import Requirement


class ScopeContext(Requirement):
    '''
    A scope MAY be provided after a commit type to give contextual information.

    - A scope MUST consist of a noun describing a section of the codebase.
    - The scope MUST be surrounded by parenthesis immediately after the type, e.g., feat(parser): or fix(api):.
    - Providing a scope is OPTIONAL.
    '''
