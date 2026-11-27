import json
from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Tarefa
from .views import listar_tarefas  

class setuptest(TestCase)
    

class TarefaTestCase(TestCase):
   
    def test_criacao_tarefa(self):

        self.assertEqual(self.tarefa.titulo,"Estudar testes no Django")
        