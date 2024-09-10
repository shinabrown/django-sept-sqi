from django.shortcuts import render

# Create your views here.

def new_view(request):
    context = {
        'my_name': 'SHINA'
    }
    return render(request, 'dtl/dtl_example.html', context)
