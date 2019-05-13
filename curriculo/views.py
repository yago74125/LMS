from django.shortcuts import render, get_object_or_404

from curriculo.models import Curso

def curso(request, sigla):
    c = get_object_or_404(Curso, sigla=sigla)
    context = {
        'curso': c,
        'matriz': c.monta_matriz()
    }
    return render(request, 'curriculo/curso.html', context)

def cursos(request):
    context = {
        'cursos': Curso.objects.all()
    } 
    return render(request, 'curriculo/cursos.html', context)   