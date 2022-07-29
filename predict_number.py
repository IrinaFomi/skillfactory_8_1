
import numpy as np

def random_predict(number:int=np.random.randint(1,101)) -> int:
    count = 0
    predict_number_list = list(range(1,101))
    while True:
        count+=1
        predict_number = int(np.mean(predict_number_list))
        if number != predict_number:
            if number > predict_number:
                predict_number_list = list(range(predict_number+1,predict_number_list[-1]+1))
            else:
                predict_number_list = list(range(predict_number_list[0],predict_number))
        else:
            break
    return count

def score_of_predict():
    list_results = []
    for i in range(1000):
        list_results.append(random_predict())
    return np.mean(list_results)

print(score_of_predict())
            
                  