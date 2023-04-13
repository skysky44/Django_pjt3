from django.shortcuts import render
from .models import Review, Comment
# Create your views here.
def index(request):
    reviews = Review.objects.all()


    context = {
        'reviews' : reviews,
    }
    return render(request, 'reviews/index.html', context)