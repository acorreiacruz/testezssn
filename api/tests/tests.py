from unittest.mock import patch
from django.urls import resolve, reverse
from parameterized import parameterized
from rest_framework import test
from ..models import Sobrevivente
from .test_base_mixin import TesteBaseMixin


class ZssnAPITest(test.APITestCase, TesteBaseMixin):

    def test_se_listar_retorna_status_code_200(self):
        url = reverse('api:listar_criar_sobrevivente')
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 200)

    @patch('api.views.PaginacaoCustomizada.page_size', new=5)
    def test_se_listar_retorna_numero_correto_de_registros_por_pagina(self):
        self.criar_conjunto_de_sobreviventes(8)
        url = reverse('api:listar_criar_sobrevivente')
        resposta = self.client.get(url)
        self.assertEqual(len(resposta.data.get('results')),5)

    def test_se_listar_nao_retorna_sobrevivente_infectado(self):
        sobrevivente = self.criar_sobrevivente(infectado=True,nome="NÂO Publicado")
        self.criar_conjunto_de_sobreviventes(4)
        url = reverse('api:listar_criar_sobrevivente')
        resposta = self.client.get(url)
        self.assertNotIn(sobrevivente.nome, resposta.content.decode('utf-8'))

    def test_se_detalhar_retorna_status_code_200(self):
        self.criar_sobrevivente()
        url = reverse('api:buscar_alterar_excluir_sobrevivente',kwargs={'pk':1})
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 200)



