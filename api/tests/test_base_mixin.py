from ..models import Sobrevivente


class TesteBaseMixin():
    def criar_sobrevivente(self,
            nome='Sobrevivente',
            idade=30,
            sexo='M',
            infectado=False,
            denuncias=0,
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
        sobreviventes = []
        for i in range(quant):
            nome = f'survivor{i}'
            sobrevivente = self.criar_sobrevivente(nome=nome)
            sobreviventes.append(sobrevivente)

        return sobreviventes