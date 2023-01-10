def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    j=0
    while i<len(s):
        if s[i].isdigit():
            j+=1
        i+=1
    return j
print(main('jscv 345'))
    