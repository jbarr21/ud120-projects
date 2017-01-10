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
print type(enron_data), enron_data

for name in sorted(enron_data):
    print '    %s' % name

person_data = enron_data['METTS MARK']
print type(person_data), person_data

for feature in sorted(person_data):
    print '    %s' % feature

print '\n'

print 'num people: %d' % len(enron_data)
print 'num features: %d' % len(person_data)

poi_data = {name: person_data for name, person_data in enron_data.iteritems() if person_data['poi'] == 1}
print 'num POIs: %d' % len(poi_data)

print 'James Prentice stock value = $%d' % enron_data['PRENTICE JAMES']['total_stock_value']

print 'Wesley Colwell sent %d messages to POIs' % enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'Jeff Skilling exercised %d in stock options' % enron_data['SKILLING JEFFREY K']['exercised_stock_options']

for name in ['FASTOW ANDREW S', 'LAY KENNETH L', 'SKILLING JEFFREY K']:
    print '%s total payments were: %d' % (name, enron_data[name]['total_payments'])

print 'num with known salary: %d' % len({name: person_data for name, person_data in enron_data.iteritems() if person_data['salary'] != 'NaN'})

print 'num with known email: %d' % len({name: person_data for name, person_data in enron_data.iteritems() if person_data['email_address'] != 'NaN'})

# with pandas

import pandas as pd

df = pd.DataFrame(enron_data)
print '\n********** with pandas **********\n'

print 'num people: %d' % df.shape[1]
print 'num features: %d' % df.shape[0]
print 'num POIs: %d' % df.ix['poi'].value_counts()[True]
print 'James Prentice stock value = $%d' % df['PRENTICE JAMES']['total_stock_value']
print 'Wesley Colwell sent %d messages to POIs' % df['COLWELL WESLEY']['from_this_person_to_poi']
print 'Jeff Skilling exercised %d in stock options' % df['SKILLING JEFFREY K']['exercised_stock_options']
print 'person with most payments: %s' % df.ix['total_payments', ['FASTOW ANDREW S', 'LAY KENNETH L', 'SKILLING JEFFREY K']].idxmax()
print 'num with known salary: %d' % df.ix['salary'].value_counts()['NaN']
print 'num with known email: %d' % df.ix['email_address'].value_counts()['NaN']
print 'percent with unknown payments: %.1f%%' % (df.ix['total_payments'].value_counts()['NaN'] / float(df.shape[1]) * 100)
print 'percent POIs with unknown payments: %.1f%%' % len(df.T.ix[df.T['poi'] & (df.T['total_payments'] == 'NaN')])

df_no_total = df.fillna(0)
df_no_total = df_no_total.drop('TOTAL', axis=1)

salaries = df_no_total.ix['salary']
print 'max salary: %s' % salaries.idxmax()

stock_options = df_no_total.ix['exercised_stock_options']
print 'max stock options = %d (%s)' % (stock_options[stock_options.idxmax()], stock_options.idxmax())
print 'min stock options = %d (%s)' % (stock_options[stock_options.idxmin()], stock_options.idxmin())

print 'max salary = %d (%s)' % (salaries[salaries.idxmax()], salaries.idxmax())
print 'min salary = %d (%s)' % (salaries[salaries.idxmin()], salaries.idxmin())
