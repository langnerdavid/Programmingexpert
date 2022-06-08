class Page:
    def __init__(self, text, page_number):
        self.text = text
        self.page_number = page_number

    def __len__(self):
        return len(self.text)

    #string representation
    def __str__(self):
        return f"Page (text = {self.text}, page_number = {self.page_number})"

    #internal representation (all important information for debugging)
    def __repr__(self):
        return self.__str__()

class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number

    def __len__(self):
        return len(self.pages)

    #string representation
    def __str__(self):
        output =  f"Book ({self.title}, {self.author}, {self.id_number})"
        
        for page in self.pages:
            output += "\n" + str(page)

        return output

    #internal representation (all important information for debugging)
    def __repr__(self):
        return f"Book (id_number = {self.id_number})"

page1 = Page("Page 1!", 1)
page2 = Page("This is page 2.!", 2)
book = Book("Tim is Great", "Tim", [page1, page2], 1)
#print(page1)
print(book)
