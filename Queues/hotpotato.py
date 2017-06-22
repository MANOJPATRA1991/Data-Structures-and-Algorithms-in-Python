from Queues.queue import Queue

def hotPotato(namelist, num):
    simQueue=Queue()
    for name in namelist:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()

    return simQueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
