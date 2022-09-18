<template>
    <div class="pagination-container">
        <div class="pagination">
            <a href="" class="page-link" v-for="(numero,index) in range" :key="index">
                {{numero}}
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name:'Pagination',
    data(){
        return {
            range: null,
            primeiraPaginaForaDoRange: null,
            ultimaPaginaForaDoRange: null,
            rangeDePaginas: null,
            quantPaginas: null,
        }
    },
    methods:{
        criarRangeDePaginacao(){
            let meio = Math.ceil(this.quantPaginas / 2);
            let inicio = this.paginaAtual - meio;
            let fim = this.paginaAtual + meio;
            let parada = this.rangeDePaginas.length;
            let falta;

            falta = inicio < 0 ? Math.abs(inicio) : 0;

            if(inicio < 0){
                inicio = 0;
                fim += falta;
            }

            if(fim >= parada){
                inicio -= Math.abs(fim - parada);
            }

            this.primeiraPaginaForaDoRange = this.paginaAtual > meio;
            this.ultimaPaginaForaDoRange = fim < parada;
            this.range = this.rangeDePaginas.slice(inicio, fim);
        },

    },
}
</script>