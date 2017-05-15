def calcWei(Ns,Nf,Dur):

    # calculate the weight matrix of the nodes in the directed graph using the 
    # information extracted from the file
    
    n = 28 
    # define the number of nodes in the graph
    
    wei = np.zeros((n,n),dtype=float) 
    # initialise the weight matrix
    
    for i in range(len(Dur)):
    
        # allocate the weights to their corresponding position in the weight matrix
        wei[int(Ns[i]),int(Nf[i])] = Dur[i]
    return wei
