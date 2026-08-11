'''
Feature Specification for Semantic Versioning (SemVer) Mapping
'''

from .err import Feat


class SemVerMapping(Feat):
    '''
    Conventional Commits dovetail with Semantic Versioning (SemVer v2.0.0).

    1. PATCH Release:
       - Triggered by commits of type 'fix'.
       - Represents a bug fix in the codebase.

    2. MINOR Release:
       - Triggered by commits of type 'feat'.
       - Represents a new backward-compatible feature added to the codebase.

    3. MAJOR Release:
       - Triggered by any commit containing a breaking change (indicated by '!' in prefix or 'BREAKING CHANGE:' footer).
       - Applies regardless of the commit type (e.g., 'feat!:', 'fix!:', 'chore!:').

    4. Other Types:
       - Types other than 'fix' and 'feat' (e.g. 'docs', 'style', 'refactor', 'test', 'chore') have no implicit version bump impact, unless they include a breaking change.
    '''
