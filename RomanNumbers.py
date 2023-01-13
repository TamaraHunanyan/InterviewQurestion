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
    prevVal = 1000
    prevSym = "M"
    expected = ()
    sum = 0
    for idx in range(len(s)):
        val = romanDict.get(s[idx], None)
        if val is None:
            raise ValueError()
        sum += val
        if val > prevVal:
            if s[idx] not in expected:
                raise ValueError()
            sum -= 2*prevVal
            prevVal = 1000
            prevSym = "M"
            expected = ()
        else:
            sp = specialChars.get(s[idx], None)
            if sp is not None:
                prevVal = val
                prevSym = s[idx]
                expected = sp

    return sum
