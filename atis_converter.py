# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:46:35 2021
@author: isi
"""
import re
from collections import defaultdict 

def transform_l(l1, l2):
    for s in l2[:]:
        if s.startswith('I-'):
            i=l2.index(s)
            l2.remove(s)
            l1[i-1:i+1]=[' '.join(l1[i-1:i+1])]
    
    labels={'B-aircraft_code':'{"entity": "aircraft"}',
            'B-airline_code':'{"entity": "airline"}',
            'B-airline_name':'{"entity": "airline"}',
            'B-airport_code':'{"entity": "airport"}',
            'B-airport_name':'{"entity": "airport"}',
            'B-arrive_date.date_relative':'{"entity": "date", "role": "arrival"}',
            'B-arrive_date.day_name':'{"entity": "date", "role": "arrival"}',
            'B-arrive_date.day_number':'{"entity": "date", "role": "arrival"}',
            'B-arrive_date.month_name':'{"entity": "date", "role": "arrival"}',
            'B-arrive_date.today_relative':'{"entity": "date", "role": "arrival"}',
            'B-arrive_time.end_time':'{"entity": "time", "role": "arrival"}',
            'B-arrive_time.period_mod':'{"entity": "time", "role": "arrival"}',
            'B-arrive_time.period_of_day':'{"entity": "time", "role": "arrival"}',
            'B-arrive_time.start_time':'{"entity": "time", "role": "arrival"}',
            'B-arrive_time.time':'{"entity": "time", "role": "arrival"}',
            'B-arrive_time.time_relative':'{"entity": "time", "role": "arrival"}',
            'B-booking_class':'{"entity": "booking", "role": "class"}',
            'B-city_name':'{"entity": "location"}',
            'B-class_type':'{"entity": "booking", "role": "class"}',
            'B-compartment':'{"entity": "booking", "role": "compartment"}',
            'B-connect':'{"entity": "booking", "role": "connect"}',
            'B-cost_relative':'{"entity": "cost"}',
            'B-day_name':'{"entity": "date"}',
            'B-day_number':'{"entity": "date"}',
            'B-days_code':'{"entity": "date"}',
            'B-depart_date.date_relative':'{"entity": "date", "role": "departure"}',
            'B-depart_date.day_name':'{"entity": "date", "role": "departure"}',
            'B-depart_date.day_number':'{"entity": "date", "role": "departure"}',
            'B-depart_date.month_name':'{"entity": "date", "role": "departure"}',
            'B-depart_date.today_relative':'{"entity": "date", "role": "departure"}',
            'B-depart_date.year':'{"entity": "date", "role": "departure"}',
            'B-depart_time.end_time':'{"entity": "time", "role": "departure"}',
            'B-depart_time.period_mod':'{"entity": "time", "role": "departure"}',
            'B-depart_time.period_of_day':'{"entity": "time", "role": "departure"}',
            'B-depart_time.start_time':'{"entity": "time", "role": "departure"}',
            'B-depart_time.time':'{"entity": "time", "role": "departure"}',
            'B-depart_time.time_relative':'{"entity": "time", "role": "departure"}',
            'B-economy':'{"entity": "cost", "role": "budget"}',
            'B-fare_amount':'{"entity": "cost", "role": "amount"}',
            'B-fare_basis_code':'{"entity": "cost"}',
            'B-flight_days':'{"entity": "flight"}',
            'B-flight_mod':'{"entity": "flight"}',
            'B-flight_number':'{"entity": "flight"}',
            'B-flight_stop':'{"entity": "flight"}',
            'B-flight_time':'{"entity": "flight"}',
            'B-fromloc.airport_code':'{"entity": "airport", "role": "from"}',
            'B-fromloc.airport_name':'{"entity": "airport", "role": "from"}',
            'B-fromloc.city_name':'{"entity": "location", "role": "from"}',
            'B-fromloc.state_code':'{"entity": "location", "role": "from"}',
            'B-fromloc.state_name':'{"entity": "location", "role": "from"}',
            'B-meal':'{"entity": "meal"}',
            'B-meal_code':'{"entity": "meal"}',
            'B-meal_description':'{"entity": "meal"}',
            'B-month_name':'{"entity": "date"}',
            'B-or':'{"entity": "booking", "role": "or"}',
            'B-period_of_day':'{"entity": "time"}',
            'B-return_date.date_relative':'{"entity": "date", "role": "return"}',
            'B-return_date.day_name':'{"entity": "date", "role": "return"}',
            'B-return_date.day_number':'{"entity": "date", "role": "return"}',
            'B-return_date.month_name':'{"entity": "date", "role": "return"}',
            'B-return_date.today_relative':'{"entity": "date", "role": "return"}',
            'B-return_time.period_mod':'{"entity": "time", "role": "return"}',
            'B-return_time.period_of_day':'{"entity": "time", "role": "return"}',
            'B-round_trip':'{"entity": "booking", "role": "round-trip"}',
            'B-state_code':'{"entity": "location"}',
            'B-state_name':'{"entity": "location"}',
            'B-stoploc.airport_code':'{"entity": "airport", "role": "connect"}',
            'B-stoploc.airport_name':'{"entity": "airport", "role": "connect"}',
            'B-stoploc.city_name':'{"entity": "location", "role": "connect"}',
            'B-stoploc.state_code':'{"entity": "location", "role": "connect"}',
            'B-time':'{"entity": "time"}',
            'B-time_relative':'{"entity": "time"}',
            'B-today_relative':'{"entity": "time"}',
            'B-toloc.airport_code':'{"entity": "airport", "role": "to"}',
            'B-toloc.airport_name':'{"entity": "airport", "role": "to"}',
            'B-toloc.city_name':'{"entity": "location", "role": "to"}',
            'B-toloc.country_name':'{"entity": "location", "role": "to"}',
            'B-toloc.state_code':'{"entity": "location", "role": "to"}',
            'B-toloc.state_name':'{"entity": "location", "role": "to"}',
            'B-transport_type':'{"entity": "transport"}'
            }
    for s in l2:
        if s in labels:
            i=l2.index(s)
            l2[i]= '0'
            l1[i]='[{}]'.format(l1[i])
            l1[i]=l1[i] + labels.get(s)
    s = '    - ' + ' '.join(l1[1:-1])
    return(s)

intents = defaultdict(list)
with open("\ICE-ATIS\ice_atis.train.w-intent.iob","r",encoding="utf8") as file:
    for l in file.readlines():
        l1=list(l.split())
        i=l1.index('EOS')
        l2=l1[i+1:]
        l1=l1[0:i+1]
        intents[l2[-1]].append(transform_l(l1,l2))
#print(intents)
with open("nlu.yml","w",encoding="utf8") as wfile:
    wfile.write('version: "2.0"\n\nnlu:\n')
    for k,v in intents.items():
        s='- intent: ' + k + '\n  examples: |\n'
        wfile.write(s)
        for s in v:
            wfile.write(s)
            wfile.write('\n')
        wfile.write('\n')
        
