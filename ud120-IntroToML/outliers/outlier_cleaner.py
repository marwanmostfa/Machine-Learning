#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    preCleaned=[]
    diff=[]
    for i in range(90):
        diff.append(predictions[i]-net_worths[i])
        tup=(ages[i],net_worths[i],predictions[i]-net_worths[i])
        preCleaned.append(tup)
    diff.sort(reverse=True)
    th=diff[8]
    for item in preCleaned:
        if item[2]<th:
            cleaned_data.append(item)

    
    return cleaned_data

