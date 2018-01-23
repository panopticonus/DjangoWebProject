"""
Definition of views.
"""

from django.shortcuts import render
from _io import StringIO
from django.http import HttpRequest
from datetime import datetime
from django.http import HttpResponseRedirect
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
	)

def imageTypeConverter(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')
        form= request.POST.get('fileFormat')
                
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()
        name = request.POST.get('fname')

        print(file_path)
        img = Image.open(item)
        nazwa=file_path+"/"+name+"."+form
        img.save(nazwa)

        return HttpResponseRedirect('imageTypeConverter')
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageTypeConverter.html',
		    {
			    'title':'Konwerter plików graficznych',
                'year':datetime.now().year,
		    })
