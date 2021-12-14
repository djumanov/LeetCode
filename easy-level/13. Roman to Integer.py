# class Solution:
def romanToInt(s):
    data = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    lst = ['IVXLCDM']
    result = 0
    i = 0
    while i <= len(s)-1:
        if lst.find(s[i]) >= lst.find(s[i+1]):
            result += data.get(s[i])
        else:
            i += 1
            result += data.get(s[i]) - data.get(s[i-1])
        i += 1
    return result

# test = Solution()
print(romanToInt("III"))