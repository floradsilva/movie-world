from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Movie, Category, Relationship
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

language = None
genre = None
sorter = None
    
m = None
c = None
l = None
g = None

def initialize():
    global m, c, l,g
    m = Movie.objects.all()
    c = Category.objects.all()
    l = Category.objects.filter(c_type__startswith='Language')
    g = Category.objects.filter(c_type__startswith='Genre')
    
def index(request):
    initialize()
    paginator = Paginator(m, 10)
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('movie_info/list.html', {"movies": movies,'categories': c, 'languages':l, 'genres':g})

def filter_sort(request):
    initialize()
    global language, genre, sorter
    
    lang = request.GET.get('filter_language', None)
    if lang:
        global language
        language = request.GET.get('filter_language')

    gen =  request.GET.get('filter_genre', None)
   
    if gen:
        global genre
        genre = request.GET.get('filter_genre')

    sort = request.GET.get('Sort', None)
    if sort:
        global sorter
        sorter = request.GET.get('Sort')

    if lang and gen and sort:
        if (lang != 'All' and gen != 'All' and sort != 'no_sort'):
            return lgs(request) 

        elif (lang != 'All'  and gen != 'All') or (request.GET.get('lg',None)):
            return lg(request)        

        elif lang != 'All' and sort != 'no_sort':
            return ls(request)

        elif gen != 'All' and sort != 'no_sort':
            return gs(request)

        elif lang != 'All':
            return la(request)

        elif genre != 'All':
            return ge(request)

        elif sorter != 'no_sort':
            return so(request)

    elif (request.GET.get('lgs',None)):
        return lgs(request) 
 
    elif (request.GET.get('lg',None)):
        return lg(request) 

    elif (request.GET.get('ls',None)):
        return ls(request) 

    elif (request.GET.get('gs',None)):
        return gs(request) 

    elif (request.GET.get('la',None)):
        return la(request) 

    elif (request.GET.get('g',None)):
        return ge(request) 

    elif (request.GET.get('s',None)):
        return so(request) 

    else:
        return index(request)
    

def lgs(request):
    
    c_language = Category.objects.filter(value = language)
    movies1 = [x.c_movie.all() for x in c_language]
    movie = []
    for mov in movies1:
        movie += mov
    m = movie
    #m = [x for x in m if x in movie]
    c_genre = Category.objects.filter(value = genre)
    movies1 = [x.c_movie.all() for x in c_genre]
    movie = []
    for mov in movies1:
        movie += mov
    m = [x for x in m if x in movie]

    sortedList = Movie.objects.all().order_by(sorter) 
    m = [x for x in sortedList if x in m]

      
    paginator = Paginator(m, 10)
    page = request.GET.get('lgs')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('movie_info/lgs.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})



def lg(request):

    c_language = Category.objects.filter(value = language)
    movies1 = [x.c_movie.all() for x in c_language]
    movie = []
    for mov in movies1:
        movie += mov
    m = movie

    c_genre = Category.objects.filter(value = genre)
    movies1 = [x.c_movie.all() for x in c_genre]
    movie = []
    for mov in movies1:
        movie += mov
    m = [x for x in m if x in movie]
      
    paginator = Paginator(m, 10)
    page = request.GET.get('lg')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    #assert False
    return render_to_response('movie_info/lg.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})


def ls(request):
    c_language = Category.objects.filter(value = language)
    movies1 = [x.c_movie.all() for x in c_language]
        
    movie = []
    for mov in movies1:
        movie += mov
        
    m = movie

    sortedList = Movie.objects.all().order_by(sorter) 
    m = [x for x in sortedList if x in m]

    
    paginator = Paginator(m, 10)
    page = request.GET.get('ls')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('movie_info/ls.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})
    


def gs(request):
    c_genre = Category.objects.filter(value = genre)
    movies1 = [x.c_movie.all() for x in c_genre]
        
    movie = []
    for mov in movies1:
        movie += mov
        
    m = movie

    sortedList = Movie.objects.all().order_by(sorter) 
    m = [x for x in sortedList if x in m]

    
    paginator = Paginator(m, 10)
    page = request.GET.get('gs')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('movie_info/gs.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})


def la(request):

    c_language = Category.objects.filter(value = language)
    movies1 = [x.c_movie.all() for x in c_language]
    movie = []
    for mov in movies1:
        movie += mov
    m = movie

    paginator = Paginator(m, 10)
    page = request.GET.get('la')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render_to_response('movie_info/la.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})


def so(request):
    m = Movie.objects.all().order_by(sorter) 

    paginator = Paginator(m, 10)
    page = request.GET.get('s')
    

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    #assert False
    return render_to_response('movie_info/s.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})


def ge(request):

    c_genre = Category.objects.filter(value = genre)
    movies1 = [x.c_movie.all() for x in c_genre]
    movie = []
    for mov in movies1:
        movie += mov
    m = movie
      
    paginator = Paginator(m, 10)
    page = request.GET.get('g')
    
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    #assert False
    return render_to_response('movie_info/g.html', {"movies": movies, 'categories': c, 'languages':l, 'genres':g})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_info/movie_detail.html', {'movie':movie})
