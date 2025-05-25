def anagrams(strs):

    mydic = defaultdict(list)

    for i in strs:

        word = ''.join(sorted(i))
        mydic[word].append(i)

    return list(mydic.values())
