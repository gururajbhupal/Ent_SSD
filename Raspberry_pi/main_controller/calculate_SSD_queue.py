

#Distribute the computing wit virtual drives


#The below code implemets a queue structre to distribute tasks in queues. 
#Three queus are 
#1. Internal Queue 
#2. Specific Queue
#3. Generic Queue

# 'calculate_SSD_equal_Share' is distributed to each virtual_drive in an equal fashion on the network
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
    self_ip = '192.168.1.10' #ip of the main controller
    ip = ['192.168.1.100' , '192.168.1.101', '192.168.1.102','192.168.1.103','192.168.1.104','192.168.1.105','192.168.1.106','192.168.1.107'] #ip of all the virtual drives
    priority = [1,3,1,2,1,3,1,2,2,1,2,3,1,2,3,3] # list of priorities of the tasks
    disk = [1,5,1,8,5,5,7,3,4,4,7,3,3,6,5,2] # list of the disk which contains the data that needed to be processed.
if __name__ == '__main__':
    import dispy, random
    v_drive = dispy.JobCluster(calculate_SSD, '192.168.1.100' , '192.168.1.101', '192.168.1.102','192.168.1.103','192.168.1.104','192.168.1.105','192.168.1.106','192.168.1.107') # list ip of all virtual drives here
    tasks = []
    for i in range(16):
        if priorrityp[i] = 1:
            task = v_drive.submit_node(self_ip,random.randint(0,200)) # high priority so controller will process it itself

        elseif priority[i] == 2:
            task = v_drive.submit_node(ip[disk[i]],random.randint(0,200)) # medium priority so the virtual drive containing the data can process it. 

        else:
            task = v_drive.submit(random.randint(0,200)) # low priority so it is put in a generic queeu with greedy algorithm.

        
        task.id = i 
        tasks.append(task)
   
    for task in tasks:
        v_d, n,k = task() # tasks get returned here for results
        print('%s executed job %s at %s with %s result is %s' % (v_d, task.id, task.start_time, n,k))
       
       
    cluster.print_status()
    cluster.close()
