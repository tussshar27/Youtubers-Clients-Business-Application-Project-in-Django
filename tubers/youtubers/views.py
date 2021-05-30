from django.shortcuts import render, get_object_or_404
from .models import Youtuber

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')    
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()    
    #note: values_list() gives array of items   #values_list() return array list
    #we can also use all() instead of values_list() but values_list() is more precise then all(). 
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'city' in request.GET:               #if there is city in request...
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search
    }
    return render(request, 'youtubers/tubers.html', data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date') #objects return key value pair objects
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()    
    #note: values_list() gives array of items   #values_list() return array list
    #we can also use all() instead of values_list() but values_list() is more precise then all(). 
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()


    #search logic           #overriding tubers
    if 'keyword' in request.GET:            #if there is keyword in request...
        keyword = request.GET['keyword']    #note: get or post have named parameter eg. <right side> 'keyword', bring that data into <left side> keyword
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)  #the above tubers variable is used wth filter() here.

    if 'city' in request.GET:               #if there is city in request...
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    

    data = {
        'tubers': tubers,

        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search
    }
    return render(request, 'youtubers/search.html', data)