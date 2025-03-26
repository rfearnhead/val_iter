import numpy as np

def val_iter(S,A,P,R, iters=1000, gamma = 0.8):
    R = np.array(R)
    P = np.array(P)

    V = np.zeros(((iters+1),len(S))) #initialise empty matrix for values
    pi = np.zeros(len(S),dtype=str) #initialise empty vector for pi 
    for k in range(1,(iters+1)):
        for s in range(0,len(S)):
            Anew = np.zeros(len(A))
            #calculate the values across each possible action
            for a in range(0,len(A)):
                Anew[a] = R[s,a] + gamma*sum(V[k-1]*P[:,s,a])
            V[k,s] = max(Anew)
    
    for s in range(0,len(S)):
        pis = np.zeros(len(A))
        #calculating best policy for each state
        for a in range(0,len(A)):
            pis[a] = R[s,a] + gamma*sum(V[(iters)]*P[:,s,a])
        pimax = np.argmax(pis)
        pi[s] = A[pimax]
        
    #return as a tuple of two lists    
    return(pi.tolist(),V[(iters)].tolist())
