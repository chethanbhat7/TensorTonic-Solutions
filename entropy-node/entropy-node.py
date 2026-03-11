import numpy as np
import math
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    
    y = np.array(y)

    if len(y) == 0:
        return 0.0
    values, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    
    H = 0
    for i in probs:
        if i > 0:
            H += (i * math.log2(i))
    
    return -H
    pass