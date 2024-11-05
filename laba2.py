import csv
import random
import time
import xml.etree.ElementTree as ET


def nazv():
    reader = csv.reader(books, delimiter=';')

    count = 0
    
    name = next(reader)
    
    numb = name.index('Название')
    
    for row in reader:
        if len(row[numb]) > 30:
            count += 1

    print(f"Количество записей с названием длиной больше 30 символов: {count}")       
            

def search(author):   
    reader = csv.reader(books, delimiter=';')
    
    name = next(reader)
    
    numb_author = name.index('Автор')
    numb_title = name.index('Название')
    
    books_author = []

    for row in reader:
        if author.lower() in row[numb_author].lower():
            books_author.append(row[numb_title])
    
    return books_author


def generate_bibliography(numery=20):

    reader = csv.reader(books, delimiter=';')
    name = next(reader)
    

    numb_author = name.index('Автор')
    numb_title = name.index('Название')
    numb_year = name.index('Дата поступления')
    

    elements = []
    for row in reader:
        elements.append(row)
    

    random_elements = random.sample(elements, min(numery, len(elements)))
    

    bibliography = []
    for i, j in enumerate(random_elements, 1):
        author = j[numb_author]
        title = j[numb_title]
        year = j[numb_year].split('.')[2][:-5]
        bibliography.append(f"{i}. {author}. {title} - {year}")
    
    return bibliography


def savefiletxt(bibliography, filename='bibliography.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in bibliography:
            f.write(line + '\n')


def currencyy():

    file_path = 'currency.xml'

    tree = ET.parse(file_path)
    root = tree.getroot()

    char_codes = []
    values = []


    for currency in root.findall('Valute'):
        char_code = currency.find('CharCode').text
        value = currency.find('Value').text

        char_codes.append(char_code)
        values.append(value)


    print(f'CharCode: {char_codes}')
    print(f'Value: {values}')


def unique():
        
    reader = csv.reader(books, delimiter=';')
    
    name = next(reader)
    numb_tags = name.index('Жанр книги')
    

    unique_tags = set()
    
    for row in reader:
        tags = row[numb_tags].split(',')
        for tag in tags:
            unique_tags.add(tag.strip())

    return unique_tags


def top_20_books():

    reader = csv.reader(books, delimiter=';')
    
    name = next(reader)
    
    numb_title = name.index('Название')
    numb_author = name.index('Автор')
    numb_give = name.index('Кол-во выдач')
    

    book = []
    
    for row in reader:
        try:
            title = row[numb_title]
            author = row[numb_author]
            give = int(row[numb_give])
            book.append((title, author, give))
        except:
            continue
    
    books_sorted = sorted(book, key=lambda x: x[2], reverse=True)
    
    top_20_books = books_sorted[:20]
    
    return top_20_books


if __name__ == "__main__":
    
    print('№1')
    with open('books.csv') as books:
        nazv()


    print()
    time.sleep(1.5)


    print('№2')   
    with open('books.csv') as books:  
        author_name = input("Введите имя автора для поиска: ")
        select_books = search(author_name)

        if select_books:
            print(f"Найденные книги автора {author_name}:")
            for book in select_books:
                print(book)
        else:
            print(f"Книги автора {author_name} не найдены.")


    print()
    time.sleep(1.5)


    print('№3')   
    with open('books.csv') as books:

        bibliography = generate_bibliography()
        savefiletxt(bibliography)

        print(f"Список библиографических ссылок сохранён в файл 'bibliography.txt'.")


    print()
    time.sleep(1.5)


    print('№4') 
    currencyy()   


    print()
    time.sleep(1.5)


    print('Доп. задание')
    with open('books.csv') as books:
        tags = unique()
        print("Уникальные теги:")

        for tag in tags:
            print(f'{tag}')


    time.sleep(1.5)
    print()


    with open('books.csv') as books:

        print("Топ 20 самых популярных книг:")

        for i, (title, author, give) in enumerate(top_20_books(), 1):
            print(f"{i}. {title} — {author}, Количество выдач: {give}")
