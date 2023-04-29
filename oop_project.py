class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author}, Price: ${self.price}, Quantity: {self.quantity}"


class Author:
    def __init__(self, name, email, bio):
        self.name = name
        self.email = email
        self.bio = bio

    def __str__(self):
        return f"{self.name} ({self.email}): {self.bio}"


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.email}): {self.address}"


class Order:
    def __init__(self, customer, books):
        self.customer = customer
        self.books = books

    def total_cost(self):
        return sum(book.price for book in self.books)

    def __str__(self):
        book_list = "\n".join([f"  {book}" for book in self.books])
        return f"Order for {self.customer}:\n{book_list}\nTotal Cost: ${self.total_cost()}"


class Bookstore:
    def __init__(self):
        self.books = []
        self.authors = []
        self.customers = []
        self.orders = []

    def add_book(self, book):
        self.books.append(book)

    def add_author(self, author):
        self.authors.append(author)

    def add_customer(self, customer):
        self.customers.append(customer)

    def place_order(self, customer, books):
        order = Order(customer, books)
        self.orders.append(order)
        for book in books:
            book.quantity -= 1

    def list_books(self):
        print("Available Books:")
        for book in self.books:
            if book.quantity > 0:
                print(book)

    def list_authors(self):
        print("Authors:")
        for author in self.authors:
            print(author)

    def list_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(customer)

    def list_orders(self):
        print("Orders:")
        for order in self.orders:
            print(order)


bookstore = Bookstore()


book1 = Book("The Alchemist", "Paulo Coelho", 10.99, 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 7.99, 3)
book3 = Book("1984", "George Orwell", 12.99, 0)

bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)


print(bookstore.list_books())
