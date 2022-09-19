<template>
    <div class="main-container">
        <div class="container">
            <Title :titulo="titulo" :fontawesome="fontawesome"/>
            <div class="table-container">
                <table>
                    <TableHead col1="Sobrevivente" col2="Água" col3="Alimentação" col4="Medicação" col5="Munição"/>
                    <tbody>
                        <tr v-for="objeto in inventarios" :key="objeto.id">
                            <td>{{objeto.nome}}</td>
                            <td>{{objeto.inventario.agua}}</td>
                            <td>{{objeto.inventario.alimentacao}}</td>
                            <td>{{objeto.inventario.medicacao}}</td>
                            <td>{{objeto.inventario.municao}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="pagination-container">
                <div class="pagination">
                    <div class="page-number" v-show="primeiraPaginaForaDoRange">
                        <div class="page-link" @click="carregarDados(1)">1</div>
                    </div>
                    <span v-show="primeiraPaginaForaDoRange">...</span>
                    <div class="page-number" v-for="(numero,index) in range" :key="index">
                        <div class="page-link" @click="carregarDados(numero)">{{numero}}</div>
                    </div>
                    <span v-show="ultimaPaginaForaDoRange">...</span>
                    <div class="page-number" v-show="ultimaPaginaForaDoRange">
                        <div class="page-link" @click="carregarDados(totalDePaginas)">{{totalDePaginas}}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script src="./inventarios.js"></script>


