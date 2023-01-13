def romanToInt(s):
    romanDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    specialChars = {"I": ("V", "X"),
                    "X": ("L", "C"),
                    "C": ("D", "M")}
    sum = 0
    specialSymb = None
    for idx in range(len(s)):
        val = romanDict.get(s[idx], None)
        if val is None:
            raise ValueError()

        if specialSymb is None:
            specialSymb = specialChars.get(s[idx], None)
            if specialSymb is None:
                sum += val
            else:
                specialVal = val
        else:
            if s[idx] in specialSymb:
                sum += val
                sum -= specialVal
            else:
                if val > specialVal:
                    raise ValueError()
                sum += val;
                sum += specialVal
            specialVal = None
            specialSymb = None
    if specialVal is not None:
        sum += specialVal
    return sum
