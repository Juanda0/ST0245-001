import collections
def calculator(oper):
  operArr = oper.split(" ")
  calculator = collections.deque([])
  for element in operArr:
    if element.isnumeric(): 
      calculator.append(int(element))
    else:
      if len(calculator) <= 1:
        print("SyntaxError, Revise el orden de los elementos")
        return
      n1 = calculator.pop()
      n2 = calculator.pop()
      if element == '+':
        calculator.append(n1 + n2)
      if element == '-':
        calculator.append(n2 - n1)
      if element == '*':
        calculator.append(n1 * n2)
      if element == '/':
        calculator.append(n2 / n1)
  print(calculator.pop())
