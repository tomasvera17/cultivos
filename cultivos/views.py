from django.shortcuts import render

def listar_cultivos(request):
    datos = {
        'titulo': 'Mi huerto',
        'mensaje': 'Esta es la lista simulada de cultivos',
        'cultivos': ['Tomates', 'Papas', 'Lechuga', 'Zanahoria']
    }
    return render(request, 'cultivos/lista_cultivos.html', datos)