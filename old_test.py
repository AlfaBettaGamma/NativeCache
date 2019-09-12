import random
from NativeCache import NativeCache

class my_test():
  def test1(self):
    s = NativeCache(26,7)
    for i in range(s.size):
      s.put(str(i), i)
    for j in range(51):
      if j < 26:
        s.get(str(j))
      elif j < 35:
        s.get(str(j-26))
      else:
        s.get(str(j-35))    
    s.print_all()
    s.put('999',9000)
    s.print_all()
    s.put('888',8000)
    s.print_all()
    s.delete_all()
    s.print_all()
    print('test')

  def test2(self):
    s = NativeCache(26,7)
    for i in range(s.size):
      s.put(str(i), i)
    for j in range(51):
      if j < 26:
        s.get(str(j))
      elif j < 35:
        s.get(str(j-26))
      else:
        s.get(str(j-35))
    print(s.hits[10])
    s.print_all()
    print('_________________')
    s.get(str(0))
    s.print_all()
    print(s.hits[10])


test = my_test()
test.test2()
