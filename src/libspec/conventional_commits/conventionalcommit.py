'''
Unified Conventional Commit Specification
'''

from .breaking_change_indicator import BreakingChangeIndicator
from .breaking_change_synonym import BreakingChangeSynonym
from .case_sensitivity import CaseSensitivity
from .colon_separator import ColonSeparator
from .commit_body import CommitBody
from .commit_description import CommitDescription
from .commit_footer import CommitFooter
from .commit_header import CommitHeader
from .commit_message_schema import (
    CommitMessageSchema,
    ConventionalCommitGrammar,
    FooterSchema,
)
from .footer_separator import FooterSeparator
from .footer_token import FooterToken
from .footer_value import FooterValue
from .malformed_commit import MalformedCommit
from .multiline_footer_boundary import MultilineFooterBoundary
from .revert_commit import RevertCommit
from .scope_context import ScopeContext
from .semver_mapping import SemVerMapping
from .type_prefix import TypePrefix


class ConvCommit(
    CommitHeader,
    TypePrefix,
    ScopeContext,
    ColonSeparator,
    CommitDescription,
    CommitBody,
    CommitFooter,
    FooterToken,
    FooterSeparator,
    FooterValue,
    BreakingChangeIndicator,
    BreakingChangeSynonym,
    SemVerMapping,
    CaseSensitivity,
    RevertCommit,
    MalformedCommit,
    MultilineFooterBoundary,
    CommitMessageSchema,
    FooterSchema,
    ConventionalCommitGrammar,
):
    '''
    Conventional Commits 1.0.0 Specification Composite

    This single specification encapsulates all features, requirements, data schemas,
    constraints, grammar definitions, and edge cases for the Conventional Commits v1.0.0 standard.

    Import this class into another project's spec module via:
        from spec.conventionalcommit import ConvCommit
    '''
