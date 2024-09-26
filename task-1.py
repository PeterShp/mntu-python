class Solution(object):
    def romanToInt(s):   
        roman_symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        i = 0
        
        for i in range(len(s) - 1):
            if roman_symbols[s[i]] < roman_symbols[s[i+1]]:
                result -= roman_symbols[s[i]]
            else:
                result += roman_symbols[s[i]]
        return result + roman_symbols[s[-1]]