from flask import Flask,render_template,request,redirect
from database import *
app = Flask(__name__)


@app.route('/')
def index():
    blist = showallbook()
    return render_template("index.html",booklist=blist)

@app.route('/savebook',methods=['POST'])
def savebook():
    if request.method=='POST':
       
        id = int(request.form['bookId'])
        name = request.form['bookName']
        author = request.form['bookAuthor']
        copies = int(request.form['bookCopy'])
        price = float(request.form['bookPrice'])

        bk = Store(id,name,author,copies,price)  

        msg = insertbook(bk)
        blist = showallbook()
        print(msg)
        return render_template('index.html',message=msg,booklist=blist)

@app.route('/showbook')
def showbook():
    blist = showallbook()
    return render_template('booklist.html',booklist=blist)

@app.route('/deletebook/<int:bookId>')
def deletebook(bookId):
    delete_book(bookId)
    return redirect('/')

@app.route('/editbook/<int:bookId>')
def editbook(bookId):
    bk = get_book_byid(bookId)
    return render_template('update.html',book=bk)

@app.route('/updatebook',methods=['POST'])
def updatebook():
    if request.method=='POST':
        id = int(request.form['bookId'])
        name = request.form['bookName']
        author = request.form['bookAuthor']
        copies = int(request.form['bookCopy'])
        price = float(request.form['bookPrice'])

        bk = Store(id,name,author,copies,price) 
        
        update_book(bk)
        return redirect('/')

@app.route('/sortbook')
def sortbook():
    bklist = sort_book()
    return render_template('sortbook.html',bookslist=bklist)




if __name__=='__main__':
    app.run(debug=True,port=8080)