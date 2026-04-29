from add_books import add
from issue_books import issue
from show_books import show
from return_books import return_book

def library():
    while True:
        print("\n1. To Add Book")
        print("2. To Show Book")
        print("3. To Issue Book")
        print("4. To Return Book")
        print("5. To exit the system")
        choice = int(input("Select your choice "))
        
        if choice==1:   add()
        elif choice==2: show()
        elif choice==3: issue()
        elif choice==4: return_book()
        elif choice==5: 
            print("Thank you for working with us")
            break
        else:
            print("Wrong option selected")
            
library()