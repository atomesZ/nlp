def find_wrong_class(x_pred: list, y_pred: list, y_true: list, nb_samples: int = None) -> list:
    """
    Find wrong classification of samples in x_pred based on y_pred prediction
    
    Parameters
    ----------
    x_pred : list
        A list of samples
        
    y_pred : list
        A list of predicted labels
        
    y_true : list 
        A list of the true labels
        
    nb_samples : list
        The max number of samples to extract (could be less if not enough in provided samples)

    Returns
    -------
    list[str, int]
        A list of the wrongly classified samples along with their prediction
    """
    wrongly_classified: list = []
    count_sample: int = 0
    
    for i in range(len(y_pred)):
        if nb_samples is not None and count_sample == nb_samples:
            break
        
        if y_pred[i] != y_true[i]:
            wrongly_classified.append((x_pred[i], y_pred[i]))
            count_sample += 1
            
    return wrongly_classified