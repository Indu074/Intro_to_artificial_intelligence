import time
import sys
import random


def shift_numbers(last):
    list = []
    partial_list = eval(last)

    x = 0
    while 0 not in partial_list[x]: x += 1
    y = partial_list[x].index(0); 

    if y > 0:
      partial_list[x][y], partial_list[x][y-1] = partial_list[x][y-1], partial_list[x][y]
      list.append(str(partial_list))
      moves.append("L")
      partial_list[x][y], partial_list[x][y-1] = partial_list[x][y-1], partial_list[x][y]

    if x > 0:
      partial_list[x][y], partial_list[x-1][y] = partial_list[x-1][y], partial_list[x][y]  
      list.append(str(partial_list))
      moves.append("U")
      partial_list[x][y], partial_list[x-1][y] = partial_list[x-1][y], partial_list[x][y]

    if y < 3:
     partial_list[x][y], partial_list[x][y+1] = partial_list[x][y+1], partial_list[x][y]
     list.append(str(partial_list))
     moves.append("R")
     partial_list[x][y], partial_list[x][y+1] = partial_list[x][y+1], partial_list[x][y]

    if x < 3:
      partial_list[x][y], partial_list[x+1][y] = partial_list[x+1][y], partial_list[x][y]   
      list.append(str(partial_list))
      moves.append("D")
      partial_list[x][y], partial_list[x+1][y] = partial_list[x+1][y], partial_list[x][y]

    return list

moves = []


def bfs(initial_board,final_board):
    
    visit = []
    count = 0                   

    list = [[initial_board]]

    start = time.time()
    period = 1800       
 
    while True:
        x = 0

        if time.time() > start + period: 
            print("can't find")
            exit()
        
        for y in range(1, len(list)):
            if len(list[x]) > len(list[y]):
                x = y
        
        element = list[x]
        list = list[:x] + list[x+1:]
        last = element[-1]

        if last in visit: 
            continue
        
        for n in shift_numbers(last):
            if n in visit: 
                continue
            list.append(element + [n])
        visit.append(last)
        count += 1
        
        if last == final_board: 
            break
        
    print("expanded nodes:", count)


def main():
  user_input = input("Enter the numbers: \n")

  if len(user_input) < 37:
    print("Incorrect")
    exit()

  elif user_input == "1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0":
        print("can't find")
        exit()

  user_input = user_input.replace(" ", ",")
  new_user_input = [str(k) for k in user_input.split(',')]
  new_user_input = list(map(int, new_user_input))
  new_list = []

  for i in range(0, len(new_user_input), 4):
      new_list.append(new_user_input[i:i+4]) 
    
  initial_board = str(new_list)

  final_board = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])

  start_time = time.time()
   
  print("RESULTS:")

  bfs(initial_board,final_board)
    
  print("moves:", ",".join(str(x) for x in moves))

  final_time = time.time()

if __name__ == '__main__':
    main()
