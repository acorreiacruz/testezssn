from unittest.mock import patch
from django.urls import resolve, reverse
from parameterized import parameterized
from rest_framework import test
from .models import Sobrevivente


class ZssnTesteMixin():
    def criar_sobrevivente(self,
            nome='survivor',
            idade=30,
            sexo='M',
            infectado=False,
            denuncias= 0,
            latitude=49.6954,
            longitude=-77.9751,
            agua=10,
            alimentacao=10,
            medicacao=10,
            municao=10
        ):
        return Sobrevivente.objects.create(
            nome=nome,
            idade=idade,
            sexo=sexo,
            infectado=infectado,
            denuncias=denuncias,
            latitude=latitude,
            longitude=longitude,
            agua=agua,
            alimentacao=alimentacao,
            medicacao=medicacao,
            municao=municao
        )

    def criar_conjunto_de_sobreviventes(self,quant):
        for i in range(quant):
            nome = f'survivor{i}'
            self.criar_sobrevivente(nome=nome)


class ZssnAPITest(test.APITestCase, ZssnTesteMixin):

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



