import threading,logging

start=0
end=100
def oddNumbers(start,end):
    for i in range(start,end+1):
        if i%2!=0:
            print("Odd=>",i,end=" ")

def evenNumbers(start,end):
    for i in range(start, end):
        if i%2==0:
            print("Even=>",i,end=" ")

try:
    t1=threading.Thread(target=oddNumbers,args=(start,end)) # create a thread
    t2=threading.Thread(target=evenNumbers,args=(start,end)) # create a thread

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
except:
    logging.error("Wrong Input")
finally:
    print("Completed!")
