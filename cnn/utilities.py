'''
sequences.py -- utilities for sequences [WIP]
'''
def normalize_sos(sq, sz=30, filler=0):
    '''
    Take a list of lists and ensure that they are all of length `sz`

    Args:
    -----

        e: a non-generator iterable of lists
    '''
    def _normalize(e, sz):
        return e[:sz] if len(e) >= sz else e + [filler] * (sz - len(e))
    return [_normalize(e, sz) for e in sq]