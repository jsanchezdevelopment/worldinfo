from django.shortcuts import render
from mysql_queries import q_continents, q_countries
from do_Query import do_Query
import json

# Create your views here.

class vars:
  continents = ''
  countries = ''


def app1_view(request):
  
  if 'continent' in request.GET:
    s_continent = request.GET['continent']
  else:
    s_continent = "Select Continent"

  if not vars.continents:
    print('get continents')
    vars.continents = do_Query(q_continents)
    vars.continents.sort()

  if not vars.countries:
    print('get countries')
    vars.countries = do_Query(q_countries)
    
  j_countries = json.dumps(vars.countries)

  return render(request, 'app1.html', {'continents':vars.continents, 'j_countries':j_countries,'s_continent':s_continent})

