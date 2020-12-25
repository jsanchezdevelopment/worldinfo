from django.shortcuts import render
from home_get_data import home_get_data

def index(request):

  data1,data2 = home_get_data()
  
  return render(request, 'main_template.html', {'data1':data1, 'data2':data2})
