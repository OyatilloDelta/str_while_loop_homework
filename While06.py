def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    j=0
    x="aioueo'"
    while i<len(s):
        if not s[i] in x:
            j+=1
        i+=1
    return j
print(main('oyy'))

   