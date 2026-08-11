'''
Edge Case Specification for Revert Commits
'''

from libspec import EdgeCase


class RevertCommit(EdgeCase):
    '''
    Edge Case: Handling Revert Commits

    Conventional Commits does not mandate explicit revert behavior, leaving logic to tooling authors.

    Recommended Convention:
    - Use type 'revert' (e.g., 'revert: let us never again speak of the noodle incident').
    - Include a footer referencing the reverted commit SHAs (e.g., 'Refs: 676104e, a215868').
    '''

    def boundary_condition(self):
        return "A commit reverts one or more previously merged commits."

    def error_scenario(self):
        return "Determining whether reverting a feature or fix should trigger a major, minor, patch, or inverse version bump."
