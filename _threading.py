from threading import Lock, Thread
from time import sleep

def start_game(preq = []):
    print("Waiting to start game.")

    for t in preq:
        t.join()

    print("Started game")

def load_assets():
    sleep(2)
    print("loaded assets")
    

def load_player():
    sleep(1)
    print("Loaded player")

loaded_assets_thread = Thread(target = load_assets)
loaded_player_thread = Thread(target = load_player)
preq = [loaded_player_thread, loaded_assets_thread]
start_game_thread = Thread(target = start_game, args=(preq,))

#loaded_assets_thread.start()
#loaded_player_thread.start()
#start_game_thread.start()

def print_ran(delay):
    sleep(delay)
    print("ran")

t1 = Thread(target = print_ran, args=(1,))
t2 = Thread(target = print_ran, args=(2,))

t1.start()
t2.start()
t1.join()
t2.join() #always end with .join in case you want to import this file in another file --> that they run until the completion
          #--> to make sure that both threads are executed correctly (file runs completely when imported)







'''def print_values(values, start_lock, end_lock, name):
    for item in values:
        #print(f"{name} waiting for lock!")
        start_lock.acquire()
        print(item)
        end_lock.release()
        


lock1 = Lock()
lock2 = Lock()
lock2.acquire()

thread1 = Thread(target=print_values, args=([1,3,5], lock1, lock2, "t1"))
thread2 = Thread(target=print_values, args=([2,4], lock2, lock1, "t2"))

thread1.start()
thread2.start()'''

