from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
# Create your views here.


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar pedido')

class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')