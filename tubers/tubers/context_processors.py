from contactinfo.models import Contactinfo, Aboutinfo

def contactinfo(request):
    ci = Contactinfo.objects.all()
    return {'ci': ci}

def aboutinfo(request):
    about = Aboutinfo.objects.all()
    return {'about': about}