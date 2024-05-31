from django.shortcuts import render

# Create your views here.
def courseview(request):
    return render(request, 'lms/courses.html')