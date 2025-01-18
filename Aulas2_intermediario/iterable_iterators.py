iterable = ["Eu", "tenho", "__iter__"]

iterator = iter(iterable)#tem __iter__ e __next_



for item in iterable:
  print(next(iterator))