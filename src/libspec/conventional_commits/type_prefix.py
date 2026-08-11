'''
Specification for Commit Type Prefix
'''

from libspec import Requirement


class TypePrefix(Requirement):
    '''
    Commits MUST be prefixed with a type, which consists of a noun (e.g., feat, fix).

    - The type 'feat' MUST be used when a commit adds a new feature to the codebase (SemVer MINOR).
    - The type 'fix' MUST be used when a commit represents a bug fix for the codebase (SemVer PATCH).
    - Types other than 'feat' and 'fix' MAY be used (e.g., docs, chore, style, refactor, perf, test, ci, build).
    - Additional types have no implicit effect on Semantic Versioning unless a breaking change is included.
    '''
