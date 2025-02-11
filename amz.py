
## finding maximum length of substring in which first element is smaller than last.
## appeared in Amz test


def find_max_chain_length(s: str) -> int:
    n = len(s)
    
    if n < 2:
        return 0
    
    # Quick check: if the entire string is valid, return n.
    if s[0] < s[-1]:
        return n
    
    # Convert string to a list of characters for easier manipulation
    arr = list(s)
    LMin = [None] * n
    RMax = [None] * n
    
    # Build prefix minimum array (LMin)
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(LMin[i - 1], arr[i])
    
    # Build suffix maximum array (RMax)
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(RMax[j + 1], arr[j])
    
    # Use two pointers to find maximum index difference such that LMin[i] < RMax[j]
    i, j = 0, 0
    max_diff = -1
    while i < n and j < n:
        if LMin[i] < RMax[j]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1
            # Ensure j is always at least i
            if i > j:
                j = i
    
    # Return the result (maxDiff + 1) or 0 if no valid chain was found
    return max_diff + 1 if max_diff != -1 else 0


 Optional testing
if __name__ == "__main__":
    print(find_max_chain_length("abcd"))       # Expected output: 4
    print(find_max_chain_length("fghbbadcba")) # Expected output: 5
    print(find_max_chain_length("ecbdca"))     # Expected output: 3
