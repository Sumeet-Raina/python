a = input("enter a ")
b = input("enter b ")
c = input("Enter sum or sub or div ")
if c == "sum":
    sum = int(a) + int(b)
    print(sum)
elif c == "div":
    div = int(a) / int(b)
    print(div)
elif c == "sub": 
    sub = int(a) - int(b)
    print(sub)
else:
  print("Count to 100")