#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
#printing number of persons in data
print(len(enron_data.keys()))

#printing how many POIs exist
poi_count=0
for person in enron_data:
    if enron_data[person]["poi"]==1:
        if enron_data[person]["total_payments"]=='NaN':
            poi_count +=1
        
        
print("num:" +str(poi_count))
print(21/146)
#for i in enron_data:
#    print(enron_data[i])

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print(enron_data["SKILLING JEFFREY K"]["total_payments"])

print(enron_data["LAY KENNETH L"]["total_payments"])

print(enron_data["FASTOW ANDREW S"]["total_payments"])


