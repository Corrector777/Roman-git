HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""
today_tasks = []
tomorrow_tasks = []
other_tasks = []


while True:

    command = input("Введите команду: ")
    if command.lower().strip() == "help":
        print(HELP)
    elif command.lower().strip() == "show":
        print(f'Задачи сегодня: {today_tasks}')
        print(f'Задачи на завтра: {tomorrow_tasks}')
        print(f'Иные задачи: {other_tasks}')
    elif command.lower().strip() == "add":
      
      date_task = input("Введите дату выполнения задачи: ")
      task = input ('Введите  задачу: ')
      if date_task.lower().strip() == 'сегодня':
        today_tasks.append(task)
        print(f"Задача <{task}> добавлена")
      elif date_task.lower().strip() == 'завтра':
        tomorrow_tasks.append(task)
        print(f'Задача <{task}> добавлена')
      else:
        other_tasks.append(task)
        print(f'Задача <{task}> добавлена')    
    elif command.lower().strip() == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else: 
        print("Неизвестная команда! Попробуйте еще раз")
        

print("До свидания!")