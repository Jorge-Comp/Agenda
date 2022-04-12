from urllib import response
from django.shortcuts import redirect, render
from core.models import Evento
# Create your views here.

""" def index(request):
    return redirect('/agenda') """

def lista_eventos(request):

    usuario = request.user
    evento = Evento.objects.all() #.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html',dados)