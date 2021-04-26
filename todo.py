import time



HELP = """
add - добавить задачу
show - показать задачу
done - убрать выполненую задачу
exit - закрытть приложение
"""


todo = {}

def checkDate(date):
  try:
    time.strptime(date, "%d.%m.%Y")
    return True
  except ValueError:
    print("Error. Не правильный формат даты")
    return False



print("Введите команду , введите help для вывода списка команд")

while True:
  userAnswer = input()

  if userAnswer == "add":
    userDate = input("Введите дату:\n")
    userTask = input("Что нужно сделать?")

  
    if userDate in todo.keys():
     todo[ userDate ].append(userTask)
    else: 
       todo[ userDate ] = [userTask]
    print(f"[{userDate}] - добавлена задача '{userTask}'")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает")
  elif userAnswer =="show":
   for date in sorted(todo.keys()):
     for tasks in todo [ date ]:
      print(f"[{date}] -  {tasks} ")
  print ("Работает")
  
