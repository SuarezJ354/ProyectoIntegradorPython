class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def show_data(self):
        return f"Titulo: {self.title}, Autor: {self.author}, Año: {self.year}, Genero: {self.genre}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Ingresa el titulo del libro: ")
        author = input("Ingresa el autor: ")
        year = input("Ingresa el año de lanzamiento del libro: ")
        genre = input("Ingresa el genero del libro: ")
        new_book = Book(title, author, year, genre)
        self.books.append(new_book)
        print("Libro añadido.")

    def remove_book(self):
        title = input("Ingresa el titulo dle libro a remover: ")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Libro eliminado.")
                return
        print("Lirbo no encontrado.")

    def search_book(self):
        title = input("Ingresa el titulo del libro a buscar: ")
        for book in self.books:
            if book.title == title:
                print(book.show_data())
                return
        print("Libro no encontrado.")

    def list_books(self):
        if not self.books:
            print("No hay libros en la biblioteca.")
            return
        for book in self.books:
            print(book.show_data())
            print("---")