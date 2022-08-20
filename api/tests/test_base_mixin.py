from ..models import Inventario, Sobrevivente, Local


class TesteBaseMixin():

    def criar_inventario(
        self,
        agua=12,
        alimentacao=5,
        medicacao=6,
        municao=15
    ):
        return Inventario.objects.create(
            agua=agua,
            alimentacao=alimentacao,
            medicacao=medicacao,
            municao=municao
        )

    def criar_local(
        self,
        longitude=45.386,
        latitude=23.417
    ):
        return Local.objects.create(
            latitude=latitude,
            longitude=longitude
        )

    def criar_sobrevivente(self,
            nome='Sobrevivente',
            idade=30,
            sexo='M',
            denuncias=0,
            infectado=False,
            dados_ultimo_local=None,
            dados_inventario=None
    ):

        if dados_ultimo_local is None:
            dados_ultimo_local = {}
        if dados_inventario is None:
            dados_inventario = {}

        return Sobrevivente.objects.create(
            nome=nome,
            idade=idade,
            sexo=sexo,
            infectado=infectado,
            denuncias=denuncias,
            ultimo_local=self.criar_local(**dados_ultimo_local),
            inventario=self.criar_inventario(**dados_inventario)
        )

    def criar_conjunto_de_sobreviventes(self,quant):
        sobreviventes = []
        for i in range(quant):
            nome = f'survivor{i}'
            sobrevivente = self.criar_sobrevivente(nome=nome)
            sobreviventes.append(sobrevivente)

        return sobreviventes

    def get_dados_sobrevivente(self):
        return {
            'nome':'Sobrevivente',
            'idade':30,
            'sexo':'M',
            'infectado':False,
            'denuncias':0,
            'inventario': {
                "agua": 10,
                "alimentacao": 10,
                "medicacao": 10,
                "municao": 10
            }
        }