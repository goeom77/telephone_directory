import sys
from collections import deque

sys.stdin.flush() # 버퍼를 비운다.
input = sys.stdin.readline

# todo : 토크나이저와 함께 만들어보기
def readline():
    return

names = deque(maxlen=100)
numbers = deque(maxlen=20)
n = 0

flag = True

# add 사람이름 전화번호
def add(commands):
    global n
    if len(commands) < 3:
        print("command error")
        return
    names.append(commands[1])
    numbers.append(commands[2])
    i = len(names)
    for j in range(n-1,-1,-1):
      if names[j-1] > names[j]:
        names[j] = names[j-1]
        numbers[j] = numbers[j-1]
      break

    n += 1
    print(f"{commands[1]} was added successfully.\n")

# find 사람이름
def find(commands):
    if len(commands) < 2:
        print("command error")
        return
    if commands[1] in names:
        return
    else:
        print(f"No Person named '{commands[1]}' exists.\n")

# status
def status(commands):
    for i in range(n):
        print(f"{names[i]} {numbers[i]}")
    print(f"Total {n} persons")

# remove 사람이름
def remove(commands):
    global n
    if len(commands) < 2:
        print("command error")
        return
    for i in range(n):
        if names[i] == commands[1]:
            names.pop(i)
            numbers.pop(i)
            n -= 1
            print(f"'{commands[1]}' was deleted successfully.\n")
            return
    print(f"No person named '{commands[1]}' exists.\n")
# search 넣기

#exit
def exit():
    global flag
    flag = False

# load file이름
def load(commands):
    global n
    if (len(commands)<2):
        print("Open fialed")
        return
    fileName = commands[1]
    try:
        with open(fileName, "r") as fp:
            for line in fp:
                data = line.strip().split()
                names.append(data[0])
                numbers.append(data[1])
                n += 1
    except FileNotFoundError:
        print("Open failed")

# save file이름
def save(commands):
    global n
    fileName = commands[1]
    if (len(commands)<3):
      print("Open fialed")
      return
    try:
        with open(fileName, "w") as fp:
            for i in range(n):
                fp.write(f"{names[i]} {numbers[i]}\n")
    except:
        print("Open failed.")


# command 관리 창
while(flag):
    command = input().rstrip() # '\n'
    commands = command.split()
    if commands[0] == "add":
        add(commands)
    elif commands[0] == "find":
        find(commands)
    elif commands[0] == "status":
        status(commands)
    elif commands[0] == "remove":
        remove(commands)
    elif commands[0] == "exit":
        exit()
    elif commands[0] == "load":
        load(commands)
    elif commands[0] == "save" and commands[1] == "as":
        save(commands)