from library import library

def main():
  print('''Welcome to Your Personal Library Manager!

What would you like to do?

1. Add a book

2. Save library to file

3. Load library from file

4. Visualize library by category

5. display books

6. search book

7. delete book

8. Quit

Enter choice:\n''')  
  choice = None
  l1 = library()
  while choice != 8:
    choice = int(input("Choice: "))
    if choice == 1:
      l1.adding_books()
    elif choice ==2:
      l1.save_library()
    elif choice == 3:
      l1.load_library()
    elif choice==4:
      l1.visualize_by_category()
    elif choice ==5:
      l1.display_books()
    elif choice == 6:
      l1.search_book()
    elif choice ==7:
      l1.delete_book()
    elif choice !=8:
      print("invalid input please choose from the list")
  print("Goodbye!")

if __name__ == "__main__":
  main()
  
  