from django.shortcuts import render,redirect
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context)
    
def new(request):

    return render(request, 'movies/new.html')

def create(request):
    #영화 데이터 저장
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    #인스턴스 생성
    movie=Movie()
    movie.title = title
    movie.overview = overview
    movie.poster_path = poster_path
    movie.save()
    return redirect('movies:detail', movie.pk)

def edit(request, pk):
    movie=Movie.objects.get(pk=pk)
    context={'movie':movie}
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    
    movie.title = title
    movie.overview = overview
    movie.poster_path = poster_path
    movie.save()
    return redirect('movies:detail', movie.pk)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
