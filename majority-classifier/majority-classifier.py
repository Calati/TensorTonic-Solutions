import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    
    values, counts = np.unique(y_train, return_counts=True)
    majority_label = values[np.argmax(counts)]
    return [majority_label] * len(X_test)
    
    pass