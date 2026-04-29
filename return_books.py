from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        if issue_books[book_name]==1:
            issue_books.pop(book_name)
        else:
            issue_books[book_name]-=1    
        books[book_name]+=1
        print("Book returned successfully")
    else:
        print("Book not issued from here")