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

def main_menu():
    library = Library()

    while True:
        print("\n\nMenu Principal")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Mostrar libros")
        print("5. Salir")
        option = int(input("Seleciona una opcion: "))

        if option == 1:
            library.add_book()
        elif option == 2:
            library.remove_book()
        elif option == 3:
            library.search_book()
        elif option == 4:
            library.list_books()
        elif option == 5:
            print("Hasta pronto")
            break
        else:
            print("Opcion invalidad")

main_menu()