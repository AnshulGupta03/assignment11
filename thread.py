#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
import time

class Mythread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(5)
        print("hello",self.name)

t1 = Mythread("thread 1")
t1.start()

print("\n\n",10*"*")



#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between.

import time
import threading

class Threads(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1,11):
            print(i)
            time.sleep(1)
        

t1 = Threads()
t1.start()


print("\n\n",10*"*")



#Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements
#of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec

import time
import threading

class Threads1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        delay = 2
        for i in list1:
            time.sleep(delay)
            print(i)
            delay += 2
        

list1=[5,6,3,22,9]

t1 = Threads1()
t1.start()


print("\n\n",10*"*")


#Q4. Call factorial function using thread.


import threading

class Threads(threading.Thread):
    def __init__(self,x):
        threading.Thread.__init__(self)
        self.x = x

    def fact(self,num):
        if (num == 1):
            return 1
        else:
            return (num*self.fact(num-1))

    def run(self):
        result = self.fact(self.x)
        print("factorial of %d is %d"%(self.x,result))
        
        
x = int(input("enter the number:"))
t1 = Threads(x)
t1.start()



print("\n\n",10*"*")
