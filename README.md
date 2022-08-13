# **Teste de codificação de desenvolvedor**
Certifique-se de ler este documento com atenção e siga as diretrizes.
## **Descrição do Problema**
ZSSN (Rede Social de Sobrevivência Zumbi). O mundo como o conheceu caiu em um cenário apocalíptico. Um vírus produzido em laboratório está transformando seres humanos e animais em zumbis, famintos por carne fresca.
Você, como membro da resistência aos zumbis (e o último sobrevivente que sabe codificar), foi designado para desenvolver um sistema para compartilhar recursos entre humanos não infectados.
## **Exigências**
Use os seguintes Linguagens/ estruturas: Python e os Frameworks Django e Django Rest. Banco de Dados Postgres. Ferramenta de Controle de Versões Git. HTML, CSS, Javascript.
Você desenvolverá uma API REST (sim, nós nos preocupamos com o design da arquitetura, mesmo no meio de um apocalipse zumbi!), que armazenará informações sobre os sobreviventes, bem como os recursos que eles possuem.
Para fazer isso, a API deve atender aos seguintes casos de uso:
- **Adicionar sobreviventes ao banco de dados**
Um sobrevivente deve ter um nome, idade, sexo e último local (latitude, longitude).
Um sobrevivente também possui um inventário de recursos de sua própria propriedade (que você precisa declarar quando do registro do sobrevivente).
- **Atualizar local do sobrevivente**
Um sobrevivente deve ter a capacidade de atualizar seu último local, armazenando o novo par de latitude / longitude na base (não é necessário rastrear locais, basta substituir o anterior).
- **Sinalizar sobrevivente como infectado**
Em uma situação caótica como essa, é inevitável que um sobrevivente seja contaminado pelo vírus. Quando isso acontece, precisamos sinalizar o sobrevivente como infectado.
Um sobrevivente infectado não pode negociar com outras pessoas, não pode acessar / manipular seu inventário, nem ser listado nos relatórios (as pessoas infectadas estão meio mortas de qualquer maneira, veja o item nos relatórios abaixo).
Um sobrevivente é marcado como infectado quando pelo menos outros três sobreviventes relatam sua contaminação.
Quando um sobrevivente é infectado, seus itens de inventário ficam inacessíveis (eles não podem negociar com outros).
- **Os sobreviventes não podem adicionar / remover itens do inventário**
Seus pertences devem ser declarados quando forem registrados pela primeira vez no sistema. Depois disso, eles só podem alterar seu inventário por meio de negociação com outros sobreviventes.
Os itens permitidos no inventário são descritos acima no primeiro recurso.
- **Itens comerciais:**
Os sobreviventes podem trocar itens entre si.
Para fazer isso, eles devem respeitar a tabela de preços abaixo, onde o valor de um item é descrito em termos de pontos.
Ambos os lados do comércio devem oferecer a mesma quantidade de pontos. Por exemplo, 1 água e 1 medicamento (1 x 4 + 1 x 2) valem 6 munições (6 x 1) ou 2 itens alimentares (2 x 3).
As operações em si não precisam ser armazenadas, mas os itens devem ser transferidos de um sobrevivente para o outro.
| Item  | Pontos   |
|-------|----------|
| 1 Água | 4 pontos |
|-------|----------|
| 1 Alimentação | 3 pontos |
|-------|----------|
| 1 Medicamento | 2 pontos |
|-------|----------|
| 1 Municão | 1 pontos |

