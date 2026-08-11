'''
Data Schemas and Definitions for Conventional Commits 1.0.0
'''

from libspec import DataSchema, Def


class CommitMessageSchema(DataSchema):
    '''
    DATA-MODEL: CommitMessage
    FIELDS:
      type: str (e.g. feat, fix, docs, chore)
      scope: str | None (e.g. parser, api)
      is_breaking: bool (indicated by ! or BREAKING CHANGE footer)
      description: str (short summary of changes)
      body: str | None (optional long description)
      footers: list[FooterSchema] | None (optional key-value metadata trailers)
    '''

    type: str
    scope: str | None
    is_breaking: bool
    description: str
    body: str | None
    footers: list


class FooterSchema(DataSchema):
    '''
    DATA-MODEL: FooterTrailer
    FIELDS:
      token: str (e.g. BREAKING CHANGE, Signed-off-by, Refs)
      separator: str (': ' or ' #')
      value: str (trailer value, can span multiple lines)
    '''

    token: str
    separator: str
    value: str


class ConventionalCommitGrammar(Def):
    '''
    Grammar Specification for Conventional Commits 1.0.0:

    <commit-message> ::= <header> [ <blank-line> <body> ] [ <blank-line> <footers> ]
    <header>         ::= <type> [ "(" <scope> ")" ] [ "!" ] ": " <description>
    <type>           ::= [a-zA-Z0-9_-]+
    <scope>          ::= [a-zA-Z0-9_/-]+
    <description>    ::= [^\r\n]+
    <body>           ::= <paragraph> ( <blank-line> <paragraph> )*
    <footers>        ::= <footer-entry> ( <newline> <footer-entry> )*
    <footer-entry>   ::= <footer-token> <separator> <footer-value>
    <footer-token>   ::= "BREAKING CHANGE" | "BREAKING-CHANGE" | [a-zA-Z0-9_-]+
    <separator>      ::= ": " | " #"
    '''
