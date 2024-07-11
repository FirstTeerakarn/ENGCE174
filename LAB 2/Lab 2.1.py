n = 5 # กำหนดค่าตัวแปล n

while True:
  num_input = input("กดเลขที่ต้องการ : " )
  if num_input == '5':  # เช็คตัวเลขว่าตรงกับที่กรอกไปหรือป่าว
    for i in range(1, n+1):
      print('* ' * i)
    print("------------------------")
    for i in range(n, 0, -1):
      print('* ' * i)
    print("------------------------")
    for i in range(1, n+1):
      print('  ' * (n - i) + '*  ' * i)
    print("------------------------")
    for i in range(n, 0, -1):
      print('  ' * (n - i) + '*  ' * i)
    print("------------------------")
    for i in range(1, n+1):
      print('    ' * (n - i) + '*  ' * i )
    print("------------------------")
    break
