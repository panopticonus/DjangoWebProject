"""
Definition of views.
"""

from django.shortcuts import render
from io import BytesIO
from django.http import HttpRequest
from datetime import datetime
from django.http import HttpResponseRedirect
from PIL import Image
import os
from PIL import ImageFilter
from django.http import HttpResponse
import base64
from PIL import ImageOps
from PIL import ImageEnhance

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Obróbka plików graficznych',
            'year':datetime.now().year,
        }
	)

def imageTypeConverter(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')
        format = request.POST.get('fileFormat')               
        name = request.POST.get('fname')

        img = Image.open(item)

        output = BytesIO()
        img.save(output, format='JPEG')
        im_data = output.getvalue()
        data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

        return render(request, "app/imageSizeConverter.html", 
                      {
                          'title':'Konwerter plików graficznych',
                          'year':datetime.now().year,
                          'image': data_url,
                          'fileName' : name + '.' + format,
                          'aText' : 'Pobierz plik wynikowy',
                          'labelText' : 'Obraz wynikowy: '
                      })       
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageTypeConverter.html',
		    {
			    'title':'Konwerter plików graficznych',
                'year':datetime.now().year,
		    })

def imageSizeConverter(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')

        width = int(request.POST.get('width'))
        height = int(request.POST.get('height'))

        proportion = request.POST.get('proportion')          

        name = request.POST.get('fname')

        img = Image.open(item)

        if(proportion == 'on'):
            img.thumbnail((width, height))
        else:
            img.resize((width, height))

        resultFileName, file_extension = os.path.splitext(name)

        if not file_extension:
            filename, file_extension = os.path.splitext(item.name)

        output = BytesIO()
        img.save(output, format='JPEG')
        im_data = output.getvalue()
        data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

        return render(request, "app/imageSizeConverter.html", 
                      {
                          'title':'Zmiana rozmiaru',
                          'year':datetime.now().year,
                          'image': data_url,
                          'fileName' : resultFileName + file_extension,
                          'aText' : 'Pobierz plik wynikowy',
                          'labelText' : 'Obraz wynikowy: '
                      })       
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageSizeConverter.html',
		    {
			    'title':'Zmiana rozmiaru',
                'year':datetime.now().year,
		    })

def imageAddFilter(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')
               
        name = request.POST.get('fname')

        img = Image.open(item)

        filterForm = request.POST.get('filter')

        def filterName(x):
            return {
                'BLUR' : ImageFilter.BLUR,
                'CONTOUR' : ImageFilter.CONTOUR,
                'DETAIL' : ImageFilter.DETAIL,
                'EDGE_ENHANCE' : ImageFilter.EDGE_ENHANCE,
                'EDGE_ENHANCE_MORE' : ImageFilter.EDGE_ENHANCE_MORE,
                'EMBOSS' : ImageFilter.EMBOSS,
                'FIND_EDGES' : ImageFilter.FIND_EDGES,
                'SMOOTH' : ImageFilter.SMOOTH,
                'SMOOTH_MORE' : ImageFilter.SMOOTH_MORE,
                'SHARPEN' : ImageFilter.SHARPEN
                }[x]

        zmienna = img.filter(filterName(filterForm))
        
        resultFileName, file_extension = os.path.splitext(name)

        if not file_extension:
            filename, file_extension = os.path.splitext(item.name)

        output = BytesIO()
        zmienna.save(output, format='JPEG')
        im_data = output.getvalue()
        data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

        return render(request, "app/imageAddFilter.html", 
                      {
                          'title':'Nakładanie filtrów',
                          'year':datetime.now().year,
                          'image': data_url,
                          'fileName' : resultFileName + file_extension,
                          'aText' : 'Pobierz plik wynikowy',
                          'labelText' : 'Obraz wynikowy: '
                      })
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageAddFilter.html',
		    {
			    'title':'Nakładanie filtrów',
                'year':datetime.now().year,
		    })

def imageGrayscale(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')
               
        name = request.POST.get('fname')

        img = Image.open(item)
        img = ImageOps.grayscale(img)

        resultFileName, file_extension = os.path.splitext(name)

        if not file_extension:
            filename, file_extension = os.path.splitext(item.name)

        output = BytesIO()
        img.save(output, format='JPEG')
        im_data = output.getvalue()
        data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

        return render(request, "app/imageGrayscale.html", 
                      {
                          'title':'Skala szarości',
                          'year':datetime.now().year,
                          'image': data_url,
                          'fileName' : resultFileName + file_extension,
                          'aText' : 'Pobierz plik wynikowy',
                          'labelText' : 'Obraz wynikowy: '
                      })
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageGrayscale.html',
		    {
			    'title':'Skala szarości',
                'year':datetime.now().year
		    })

def imageRotate(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')
               
        name = request.POST.get('fname')
        degrees = int(request.POST.get('degrees'))
        
        img = Image.open(item)
        img = img.rotate(degrees)
        
        resultFileName, file_extension = os.path.splitext(name)

        if not file_extension:
            filename, file_extension = os.path.splitext(item.name)

        output = BytesIO()
        img.save(output, format='JPEG')
        im_data = output.getvalue()
        data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

        return render(request, "app/imageRotate.html", 
                      {
                          'title':'Obracanie obrazu',
                          'year':datetime.now().year,
                          'image': data_url,
                          'fileName' : resultFileName + file_extension,
                          'aText' : 'Pobierz plik wynikowy',
                          'labelText' : 'Obraz wynikowy: '
                      })
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageRotate.html',
		    {
			    'title':'Obracanie obrazu',
                'year':datetime.now().year
		    })

def imageContrast(request):
    if request.method == 'POST':
        item = request.FILES.get('imgInp')
        contrast = int(request.POST.get('contrast')) / 100          
        name = request.POST.get('fname')

        img = Image.open(item)

        enh = ImageEnhance.Contrast(img)
        result = enh.enhance(contrast)

        resultFileName, file_extension = os.path.splitext(name)

        if not file_extension:
            filename, file_extension = os.path.splitext(item.name)

        output = BytesIO()
        result.save(output, format='JPEG')
        im_data = output.getvalue()
        data_url = 'data:image/jpg;base64,' + base64.b64encode(im_data).decode()

        return render(request, "app/imageContrast.html", 
                      {
                          'title':'Zmiana kontrastu',
                          'year':datetime.now().year,
                          'image': data_url,
                          'fileName' : resultFileName + file_extension,
                          'aText' : 'Pobierz plik wynikowy',
                          'labelText' : 'Obraz wynikowy: '
                      })       
    else:
        assert isinstance(request, HttpRequest)
        return render(request,
		    'app/imageContrast.html',
		    {
			    'title':'Zmiana kontrastu',
                'year':datetime.now().year
		    })