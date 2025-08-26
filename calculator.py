def main():
 while True:
  op=input();if op=='q':break
  a,b=map(int,input().split())
  if op=='+':print(a+b)
  elif op=='-':print(a-b)
  elif op=='*':print(a*b)
  elif op=='/':print(a/b)
if __name__=