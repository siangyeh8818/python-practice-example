
while True :
  try:
    x = int(input("輸入數字 >"))
    break
  except ValueError:
    print("你的輸入並非數字")
