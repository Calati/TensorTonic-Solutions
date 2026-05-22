import numpy as np

def entropy_node(y):

    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.array(y)

    # Count occurrences of each class
    _, counts = np.unique(y, return_counts=True)

    # Convert counts to probabilities
    probs = counts / counts.sum()

    # Stable entropy computation: ignore zero probabilities
    entropy = -np.sum(probs * np.log2(probs, where=(probs > 0)))

    return entropy
    pass