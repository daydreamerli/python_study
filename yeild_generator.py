import time

def consumer(name):
    print("%s ready for steam bins!" %name)
    while True:
       baozi = yield

       print("Steam bin [%s] is coming,eaten by [%s]!" %(baozi,name))

c = consumer("Carrie")
c.__next__()

b1= "pork celery"
c.send(b1)
c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("Frank has started to make steam bins!")
    for i in range(10):
        time.sleep(1)
        print("One done,cut in half!")
        c.send(i)
        c2.send(i)

producer("frank")
