# here i will put the functions that i will use
from book import book
import json

class library:
  def __init__(self):
    self.books = []
  
  def adding_books(self):
     book_name = input("Enter the book name: ")
     author = input("enter the author: ")
     category = input("enter the category: ")
     book1 = book(book_name, author, category)
     self.books.append(book1)
     print("Book added!")

  def save_library(self):
    if self.books:
      with open("my_library.json",'w') as file:
        data = []
        for book in self.books:
          cd = {"name":book.book_name,"author":book.author,"category":book.category}
          data.append(cd)
        json.dump(data,file)
        print("Library saved!")
    else:
      print("library is empty")
        
  def load_library(self):
    try:
      with open("my_library.json",'r') as file:
        data = json.load(file)
        self.books = [book(b["name"],b["author"],b["category"]) for b in data]
      print("Library loaded!")
    except FileNotFoundError:
      print("No saved library found")

  
  def display_books(self):
    if self.books:
      print("\nBooks: ")
      for i,book in enumerate(self.books):
        print(f"{i+1}. book title : {book.book_name}, author: {book.author}, category: {book.category}")
    else:
      print("\nNo books available")

  def visualize_by_category(self):
    # unique categories in the list
    # I will save categories in list
    if self.books:
      categories = []
      for book in self.books:
        categories.append(book.category)
      unique = set(categories)
      unique_dict = {}
      for category in unique:
        unique_dict[category] = categories.count(category)
      print("\nCategories as follow: \n")
      for key,value in unique_dict.items():
        print(f"{key} : {value}")
      print("\n")
    else:
      print(f"No books available")

  def search_book(self):
      if self.books:
        book_name = input("Enter the book name: ")
        for book in self.books:
          if book.book_name == book_name:
            print(f"Book found: {book.book_name}, author: {book.author}, category: {book.category}")
            return
        
        print("Book not found")
      else:
        print("No books available")
      
  def delete_book(self):
    if self.books:
      book_name = input("Enter the book name: ")
      for book in self.books:
        if book.book_name == book_name:
          self.books.remove(book)
          print("Book deleted!")
          return
      print("Book not found")
    print("No books available")
    
    
  