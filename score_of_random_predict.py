import numpy as np
from predict_number import random_predict


def score_of_predict():
    """Score of random predict function :func:`~predict_number.random_predict`

    Returns:
        float: mean of 1000 calls of random_predict function
    """
    list_results = []
    
    for i in range(1000):
        list_results.append(random_predict(np.random.randint(1,101))) 
    return [min(list_results),np.mean(list_results),max(list_results)]


if __name__ == "__main__":
    # RUN
    result_score_func = score_of_predict()
    print(f'Min = {result_score_func[0]}, mean = {result_score_func[1]}, \
max = {result_score_func[2]}.')