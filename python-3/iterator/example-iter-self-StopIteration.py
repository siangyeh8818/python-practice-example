#!/usr/local/bin/python3


class Numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 100:
          x= self.a
          self.a +=1
          return x
        else:
          raise StopIteration

myclass = Numbers()
myiterator = iter(myclass)

for x in myiterator:
      print(x)