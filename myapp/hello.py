import fire

def hello(name="World"):
  return "Hello %s!" % name

def multi(number1=0, number2=0):
  multnum = number1 * number2
  return f"The mult of {number1} and {number2} is {multnum}"

if __name__ == '__main__':
  fire.Fire(hello)
  fire.Fire(multi)