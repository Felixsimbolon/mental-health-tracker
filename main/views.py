from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306219575',
        'name': 'Jeremi Felix Adiyatma',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
