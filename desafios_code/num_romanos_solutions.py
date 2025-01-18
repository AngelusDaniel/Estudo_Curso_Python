



def romanToInt(s: str) :

  num_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  total = 0

  for i in range(len(s)):
    if i+1 < len(s) and num_romanos[s[i]] < num_romanos[s[i+1]]:
      total -= num_romanos[s[i]]
    else:
      total += num_romanos[s[i]]

  return total


print(romanToInt("MCMXCIV"))
  


