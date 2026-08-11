'''
Constraint Specification for BREAKING-CHANGE Synonym
'''

from libspec import Constraint


class BreakingChangeSynonym(Constraint):
    '''
    BREAKING-CHANGE MUST be synonymous with BREAKING CHANGE when used as a token in a footer.

    Parsers and tooling MUST treat 'BREAKING-CHANGE: <description>' identically to 'BREAKING CHANGE: <description>'.
    '''

    def constraint_id(self):
        return "BREAKING_CHANGE_SYNONYM"

    def enforcement_logic(self):
        return "Commit message parsers must normalize 'BREAKING-CHANGE' token to 'BREAKING CHANGE' during AST generation."
