#Custom exceptions

class BookNotFoundException(Exception):
    """Exception is raised when book is not found"""
    def __init__(self,message="Book is not found"):
        super().__init__(message)
        
class BookAlreadyBorrowedException(Exception):
    """Exception is raised when book is already borrowed"""
    def __init__(self,message="Book has already been borrowed",is_borrowed=None):
        super().__init__(message)
        self.is_borrowed = is_borrowed
        
class MemberLimitExceededException(Exception):
    """Exception is raised when limit is exceeded"""
    def __init__(self,message="You have exceeded the limit",limit=None):
        super().__init__(message)
        self.limit=limit
        
#Book class

class Book:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

#Member class 

class Member:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = 0
        
#Library

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        
    def add_book(self,title,author):
        if title in self.books:
            self.books[title][1]+=1
        else:
            self.books[title][0]=author
            self.books[title][1]=1
        return f'Book "{title}" by {author} added to the library.'
            
    def add_member(self,name):
        if name not in self.members:
            self.members[name]=0
            return f"Member {name} added."
        else:
            return "This member already exists."
    
    def borrow_book(self, title, name):
        #checking for exceptions
        if title not in self.books:
            raise BookNotFoundException(f"The book '{title}' is not available in the library.")
        
        if self.books[title]["count"] == 0:
            raise BookAlreadyBorrowedException(f"The book '{title}' has already been borrowed.", is_borrowed=True)

        if name not in self.members:
            return "This member does not exist in the members list."

        if self.members[name] >= 2:
            raise MemberLimitExceededException(f"{name} has exceeded the borrowing limit.", limit=2)

        # Borrow the book
        self.books[title]["count"] -= 1
        self.members[name] += 1
        return f"{name} has successfully borrowed '{title}'."
    
    def return_book(self,title,name):
        self.books[title]["count"]+=1
        self.members[name] -= 1
        return f"{name} has returned the {title}"
        
        
        