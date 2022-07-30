
import numpy as np

def random_predict(number:int=np.random.randint(1,101)) -> int:
    """Guess the number, that passed in argumet.

    Args:
        number (int, optional): guessed number. Defaults to np.random.randint(1,101).

    Returns:
        int: the number of attempts when the number was guessed
    """
    count = 0
    left_border = 1
    right_border = 100
    
    if number<left_border or number>right_border:
        raise ValueError(f'Incorrect argument. Must be between [{left_border},{right_border}]')
    
    while True:
        count+=1
        predict_number = int((left_border+right_border)/2)
        if number != predict_number:
            if number > predict_number:
                left_border = predict_number + 1
            else:
                right_border = predict_number - 1
        else:
            break
        
    return count

            
                  