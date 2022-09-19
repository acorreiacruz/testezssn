<template>
    <div class="main-container">
        <div class="container">
            <Title :titulo="titulo" :fontawesome="fontawesome"/>
            <div class="table-container">
                <table>
                    <TableHead col1="Porcentagem de Infectados" col2="Prcentagem de Não Infectados" col3="Média dos Recursos Por Sobrevivente"/>
                    <tbody>
                        <tr>
                            <td>
                                {{infectados}}
                            </td>
                            <td>
                                {{naoInfectados}}
                            </td>
                            <td>
                                <p>Água: {{medias.agua}}</p>
                                <p>Alimentação: {{medias.alimentacao}}</p>
                                <p>Medicação: {{medias.medicacao}}</p>
                                <p>Munição: {{medias.municao}}</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script src="./relatorios.js"></script>