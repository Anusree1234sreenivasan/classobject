class Library:
    def __init__(self,name,address,phone_number):#self=object
        self.name= name
        self.address= address
        self.phone_number= phone_number
        self.books = []
    def book_taken(self,book): # book_taken is a method or function
        self.books.append(book)
    def book_returned(self,book):
        self.books.remove (book)
    def display(self):
        print(self.name,self.address,self.phone_number)
        print("Books:")
        print(self.books)
obj=Library("ANUS", "thamilnadu" ,"12345")
obj.book_taken("Python")
obj.book_taken("java")
obj.book_taken("c++")
obj.display()
obj.book_returned("Python")
obj.display()
obj.book_taken("c")
obj.display()
obj.book_returned("PYTHON")
obj.display()
