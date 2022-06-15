"""
1- Write a function that flattens the list. Its elements can
consist of multi-layered lists(such as [[3],2]) or non-scalar data.

For example: 

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

def f(list_):
     for i in list_:
          if isinstance(i,list):
               f(i)
          else:
               flatList.append(i)
     return flatList

x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


flatList = list()

print(f(x))

