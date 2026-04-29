from utils import books
def show():
    if len(books)==0:   
        print("No book currently available for issue")
    else:
        print(books)
        
            