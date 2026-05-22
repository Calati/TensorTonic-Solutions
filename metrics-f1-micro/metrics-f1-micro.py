import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # True positives across all classes
    tp = np.sum(y_true == y_pred)

    # Total number of predictions
    total = len(y_true)

    # FP + FN = 2 * (total - tp)
    fp = total - tp
    fn = total - tp
    denominator = (2 * tp) + fp + fn

    if denominator == 0:
        return 0.0
    return (2 * tp) / denominator

    f1_micro = (2*t_p) / ((2 * t_p) + f_p + f_n)
    return f1_micro
    pass