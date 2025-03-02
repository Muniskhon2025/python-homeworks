class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum limit of books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        books = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name}, Borrowed Books: {books}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library.")

    def borrow_book(self, member, title):
        book = self.find_book(title)
        member.borrow_book(book)
        print(f"{member.name} successfully borrowed '{book.title}'")

    def return_book(self, member, title):
        book = self.find_book(title)
        member.return_book(book)
        print(f"{member.name} successfully returned '{book.title}'")

# Testing the Library Management System
if __name__ == "__main__":
    library = Library()
    
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("Moby Dick", "Herman Melville")
    book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    
    member1 = Member("Alice")
    member2 = Member("Bob")
    
    library.add_member(member1)
    library.add_member(member2)
    
    try:
        library.borrow_book(member1, "1984")
        library.borrow_book(member1, "To Kill a Mockingbird")
        library.borrow_book(member1, "Moby Dick")
        library.borrow_book(member1, "The Great Gatsby")  # Should raise MemberLimitExceededException
    except Exception as e:
        print(e)
    
    try:
        library.borrow_book(member2, "1984")  # Should raise BookAlreadyBorrowedException
    except Exception as e:
        print(e)
    
    try:
        library.borrow_book(member2, "Unknown Book")  # Should raise BookNotFoundException
    except Exception as e:
        print(e)
    
    library.return_book(member1, "1984")
    library.borrow_book(member2, "1984")  # Now possible since it's returned
