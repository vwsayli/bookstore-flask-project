import pymysql as pm

class Store:

    def __init__(self,id=0,name=None,author=None,copies=0,price=0):
        self.bookId = id
        self.bookName = name
        self.bookAuthor = author
        self.bookCopy = copies
        self.bookPrice = price



con = pm.connect(host='localhost',
                    user='root',
                    password='root',db='bookstore')
    
cursor = con.cursor()

def insertbook(bk):
    try:
        sqlQuery = f"insert into book values ({bk.bookId},'{bk.bookName}','{bk.bookAuthor}',{bk.bookCopy},{bk.bookPrice})"
        cursor.execute(sqlQuery)
        con.commit()
        return 'Book Saved Successfully'
    except Exception as e:
        print('Error:- ',e)
        return 'Book is not Saved'

def showallbook():
    try:
        booklist = []
        sqlQuery = f"select * from book"
        cursor.execute(sqlQuery)

        rows = cursor.fetchall()
        for row in rows:
            bk = Store(row[0],row[1],row[2],row[3],row[4])
            booklist.append(bk)
        else:
            return booklist
        con.commit()
    except Exception as e:
         print('Error:- ',e)

def delete_book(bookId):
    try:
        sqlQuery = f"delete from book where bookId={bookId}"
        cursor.execute(sqlQuery)
        con.commit()
        return 'Book Deleted Successfully'
    except Exception as e:
        print('Error:- ',e)
        return 'Book is not Deleted'

def get_book_byid(bookId):
    try:
        sqlQuery = f"select *  from book where bookId={bookId}"
        cursor.execute(sqlQuery)
        row = cursor.fetchone()
        bk = Store(row[0],row[1],row[2],row[3],row[4])
        con.commit()
        return bk
    except Exception as e:
        print('Error:- ',e)
        return

def update_book(bk):
    try:
        sqlQuery = f"update book set bookName='{bk.bookName}', bookAuthor='{bk.bookAuthor}',bookCopy={bk.bookCopy},bookPrice={bk.bookPrice} where bookId={bk.bookId}"
        cursor.execute(sqlQuery)
        con.commit()
        return 'Updated Successfully..'
    except Exception as e:
        print('Error:- ',e)
        return 'Cannot update'

def sort_book():
    try:
        bookslist = []
        sqlQuery = f"select * from book ORDER BY bookCopy"
        cursor.execute(sqlQuery)

        rows = cursor.fetchall()
        for row in rows:
            b = Store(row[0],row[1],row[2],row[3],row[4])
            bookslist.append(b)
        else:
            return bookslist
        con.commit()
    except Exception as e:
         print('Error:- ',e)
