def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    while i!=len(s):
        if i[s]==1:
            ans+=1
        if i[s]==2:
            ans+=1
        if i[s]==3:
            ans+=1
        
    return ans
print(main('213'))