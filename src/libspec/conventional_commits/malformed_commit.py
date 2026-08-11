'''
Edge Case Specification for Malformed Commit Messages
'''

from libspec import EdgeCase


class MalformedCommit(EdgeCase):
    '''
    Edge Case: Handling Malformed or Non-Conforming Commits

    What happens when a commit message does not conform to Conventional Commits specification (e.g. missing colon space, unknown format)?
    '''

    def boundary_condition(self):
        return "Commit message lacks required type prefix, space after colon, or valid header structure."

    def error_scenario(self):
        return "Automated changelog generation and SemVer calculation tools will ignore non-conforming commits during release processing."
