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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### Number of people in dataset

print "Number of people in dataset:", len(enron_data)

### Number of features for one person

print "Number of features for one person:", len(enron_data["SKILLING JEFFREY K"])

### Number of people with poi == 1

num_of_poi = 0
for feature in enron_data.itervalues():
	if feature["poi"] == 1:
		num_of_poi += 1
print "Number of people with poi == 1: ", num_of_poi

### Total value of the stock belonging to James Prentice

print "Total value of the stock belonging to James Prentice:", enron_data["Prentice James".upper()]["total_stock_value"]

### all features available for one person

for feature in enron_data["Prentice James".upper()].keys():
    print feature

### Number of email messages from Wesley Colwell to persons of interest

print "Number of email messages from Wesley Colwell to persons of interest: ", enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"]

### Value of stock options exercised by Jeffrey Skilling:

print "Value of stock options exercised by Jeffrey Skilling:", enron_data["Skilling Jeffrey K".upper()]["exercised_stock_options"] 













