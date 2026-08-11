'''
Constraint Specification for Case Sensitivity
'''

from libspec import Constraint


class CaseSensitivity(Constraint):
    '''
    Case Sensitivity Rules for Conventional Commits Implementors:

    - The units of information that make up Conventional Commits MUST NOT be treated as case-sensitive by implementors (e.g., 'FEAT:', 'Feat:', 'feat:' should all be accepted).
    - EXCEPTION: 'BREAKING CHANGE' (and 'BREAKING-CHANGE') tokens in footers MUST be uppercase. Lowercase 'breaking change:' in a footer is NOT recognized as a breaking change token.
    '''

    def constraint_id(self):
        return "CASE_SENSITIVITY"

    def enforcement_logic(self):
        return "Parsers accept case-insensitive types/scopes, but strictly enforce uppercase 'BREAKING CHANGE' / 'BREAKING-CHANGE' tokens in footers."
