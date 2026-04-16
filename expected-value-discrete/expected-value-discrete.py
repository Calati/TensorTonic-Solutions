import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    
    if np.shape(x) != np.shape(p):
        raise ValueError("shape mismatch")
    elif not np.isclose(np.sum(p), 1, 1e-6):
        raise ValueError("sum of p != 1")
    return np.sum(x*p)
    pass
