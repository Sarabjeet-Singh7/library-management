from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books:
        if books[book_name]>=1:
            books[book_name]-=1

            if book_name in issue_books:
                issue_books[book_name]+=1
                print("Book issued successfully")
            else:
                issue_books[book_name]=1    
                print("Book issued successfully")
        else:
            print("Book is not available in library")
    else:
        print("Book is not available in library")