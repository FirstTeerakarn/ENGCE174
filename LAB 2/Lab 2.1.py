# -*- coding: utf-8 -*-
"""LAB 2.1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lNwSeZtc9COeX5F5JOJINCT3ccIPe99E
"""

while True:
  num_input = input("กดเลข '5' : " )
  if num_input == '5':
    for i in range(1, 6):
      print('* ' * i)
    print("-----------------")
    for i in range(5, 0, -1):
      print('* ' * i)
    print("-----------------")
    for i in range(1, 6):
      print('  ' * (5 - i) + '*  ' * i)
    print("-----------------")
    for i in range(5, 0, -1):
      print('  ' * (5 - i) + '*  ' * i)
    print("-----------------")
    for i in range(1, 6):
      print('    ' * (5 - i) + '*  ' * i )
    print("-----------------")
    break

