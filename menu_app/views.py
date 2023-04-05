from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

# def pdf_view(request):
#     fs = FileSystemStorage()
#     filename = 'archivo.pdf'
#     if fs.exists(filename):
#         with fs.open(filename) as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'inline; filename="archivo.pdf"'
#             return response
#     else:
#         return HttpResponseNotFound('No se encuentra el archivo PDF.')
    
def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'archivo.pdf'
    try:
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="archivo.pdf"'
            return response
    except FileNotFoundError:
        return HttpResponseNotFound('No se encuentra el archivo PDF.')