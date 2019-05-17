

#Distribute the computing wit virtual drives


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
    ip = ['192.168.1.100' , '192.168.1.101', '192.168.1.102','192.168.1.103','192.168.1.104','192.168.1.105','192.168.1.106','192.168.1.107']
if __name__ == '__main__':
    import dispy, random
    v_drive = dispy.JobCluster(calculate_SSD, '192.168.1.100' , '192.168.1.101', '192.168.1.102','192.168.1.103','192.168.1.104','192.168.1.105','192.168.1.106','192.168.1.107') # list ip of all virtual drives here
    tasks = []
    for i in range(16):

        task = v_drive.submit_node(ip[i%8],random.randint(0,200))
        task.id = i 
        tasks.append(task)
   
    for task in tasks:
        v_d, n,k = task() # tasks get returned here for results
        print('%s executed job %s at %s with %s result is %s' % (v_d, task.id, task.start_time, n,k))
       
       
    cluster.print_status()
    cluster.close()
