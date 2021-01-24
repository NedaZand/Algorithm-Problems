
def longestSubString(str):
    if len(str) == 0:
        return 0
    strDict = {}
    maxLength = start = 0
    for i in range(len(str)):
        if str[i] in strDict and start <= strDict[str[i]]:
            start = strDict[str[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        strDict[str[i]] = i
    return (maxLength)

print(longestSubString("abcbcadde   "))
    

        
            