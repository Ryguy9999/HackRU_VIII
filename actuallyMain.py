from threading import Thread
from game import gameFunc
from Queue import Queue
import main

commandsQueue = Queue()
thread1 = Thread(target = main.main, args=(commandsQueue,))
thread1.start()
thread = Thread(target = gameFunc, args=(commandsQueue,))
thread.start()
