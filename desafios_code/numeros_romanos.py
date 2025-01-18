
num_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

roman = "MCMXCIV"

print(num_romanos[roman[1]])

arr_nums = []

sub = 0
soma = 0

for alg in roman:
  for chave, valor in num_romanos.items():
    if alg == chave:
      arr_nums.append(valor)

print(arr_nums)

#arr_nums.append(0)

for i in range(len(arr_nums)):
  if i+1 < len(arr_nums) and arr_nums[i] < arr_nums[i+1]: 
    sub += arr_nums[i]
  else:
    soma += arr_nums[i]

result = soma - sub

print(result)









  





