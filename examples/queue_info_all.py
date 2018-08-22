from pythonlsf import lsf

def queryQueueInfoAll():
    """
    "Query all queue info"
    """
    if lsf.lsb_init("queryQueueInfoAll") > 0:
        return -1;
    
    for queue_info in lsf.get_all_queue_info():
        print "queue: {0}, description: {1}, priority: {2}, nice: {3}".format(queue_info.queue, 
            queue_info.description, queue_info.priority, queue_info.nice)

    return 0;

if __name__ == '__main__':
    queryQueueInfoAll();
