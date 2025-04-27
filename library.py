def get_shelfs_book():
    quantity = int(input("Сколько книг вы хотите добавить?"))
    for index in range(quantity):
        number = int(input("На какую полку добавить книгу:"))
        book_name = input("Название книги:")
        author = input("Автор книги:")
        book_format = {'name' : None, 'authors' : None}
        book_format["name"] = book_name
        book_format["authors"] = author
        shelf_format = "shelf_{} : {}"
        shelf_format = shelf_format.format(number, book_format)
        with open("Library.txt", "a") as f:
            f.write(f"{shelf_format}\n")

    
def read_file_library():
    with open("Library.txt", "r") as f:
        for line in f:
            print(line.strip("\n"))


def main():
    get_shelfs_book()
    read_file_library()


if __name__ == '__main__':
    main()