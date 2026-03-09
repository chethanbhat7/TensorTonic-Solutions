import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x=np.array(x)
    p=np.array(p)
    Ex=0
    p_sum=0
    for i in p:
        p_sum+=i
    for i in range(len(x)):
      Ex+=(x[i]*p[i])  
    if p_sum!=1:
        raise ValueError("Error")
    else:
        return Ex
    pass
