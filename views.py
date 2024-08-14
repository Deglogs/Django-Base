from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
'''
def home(request):
    mylist=['A','B','c','D','E','F','G']
    context={'mylist':mylist}
    return render(request,"homepage.html",context)
'''



def movie_det(request):
    title='Toy Story'
    api_key='c4759f5d'
    url=f'https://www.omdbapi.com/?t={title}&apikey={api_key}'
    r=requests.get(url)
    if r.status_code==200:
        moviedata=r.json()
        return render(request,'movie_det.html',context={'movie':moviedata})
    else:
        return HttpResponse(f'Error fetching movie details:{r.text}')

def home(request):
    fav_movie='Cars'
    api_key='c4759f5d'
    page='1'
    url=f'https://www.omdbapi.com/?s={fav_movie}&apikey={api_key}&page={page}'

    h_response=requests.get(url)
    if h_response.status_code==200:
        moviedata=h_response.json()
        movies=moviedata.get('Search',[])
        return render(request,'home.html',context={'movies':movies,'fav_movie':fav_movie})
    else:
        return HttpResponse(f'Error fetching movies')
