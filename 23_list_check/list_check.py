def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    ct = 0
    for item in lst:
        if isinstance(item, list):
            ct += 1
    if ct == len(lst):
        return True
    else:
        return False