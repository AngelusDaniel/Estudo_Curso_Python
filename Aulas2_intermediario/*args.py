

x, y, *resto = 1, 2, 3, 4

print(x, y, resto)


def soma(*args):
  print(args)
  total = 0
  for num in args:
    #total = total + num
    print(total, num)
    total += num
  total2 = sum(args)
  return total, total2
    


print(soma(1, 2, 3, 4, 5, 6))


#proprio do python
print(sum((1,2,3,4,5,6, 10, 21, 5, 6, 7, 8, 9)))





