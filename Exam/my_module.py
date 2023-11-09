import numpy as np
from random import choices


def conf95_interval(sample, iter):

    """
    Bootstrap the 95% confidence interval for the mean of the data.
    
    Parameters:
    - sample: An array of data
    - iter: The number of bootstrap samples to generate
    
    Returns:
    - A tuple representing the lower and upper bounds of the 95% confidence interval
    """

    means = [np.mean(choices(sample, k= len(sample))) for i in range(iter)]

    lower_bound = np.percentile(means, 2.5)
    upper_bound = np.percentile(means, 97.5)

    return (lower_bound, upper_bound)
