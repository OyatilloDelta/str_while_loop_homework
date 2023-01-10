def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    while i!=len(s):
        d=s.isdigit(i)
        i+=1
    return i
print(main('ss12'))