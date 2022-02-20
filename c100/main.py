class Book(object):
    def __init__(self, author, pages, title, price, stock, ratingAvg):
        self.author = author
        self.pages = pages
        self.title = title
        self.price = price
        self.stock = stock
        self.ratingAvg = ratingAvg

    def stockIncrease(self, xBooks):
        self.stock += xBooks
        print('This is the stock: '+str(self.stock))

    def stockDecrease(self, xBooks):
        self.stock -= xBooks
        print('This is the stock: '+str(self.stock))

    def bookInfo(self):
        print('This book is ' + self.title + ' by ' + self.author + '.')
        print('It also has' + self.pages + ' pages.')
        print('It costs £' + str(self.price) + '.')

    def bookReview(self, rating):
        self.ratingAvg = (rating+self.ratingAvg)/2
