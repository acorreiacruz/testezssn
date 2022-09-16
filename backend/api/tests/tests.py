from unittest.mock import patch
from django.urls import reverse
from rest_framework.test import APITestCase
from .test_base_mixin import TesteBaseMixin
from json import dumps


class TestAPIZssn(APITestCase, TesteBaseMixin):

    def get_api_url(self, action='list', **kwargs):
        url = reverse(f'api:api-sobreviventes-{action}', kwargs={**kwargs})
        return url

    def get_resposta(self, action='list', method='get', content_type='', data=None, **kwargs):
        if method == 'get':
            resposta = self.client.get(
                self.get_api_url(action=action, **kwargs),
            )

        if method == 'post':
            resposta = self.client.post(
                self.get_api_url(action=action, **kwargs),
                data=data,
                content_type=content_type
            )

        if method == 'delete':
            resposta = self.client.delete(
                self.get_api_url(action=action, **kwargs)
            )

        if method == 'patch':
            resposta = self.client.patch(
                self.get_api_url(action=action, **kwargs),
                data=data
            )
        return resposta

    def test_se_api_retorna_status_code_200_ao_listar(self):
        resposta = self.get_resposta()
        self.assertEqual(resposta.status_code, 200)

    @patch('api.pagination.PaginacaoCustomizada.page_size', new=5)
    def test_se_api_retorna_numero_correto_por_pagina_ao_listar(self):
        self.criar_conjunto_de_sobreviventes(10)
        resposta = self.get_resposta()
        qnt = len(resposta.data.get('results'))
        self.assertEqual(qnt, 5)

    def test_se_api_cria_sobrevivente(self):
        dados = self.get_dados_sobrevivente()
        json = dumps(dados)
        resposta = self.get_resposta(
            method='post',
            data=json,
            content_type='application/json'
        )
        data = resposta.data
        self.assertEqual(data.get('nome'), dados.get('nome'))
        self.assertEqual(resposta.status_code, 201)

    def test_se_api_retorna_status_code_400_ao_criar(self):
        resposta = self.get_resposta(method='post')
        self.assertEqual(resposta.status_code, 400)

    def test_se_api_busca_o_sobrevivente_correto(self):
        sobrevivente = self.criar_sobrevivente()
        resposta = self.get_resposta(action='detail',pk=sobrevivente.id)
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data.get('nome'), sobrevivente.nome)

    def test_se_api_retorna_status_code_404_ao_buscar(self):
        resposta = self.get_resposta(action='detail',pk=10)
        self.assertEqual(resposta.status_code, 404)

    def test_se_api_retorna_status_code_204_ao_deletar(self):
        sobrevivente = self.criar_sobrevivente()
        resposta = self.get_resposta(
            action='detail',method='delete',pk=sobrevivente.id
        )
        self.assertEqual(resposta.status_code, 204)

    def test_se_api_retorna_status_code_404_ao_deletar(self):
        resposta = self.get_resposta('detail','delete',pk=10)
        self.assertEqual(resposta.status_code, 404)

    def test_se_api_atualiza_o_sobrevivente(self):
        local = {
			"latitude": -13.2719,
			"longitude": -48.2852,
        }
        sobrevivente = self.criar_sobrevivente(dados_ultimo_local=local)

        resposta1 = self.get_resposta(
            'detail','patch',
            {
                "latitude": 76.6762,
                "longitude": -82.2616
            },
            pk=sobrevivente.id
        )
        self.assertEqual(resposta1.status_code, 200)

        resposta2 = self.get_resposta('detail', pk=sobrevivente.id)
        self.assertEqual(resposta1.data.get('latitude'), resposta2.data.get('latitude'))
        self.assertEqual(resposta1.data.get('longitude'), resposta2.data.get('longitude'))

    def test_se_api_negocia_itens(self):
        dados_inventario = {
            'agua': 23, # 5 pontos
            'alimentacao': 12, # 4 pontos
            'medicacao': 5,
            'municao': 10
        }
        sobrevivente1 = self.criar_sobrevivente(dados_inventario=dados_inventario)
        sobrevivente2 = self.criar_sobrevivente(dados_inventario=dados_inventario)

        kwargs = {
            'id1': sobrevivente1.id,
            'itm1': 'agua',
            'qnt1': 4,
            'id2': sobrevivente2.id,
            'itm2': 'alimentacao',
            'qnt2': 5
        }

        resposta1 = self.get_resposta('negociar-itens',**kwargs)
        self.assertEqual(resposta1.status_code, 200)

        resposta2 = self.get_resposta('detail',pk=sobrevivente1.id)
        self.assertEqual(resposta2.data.get('agua'), 19)
        self.assertEqual(resposta2.data.get('alimentacao'), 17)

        resposta3 = self.get_resposta('detail',pk=sobrevivente2.id)
        self.assertEqual(resposta3.data.get('agua'), 27)
        self.assertEqual(resposta3.data.get('alimentacao'), 7)

    def test_se_api_retorna_status_code_404_ao_atualizar(self):
        resposta = self.get_resposta(
            'detail','patch',
            pk=10
        )
        self.assertEqual(resposta.status_code, 404)

    def test_se_api_retorna_relatorios_de_infectados_corretos(self):
        # Gerando 25 sobreviventes não infectados
        sobreviventes = self.criar_conjunto_de_sobreviventes(25)
        # Tornando 5 deles infectados
        for i in range(5):
            sobreviventes[i].infectado = True
            sobreviventes[i].save()

        resposta = self.get_resposta('relatorio-infectados')
        self.assertEqual(resposta.data.get('infectados'), "20.00 %")

        resposta = self.get_resposta('relatorio-nao-infectados')
        self.assertEqual(resposta.data.get('nao infectados'), "80.00 %")

    def test_se_api_retorna_relatorio_de_medias_dos_inventarios(self):
        # Gerando 25 sobreviventes não infectados com as mesmas quantidades
        # de itens no inventario
        sobreviventes = self.criar_conjunto_de_sobreviventes(25)
        resposta = self.get_resposta('relatorio-medias-dos-inventarios')
        medias = resposta.data.get('medias dos inventarios')
        self.assertEqual(medias.get('agua'), "12.00")
        self.assertEqual(medias.get('alimentacao'), "5.00")
        self.assertEqual(medias.get('medicacao'), "6.00")
        self.assertEqual(medias.get('municao'), "15.00")

    def test_se_api_realiza_denuncia_de_infectado(self):
        # Criando um sobrevivente com 0 denúncias
        sobrevivente = self.criar_sobrevivente()

        # Realizando 3 denúncias
        for i in range(3):
            resposta = self.get_resposta('denunciar', pk=sobrevivente.id)
        # Verificando se a denuncia foi realizada
        self.assertEqual(resposta.status_code, 201)

        # Buscando o sobrevivente denunciado
        resposta2 = self.get_resposta('detail', pk=sobrevivente.id)
        # Verificando se a quantidade de denuncias é 1
        self.assertEqual(
            resposta2.data.get('detail')[:],
            "Indivíduo infectado!"
        )



