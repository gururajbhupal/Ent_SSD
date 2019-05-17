

#Distribute the computing with virtual drives 


# 'calculate_SSD_random' is distributed to each virtual_drive randomly that is on the network 
def calculate_SSD(n):
    import time, socket
    time.sleep(n)
    k = 526 * 769
    k = k + 65891
    k = k - 2773
    k = k/7
    k = k * 247
    k = k + 6675
    k = k - 3551
    k = k/2 

    master = socket.gethostname()
    return (master, n, k)

if __name__ == '__main__':
    import dispy, random
    v_drive = dispy.JobCluster(calculate_SSD, nodes='192.168.1.*') # put your network address here. You need to leave the subnet mask as *
    tasks = []
    for i in range(16):

        task = v_drive.submit(random.randint(0,50))
        task.id = i 
        tasks.append(task)
   
    for task in tasks:
        v_d, n,k = task() # tasks get returned here for results
        print('%s executed job %s at %s with %s result is %s' % (v_d, task.id, task.start_time, n,k))
       
       
    cluster.print_status()
    cluster.close()
