import  random,sys,dispy,time

#node class
class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
#insert 
def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


def make_tree_and_return_root(arr):
    r=Node(arr[0])
    for i in range(1,arr.__len__()):
        binary_insert(r, Node(arr[i]))
    
    return r

#search
def search_tree(root,ele):
    print "root is: "+str(root.data)
    if root.data==ele :
        print "Element found:"+str(root.data)
    elif root.data>ele:
        print "left "
        if root.l_child!=None:
            search_tree(root.l_child, ele)
        else:print "not found"
    elif root.data<ele:
        print "right "
        if root.r_child!=None:
            search_tree(root.r_child, ele)
        else:print "not found"


#for dividing list
def divide_list(lst, n):
    return [lst[i::n] for i in range(n)]


#tree


if __name__ == '__main__':
    
    arr=[]
    nodes=[]
    n=int(raw_input("Enter the total size of elements : "))
    for i in range(0,n):
        #sys.maxint
        temp=random.randrange(1,100)
        arr.append(temp)
   
    #initializing the nodes dynamically
    '''while True:
        temp=raw_input("Enter the node ip or ok to initialize :")
        if temp=="ok":
            break
        else:
            nodes.append(temp) '''
    
    #make cluster now
    nodes=["192.168.1.102","192.168.1.104"]
    cluster = dispy.JobCluster(search_tree,nodes,depends=[Node])
    cluster.stats()
    #making trees according to the nodes
    n=nodes.__len__()
    z=divide_list(arr, n)
    print z
    #dynamic b trees list
    bst_lst=[]
    for array in z:
        bst_lst.append(make_tree_and_return_root(array))
    #bst_lst stores the roots of binary trees
    
    elementToSearch=int(input("Enter the element to be searched: "))
    
    #search_tree(bst_lst[0], elementToSearch)
    
    
    
    
    
    
    
    # now time to submit the jobs and get the element 
    jobs = []
    for i in range(n):
        job = cluster.submit_node(nodes[i],bst_lst[i],elementToSearch)
        job.id = nodes[i]
        jobs.append(job)
        
    for job in jobs:
        job()
        if job.status != dispy.DispyJob.Finished:
            print('job %s failed: %s' % (job.id, job.exception))
        else:
            print('%s: %s :output: %s' % (job.id, job.result,job.stdout))
        
    cluster.print_status()
    cluster.close()

        
    
    
    
    
    
    
    
    
    

    
