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
    cleaned_data = [(ages[i], net_worths[i], predictions[i] - net_worths[i]) for i in range(0, len(predictions))]
    cleaned_data = sorted(cleaned_data, key=lambda data: data[2])[0:int(.9 * len(predictions))]

    return cleaned_data
