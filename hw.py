documents_list = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


directories_dict = {
      '1': ['2207 876234', '11-2'],
      '2': ['10006'],
      '3': []
    }


def add_to_documents(documents, add_fields):

  for doc in documents:
    if add_fields['type'] == doc['type'] and add_fields['number'] == doc['number'] and add_fields['name'] == doc['name']:
      print('Документ уже существует в каталоге!')
      return dict()
    else:
      documents.append(add_fields)
      print('Документ добавлен в каталог')
      return documents


def add_to_shelf(directories, shelf, doc_number):
  if shelf  in directories.keys():
      directories[shelf].append(doc_number)
      print('Документ добавлен на полку')
      return directories
  else:
    while shelf not in directories.keys():
      available_shelves = ", ".join(directories.keys())
      print(f'Такой полки не существует! Выберите доступную полку. Доступные полки {available_shelves}') 
      shelf = input("Номер полки: ")
      if shelf  in directories.keys():
        directories[shelf].append(doc_number)
        print('Документ добавлен на полку')
      return directories

def delete_document(documents,directories, doc_number):
  
  for doc in documents:
    if doc['number'] == doc_number:
      print('Документ удален из каталога.')
      documents.remove(doc)

  for shelf in directories:
    if doc_number in directories[shelf]:
      directories[shelf].remove(doc_number)
      print('Документ удален c полки.')

  return documents, directories


def move_document_in_shelves(directories):
  doc_number = input("Номер документа: ")
  find_doc = False
  for directory in directories.values():
    if doc_number in directory:
      directory.remove(doc_number)
      find_doc = True

  if find_doc:
    shelf = input("На какую полку переместить? ")
    try:
      directories[shelf].append(doc_number)
      print('Документ перемещен.')
      return directories
    except KeyError:
      available_shelves = ", ".join(directories.keys())
      continue_adding = input(f'Целевой полки не существует. Доступные полки {available_shelves}. Продолжить перемещение? y/n ')
      if continue_adding == 'y':
        try:
          shelf = input("На какую полку переместить? ")
          directories[shelf].append(doc_number)
          print('Документ перемещен.')
          return directories
        except:
          print('Целевой полки не существует. Перемещение не удалось.')
      else:
        print('Прервано')


  else:
    print('Такого документа нет!') 


def add_shelf(directories):
  shelf = input("Какую полку создать? ") 

  if shelf:
    if not directories.get(shelf):
      directories.setdefault(shelf,[])
      print ('Новая полка создана!')
    else:
      print('Эта полка уже существует')
    return directories
  return directories



def find_doc(documents, doc_number):  

  for doc in documents:
    if doc_number  == doc['number']:
      # return f"Документ принадлежит {doc['name']}"
      return doc['name']

  # return f'Документ не найден'
  return

def find_doc_in_shelf(directories, doc_number):  

  for directory in directories.items(): 
    if doc_number in directory[1]:          
      # return f'Документ на полке № {directory[0]}'
      return directory[0]

  # return f'Документ не найден'
  return

def check_command(command, documents, directories):

    if command == 'p':
      doc_number = input("Номер документа: ")
      return find_doc(documents, doc_number)

    elif command == 's':      
      doc_number = input("Номер документа: ")
      return find_doc_in_shelf(directories, doc_number)
    
    elif command == 'l': 
      all_docs = []
      print('Все документы:\n')
      for doc in documents:
        print(f"{doc['type']}", f"\"{doc['number']}\"", f"\"{doc['name']}\"")


    elif command == 'a':
      add_fields = {}
      add_fields['type'] = input("Тип документа: ") # passport
      add_fields['number'] = input("Номер документа: ") # 2207 876234
      add_fields['name'] = input("Имя владельца: ") # Василий Гупкин
      shelf = input("Номер полки: ") #1

      new_documents = add_to_documents(documents, add_fields)
      if new_documents:
        new_in_shelf = add_to_shelf(directories, shelf, add_fields['number'])

    elif command == 'd':        
      new_documents = delete_document(documents, directories)
    
    elif command == 'm':         
      new_documents = move_document_in_shelves(directories)
    
    elif command == 'as':         
      result = add_shelf(directories)

    else:
      print('Команда не найдена.\nДоступные команды p, s, l, a, d, m, as')


if __name__ == '__main__':  
  print('====================== Задача №1 ====================================')
  command = input("Введите команду: ")
  d = check_command(command, documents_list, directories_dict)
  if d:
    print(d)