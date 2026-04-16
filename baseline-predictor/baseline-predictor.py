import numpy as np

def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    # Write code here
    ratings_matrix = np.array(ratings_matrix)
    
    mask = (ratings_matrix!=0)
    global_mu = np.sum(ratings_matrix[mask])/np.sum(mask)
    
    # User means
    user_sum = np.sum(ratings_matrix, axis=1)
    user_count = np.sum(mask, axis=1)
    user_mean = np.divide(user_sum, user_count, out=np.zeros_like(user_sum, dtype=float), where=user_count!=0)
    
    # Item means
    item_sum = np.sum(ratings_matrix, axis=0)
    item_count = np.sum(mask, axis=0)
    item_mean = np.divide(item_sum, item_count, out=np.zeros_like(item_sum, dtype=float), where=item_count!=0)
    
    # Biases
    user_bias = user_mean - global_mu
    item_bias = item_mean - global_mu

    predictions = []
    for user,item in target_pairs:
        pred = global_mu + user_bias[user] + item_bias[item]
        predictions.append(float(pred))
    
    return predictions
        