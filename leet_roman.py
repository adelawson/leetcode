def romanToInt(s):
        roman_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                     "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
                     "IV": 4, "I": 1}
        num = 0
        inc = 0
        for i in range(len(s)):
            if i+inc >= len(s):
                break
            i = i+inc
            if i+1 < len(s):
                if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                    num += roman_dict[s[i]]
                else:
                    num += roman_dict[s[i]+s[i+1]]
                    inc += 1
            else:
                num += roman_dict[s[i]]
        return num
