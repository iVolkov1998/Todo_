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
    print("Работает")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Работает")