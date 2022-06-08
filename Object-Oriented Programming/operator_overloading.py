class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number

    # +
    def __add__(self, other):
        new_words = self.words + " " + other.words
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)


page1 = Page("Tim is a very good instructor!", 1)
page2 = Page("This is another page.", 2)
page3 = page1 + page2
print(page3.words, page3.page_number)