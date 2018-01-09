"""
Definition of views.
"""

from django.shortcuts import render
from _io import StringIO
from django.http import HttpRequest
from datetime import datetime
from django.http import HttpResponseRedirect

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
        return HttpResponseRedirect('imageTypeConverter')
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageTypeConverter.html',
		    {
			    'title':'Konwerter plików graficznych',
                'year':datetime.now().year,
		    })
