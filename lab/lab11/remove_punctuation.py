#!/usr/bin/env python3

import string

### helper function: no need to understand; read at your peril
def removePunctuation (s):

    """Remove punctuation from a string.

    https://docs.python.org/3/library/stdtypes.html#str.translate
    https://docs.python.org/3/library/stdtypes.html#str.maketrans

    Params: s (str)
    Returns: (str) s with all punctuation removed
    """
    
    return s.translate (str.maketrans ({c:None for c in string.punctuation}))

