def longestCommonPrefix(self, strs: List[str]) -> str:

    final = ""
    sl = sorted(strs)
    first,last = sl[0], sl[-1]

    for i in range(len(min(first,last))):
        if first[i] != last[i]:
            return final

        final += first[i]
    return final
