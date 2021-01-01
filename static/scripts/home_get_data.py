#!/usr/bin/python

from do_Query import do_Query
from mysql_queries import q_continent_country_count, q_continent_pop

DEBUG = False

def home_get_data():
  data1 = do_Query(q_continent_country_count)
  data2 = do_Query(q_continent_pop)
  if DEBUG:
    print()
  # the population total is returned in the python "Decimal(x)" format
  # convert it to int so it can be used by the chart  
  for row in data2:
    row[1] = int(row[1])
    if DEBUG:
      print(row)
  
  return data1,data2

if __name__ == "__main__":
    home_get_data()
