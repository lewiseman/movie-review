from django.shortcuts import render
from django.core.paginator import Paginator
import requests


# def index(request):
#     return render(request, 'index.html')

def index(request):
    meme = []
    for x in range(1, 10):
        x+=1
        nene = "https://api.themoviedb.org/3/trending/movie/day?api_key=2bca7835c548e3242e8ccc0aa44a0513&page=" + str(x)
        nano = requests.get(nene).json()
        nini = nano['results']
        meme.extend(nini)
    paginator = Paginator(meme, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)