class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print("ketab gharz gerefte shod")
        else:
            print("in ketab dar dastres nist")

    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print("ketab bargardande shod")
        else:
            print("in shakhs ketab ro gharz nagerefte")

    def show_available_books(self):
        for book in self.books:
            if book.available:
                print(book.title)