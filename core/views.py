from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CoreForm 
import pickle5 as pickle
import numpy as np
import os
def main_view(request):
    if request.method == 'POST':
        pickle_file_path = os.path.join(os.path.dirname(__file__), 'datafile.pickle')

        form = CoreForm(request.POST)
        with open(pickle_file_path, 'rb') as f:
            obj = pickle.load(f)
        # print(list(request.POST.values()))
        val = np.array([float(x) for x in list(request.POST.values())[1:]]).reshape(1,-1)
        answer = obj.predict(val)


        if form.is_valid():
            return render(request, 'mainpage.html', {'form': form,'answer':answer})
    else:
        form = CoreForm()
    return render(request, 'mainpage.html', {'form': form,'answer':0})