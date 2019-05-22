from django.shortcuts import render, get_object_or_404

from curriculo.models import Curso,Disciplina

def curso(request, sigla):
    context = {
        'curso': get_object_or_404(Curso, sigla=sigla)
    }
    return render(request, 'curriculo/curso.html', context)

def disciplina(request, id_disciplina):
    context = {
        'disciplina': get_object_or_404(Disciplina, id=id_disciplina)
    }
    return render(request, 'curriculo/disciplina.html', context)