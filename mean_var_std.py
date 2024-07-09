import numpy as np

def calculate(list):
    # checking for list length
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # list to matrix conversion
    matrix = np.array(list).reshape(3,3)

    # creating dictionary for results
    calculations = {
        'mean': [],
        'variance': [],
        'standart deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    # calculations for columns (axis 0)
    calculations['mean'].append(np.mean(matrix, axis=0).tolist())
    calculations['variance'].append(np.var(matrix, axis=0).tolist())
    calculations['standart deviation'].append(np.std(matrix, axis=0).tolist())
    calculations['max'].append(np.max(matrix, axis=0).tolist())
    calculations['min'].append(np.min(matrix, axis=0).tolist())
    calculations['sum'].append(np.sum(matrix, axis=0).tolist())

    # calculations for rows (axis 1)
    calculations['mean'].append(np.mean(matrix, axis=1).tolist())
    calculations['variance'].append(np.var(matrix, axis=1).tolist())
    calculations['standart deviation'].append(np.std(matrix, axis=1).tolist())
    calculations['max'].append(np.max(matrix, axis=1).tolist())
    calculations['min'].append(np.min(matrix, axis=1).tolist())
    calculations['sum'].append(np.sum(matrix, axis=1).tolist())

    # calculations for flattened matrix
    calculations['mean'].append(np.mean(matrix).tolist())
    calculations['variance'].append(np.var(matrix).tolist())
    calculations['standart deviation'].append(np.std(matrix).tolist())
    calculations['max'].append(np.max(matrix).tolist())
    calculations['min'].append(np.min(matrix).tolist())
    calculations['sum'].append(np.sum(matrix).tolist())

    return calculations

#result = calculate([0,1,2,3,4,5,6,7,8])
#print(result)