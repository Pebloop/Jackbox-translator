def safe_member(optional_of, member):
    if optional_of is None:
        return None
    return getattr(optional_of, member)
