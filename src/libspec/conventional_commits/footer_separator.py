'''
Specification for Footer Separator
'''

from libspec import Requirement


class FooterSeparator(Requirement):
    '''
    A footer entry MUST use a valid token-value separator.

    - Allowed separators are either:
      1. ':<space>' (colon followed by space, e.g., 'Reviewed-by: Z', 'BREAKING CHANGE: change API')
      2. '<space>#' (space followed by hash/pound symbol, e.g., 'Refs #123', 'Closes #456')
    '''
