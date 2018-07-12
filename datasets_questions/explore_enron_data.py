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
import os
# import sys

homedir = os.getcwd()

print "homedir -> " + homedir
# print "sys path -> " + sys.path

enron_data = pickle.load(open(homedir + "/final_project/final_project_dataset.pkl", "r"))

print

print "number of person in enron_data -> " + str(len(enron_data))

print

print "all keys -> " + str(enron_data.keys())

print

print "number of features of a person -> " + str(len(enron_data.get(enron_data.keys()[0])))

print

poi = []

for i in enron_data.keys():
    if enron_data[i]["poi"] == 1:
        poi.append(i)

print "number of poi -> " + str(len(poi)) + "\n poi name is -> " + str(poi)

print

print "total value of the stock belonging to James Prentice -> " + str(enron_data['PRENTICE JAMES']['total_stock_value'])

print

print "email from_this_person_to_poi COLWELL WESLEY -> " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print

print "SKILLING JEFFREY K exercised_stock_options -> " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

print

print "max total payment -> " + str(max(enron_data.values(), key=lambda x: x['total_payments']))

print

print "non-nan salary-> " + str(len(filter(lambda x: x['salary'] != 'NaN', enron_data.values())))

print

print "non-nan email -> " + str(len(filter(lambda x: x['email_address'] != 'NaN', enron_data.values())))

print

print "number of NaN total payments -> " + str(len(filter(lambda x: x['total_payments'] == 'NaN', enron_data.values())))
