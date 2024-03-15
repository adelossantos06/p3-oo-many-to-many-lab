class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
      
    def contracts(self):
        matching_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                matching_contracts.append(contract)
        return matching_contracts

    def books(self):
        matching_books = []
        for contract in self.contracts():
                matching_books.append(contract.book)
        return matching_books

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        author_contracts = self.contracts()
        total = 0
        for contract in author_contracts:
            total += contract.royalties
        return total

class Book:
    all = []

    def __init__(self, title, date=None):
        self.title = title
        self.date = date
        Book.all.append(self)
    
    def contracts(self):
        matching_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                matching_contracts.append(contract)
        return matching_contracts

    def authors(self):
        matching_authors = []
        for contract in self.contracts():
            matching_authors.append(contract.author)
        return matching_authors



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be a percentage")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        matching_dates = []
        for contract in cls.all:
            if contract.date == date:
                matching_dates.append(contract)
        return matching_dates