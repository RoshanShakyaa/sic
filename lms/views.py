from django.shortcuts import render
from .models import Course


# Create your views here.
def courseview(request):
    courses = Course.objects.all().order_by('-id')
    context = {'courses': courses}
    return render(request, 'lms/courses.html', context)