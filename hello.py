def lengthOfLongestSubstring(s):
    import pdb; pdb.set_trace()
    d,m,c,st={},0,0,0
    for i, e in enumerate(s):
        if e in d and d[e]>=st: m,c,st=max(m,c),i-d[e],d[e]+1
        else: c+=1
        d[e]=i
    return max(m,c)

print(lengthOfLongestSubstring('abcabcaa'))

print(lengthOfLongestSubstring('pwwkew'))
