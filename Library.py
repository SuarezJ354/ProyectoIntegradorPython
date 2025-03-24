class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def show_data(self):
        return f"Titulo: {self.title}, Autor: {self.author}, Año: {self.year}, Genero: {self.genre}".title()

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def register_user(self):
        print("Registro de Usuario")
        username = input("Ingresa un usuario: ")
        password = input("Ingresa una contraseña: ")
        role = input("Ingresa su rol (admin/usuario): ")
        if role not in ("admin","usuario"):
            print("Rol invalido.")
            return None
        newUser = User(username, password, role)
        self.users.append(newUser)
        print("Usuario registrado exitosamente.")

    def login_user(self):
        username = input("Ingresa tu usuario: ")
        password = input("Ingresa tu contraseña: ")

        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Bienvenido, {username}. Eres {user.role}.")
                return user
        print("Usuario o contraseña incorrectos.")
        return None

    def add_book(self):
        title = input("Ingresa el titulo del libro: ").lower()
        author = input("Ingresa el autor: ")
        year = input("Ingresa el año de lanzamiento del libro: ")
        genre = input("Ingresa el genero del libro: ")
        new_book = Book(title, author, year, genre)
        self.books.append(new_book)
        print("Libro añadido.")

    def remove_book(self):
        title = input("Ingresa el titulo del libro a remover: ").lower()
        for book in self.books:
            if book.title.lower() == title:
                self.books.remove(book)
                print("Libro eliminado.")
                return
        print("Lirbo no encontrado.")

    def search_book(self):
        title = input("Ingresa el titulo del libro a buscar: ").lower()
        for book in self.books:
            if book.title.lower() == title:
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
    
    def edit_book(self):
        title = input("Ingresa el titulo del libro a editar: ").lower()
        for book in self.books:
            if book.title.lower() == title:
                book.title = input("Nuevo título: ")
                book.author = input("Nuevo autor: ")
                book.year = input("Nuevo año: ")
                book.genre = input("Nuevo género: ")
                print("Libro actualizado.")
                return
        print("Libro no encontrado.")

    def borrow_book(self):
        title = input("Ingresa el título del libro que deseas prestar: ").lower()
        for book in self.books:
            if book.title.lower() == title:
                print(f"Has prestado el libro: {book.title.title()}")
                self.books.remove(book)
                return
        print("Libro no encontrado o ya prestado.")


library = Library()

def menuLogin(library):
    while True:
        print("\n\nBiblioteca")
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Salir")
        option = int(input("Seleciona una opcion: "))

        if option == 1:
            user = library.login_user()
            if user:
                main_menu(library, user)
        elif option == 2:
            library.register_user()
        elif option == 3:
            print("Hasta Pronto")
            break
        else:
            print("Opcion invalida")

def main_menu(library, logged_in_user):

    while True:
        if logged_in_user.role == "admin":
            print("\n\nMenu Principal")
            print("1. Añadir libro")
            print("2. Eliminar libro")
            print("3. Buscar libro")
            print("4. Mostrar libros")
            print("5. Editar libro")
            print("6. Salir")
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
                library.edit_book()
            elif option == 6:
                print("Hasta pronto")
                break
            else:
                print("Opcion invalidad")
        elif logged_in_user.role == "usuario":
            print("\n\nMenu Principal Usuario")
            print("1. Mostrar libros disponibles")
            print("2. Prestar libro")
            print("3. Salir")
            option = int(input("Seleciona una opcion: "))

            if option == 1:
                library.list_books()
            elif option == 2:
                library.borrow_book()
            elif option == 3:
                print("Hasta pronto")
                break
            else:
                print("Ingresa una opcion")





##Sistema de inicio sesion/roles
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

##Libros predeterminados
library.books.append(Book("Antes de diciembre", "Joana Marcús", 2021, "Romance"))
library.books.append(Book("El susurro de los árboles", "Javier Martínez", 2015, "Drama"))
library.books.append(Book("Más allá del horizonte", "Isabel Torres", 2019, "Romance"))
library.books.append(Book("El misterio del faro", "Roberto Sánchez", 2016, "Misterio"))
library.books.append(Book("Historias de la luna", "Ana Ruiz", 2005, "Fantasía"))
library.books.append(Book("El Principito", "Antoine de Saint-Exupéry", 1943, "Fantasía"))
library.books.append(Book("Después de diciembre", "Joana Marcús", 2022, "Romance"))
library.books.append(Book("A través de mi ventana", "Ariana Godoy", 2019, "Romance"))
library.books.append(Book("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Fantasía"))
library.books.append(Book("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico"))
library.books.append(Book("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, "Romance"))
library.books.append(Book("Delirio", "Laura Restrepo", 2004, "Novela"))
library.books.append(Book("El olvido que seremos", "Héctor Abad Faciolince", 2006, "Biografía"))
library.books.append(Book("La tejedora de coronas", "Germán Espinosa", 1982, "Histórica"))
library.books.append(Book("Sangre de campeón", "Carlos Cuauhtémoc Sánchez", 2001, "Infantil"))
library.books.append(Book("Rosario Tijeras", "Jorge Franco", 1999, "Novela"))


menuLogin(library)
