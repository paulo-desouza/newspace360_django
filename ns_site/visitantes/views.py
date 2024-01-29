
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)


from visitantes.forms import VisitanteForm
from visitantes.models import Visitante


def registrar_visitante(request):   # THE REQUEST COMES FROM THE CLICK STRAIGHT INTO HERE DIRECTED FROM URLS.PY

    form = VisitanteForm

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit = False)   # salvamos o formulario recebido no post, mas nao os enviamos ao banco de dados usando esse atributo.
                                                    # o formulario vem da classe VisitantesForm, que puxa o modelo Visitantes para buildar o form em HTML
            
            visitante.registrado_por = request.user.porteiro    #request tem informacoes a respeito do usuario e tambem variadas como OS 

            visitante.save()

            messages.success(
                request,
                "Visitante Registrado com Sucesso",

            )

            return redirect("index")
 

    context = {
        "nome_pagina": "Registrar visitante",                   # context carrega as variaveis para o site
        "form": form,

    }

    return render(request, "registrar_visitante.html", context)




def informacoes_visitante(request, id):

    visitante = get_object_or_404(
        Visitante,
        id=id,

    )

    context = {
        "nome_pagina": "Informacoes de visitante",
        "visitante": visitante
    }


    return render(request, "informacoes_visitante.html", context)





