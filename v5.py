import sys
INIT_CAPACITY = 100 # 서비스의 크기가 커지면 키우면된다.
BUFFER_LENGTH = 1024 # 입력 넣는 최대 길이

class Person:
  def __init__(self, name, number, email, group):
    self.name = name
    self.number = number
    self.email = email
    self.group = group

directory = []
capacity = INIT_CAPACITY

def init():
  global directory, capacity, n
  directory = [None] * INIT_CAPACITY
  capacity = INIT_CAPACITY


def load(fileName):
  global directory
  try:
    with open(fileName, 'r') as fp:
      for line in fp:
        buffer = line.strip().split('#')
        name = buffer[0]
        number = buffer[1] if buffer[1] != " " else None
        email = buffer[2] if buffer[2] != " " else None
        group = buffer[3] if buffer[3] != " " else None
        add_person(name, number, email, group)
  except FileNotFoundError:
    print("Open failed.")

def add_person(name, number, email, group):
  global directory, capacity
  directory.append(Person(name, number, email, group))

def add(name, number, email, group):
  global directory, capacity
  directory.append(Person(name, number, email, group))
  directory.sort(key=lambda x: x.name)

def remove(name):
  global directory
  i = search(name)
  if i == -1:
    print("No person named '{}' exists.".format(name))
    return
  del directory[i]
  n -= 1
  print("'{}' was deleted successfully.".format(name))

def read_line(fp, n):
  i = 0
  while True:
    ch = fp.read(1)  # 파일에서 한 글자씩 읽습니다.
    if not ch or ch == '\n':
      break  # 파일의 끝에 도달하거나 줄바꿈 문자를 만나면 반복문을 종료합니다.
    if i < n:
      str[i] = ch
      i += 1
  str[i] = '\0'
  return i

def info():
  print("add 사람이름")
  print("    전화번호 이름을 저장합니다.")
  print("    사람이름은 띄워 쓸수 있습니다.")
  print("find 사람이름")
  print("    사람이름으로 전화번호 및 주소,그룹을 찾습니다.")
  print("status")
  print("    전화번호에 저장된 모든 정보를 찾습니다.")
  print("delete 사람이름")
  print("    저장된 정보를 지웁니다.")
  print("read file이름")
  print("    저장된file을 불러옵니다.")
  print("save as file이름")
  print("    원하는 이름으로 저장합니다.")
  print("info")
  print("    설명창을 띄웁니다.")
  print("exit")
  print("    서비스를 종료합니다.")


def save(fileName):
  try:
    with open(fileName, 'w') as fp:
      for i in range(n):
        fp.write(f"{directory[i].name}#")
        fp.write(f"{directory[i].number}#")
        fp.write(f"{directory[i].email}#")
        fp.write(f"{directory[i].group}#\n")
  except IOError:
    print("Open failed.")

def search(name):
  for i in range(n):
    if name == directory[i].name:
      return i
  return -1

def print_person(p):
  print(f"{p.name}'s INFO")
  print(f"    Phone: {p.number}")
  print(f"    Email: {p.email}")
  print(f"    Group: {p.group}")

def status():
  for i in range(len(directory)):
    print_person(directory[i])
  print(f"Total {len(directory)} persons.")

def find(name):
  index = search(name)
  if index == -1:
    print(f"No person named '{name}' exists.")
  else:
    print_person(directory[index])

def handle_add(name):
  print(f"Write {name}'s INFO.")
  number = input("    Phone: ")
  email = input("    Email: ")
  group = input("    Group: ")
  add(name, number if number else " ", email if email else " ", group if group else " ")

def main():
  while True:
    print("$ ", end="")
    command_line = sys.stdin.readline().strip()  # 명령어 라인을 읽어들입니다.
    if not command_line:
      continue  # 빈 명령어가 입력된 경우 루프를 다시 시작합니다.

    command, *arguments = command_line.split()  # 명령어와 인수를 분리합니다.
    if command == "read":
      if not arguments:
        print("Invalid arguments.")
        continue
      fileName = arguments[0]
      load(fileName)
    elif command == "add":
      if not arguments:
        print("Name required.")
        continue
      name_str = " ".join(arguments)
      handle_add(name_str)
    elif command == "find":
      if not arguments:
        print("Name required.")
        continue
      name_str = arguments[0]
      find(name_str)
    elif command == "status":
      status()
    elif command == "delete":
      if not arguments:
        print("Name required.")
        continue
      name_str = arguments[0]
      remove(name_str)
    elif command == "save":
      if len(arguments) < 2 or arguments[0] != "as":
        print("Invalid arguments.")
        continue
      fileName = arguments[1]
      save(fileName)
    elif command == "exit":
      break
    elif command == "info":
      info()

if __name__ == "__main__":
  main()


### 정렬 알고리즘, index가 애매