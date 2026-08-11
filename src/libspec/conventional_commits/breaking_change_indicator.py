'''
Specification for Breaking Change Indication
'''

from libspec import Requirement


class BreakingChangeIndicator(Requirement):
    '''
    Breaking changes MUST be indicated in the type/scope prefix of a commit, or as an entry in the footer.

    1. Prefix Indication:
       - Breaking changes MAY be indicated by appending a '!' immediately before the terminal colon (and after optional scope).
       - Examples: 'feat!:', 'feat(api)!:'.
       - If '!' is used, 'BREAKING CHANGE:' MAY be omitted from the footer, and the commit description SHALL describe the breaking change.

    2. Footer Indication:
       - Breaking changes MAY be included as a footer consisting of uppercase 'BREAKING CHANGE', followed by a colon, space, and description.
       - Example: 'BREAKING CHANGE: extends key in config file is now used for extending other configs'.

    3. Combined Indication:
       - A commit MAY use both '!' in the prefix and a 'BREAKING CHANGE:' footer simultaneously.
    '''
