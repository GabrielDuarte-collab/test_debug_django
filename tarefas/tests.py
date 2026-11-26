import json
from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Tarefa
from .views import listar_tarefas  

class TarefaTestCase(SetupTestCase):
    # def setUp(self):
    #     self.cat = Categoria.objects.create(nome="Categoria Teste")
    #     self.tarefa = Tarefa.objects.create(titulo="Estudar testes no Django", categoria=self.cat, concluida=False)
    
    def test_criacao_tarefa(self):

        self.assertEqual(self.tarefa.titulo,"Estudar testes no Django")
        