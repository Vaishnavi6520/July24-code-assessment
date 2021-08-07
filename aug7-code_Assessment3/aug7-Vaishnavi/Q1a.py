import multiprocessing,logging
start,end=0,100
# print("Odd numbers")
def oddNumbers(start,end):
    for i in range(start,end+1):
        if i%2!=0:
            print("Odd=>",i,end=" ")
# print("Even numbers")
def evenNumber(start,end):
    for i in range(start, end):
        if i%2==0:
            print("Even=>",i,end=" ")
if __name__=='__main__':
    try:
        t1=multiprocessing.Process(target=oddNumbers,args=(start,end)) # create a thread
        t2=multiprocessing.Process(target=evenNumber,args=(start,end)) # create a thread

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("Done!")
    except:
        logging.error("Wrong Input")
    finally:
        print("Complete Successfully")