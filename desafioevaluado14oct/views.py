from django.shortcuts import render

def empleados(request):
    categories = ['Alberto', 'Armando', 'Benancio', 'Bencino', 'Dugleidy']
    context = {'categories': categories}
    return render(request, 'empleados.html', context)