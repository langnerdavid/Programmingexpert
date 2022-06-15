from threading import Lock, Thread
#from time import sleep


class WordCounter:
    def __init__(self):
        self.lock = Lock()
        #dict so that every word can be accessed by key
        self.num_of_words = {}
    
    def process_text(self, text):
        words_in_text = text.split(" ")
        self.lock.acquire()
        for word in words_in_text:
            if word in self.num_of_words:
                self.num_of_words[word] += 1
            else:
                self.num_of_words[word] = 1
        self.lock.release()


        
    def get_word_count(self, text):
        self.lock.acquire()
        if text in self.num_of_words:
            self.lock.release()
            return self.num_of_words[text]
        else:
            self.lock.release()
            return 0