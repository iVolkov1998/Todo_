HELP = """
add - добавить задачу
show - показать задачу
done - убрать выполненую задачу
exit - закрытть приложение

"""
todo = {}
print("Введите команду , введите help для вывода списка команд")

while True:
  userAnswer = input()

  if userAnswer == "add":
    userDate = input("Введите дату:\n")
    userTask = input("Что нужно сделать?")
    todo[userDate] = userTask
    print(f"[{userDate}] - добавлена задача '{userTask}' " )
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает")
  elif userAnswer =="show":
    for date in todo.keys():
     print(f"[{date}] - \t {todo [date] }")

