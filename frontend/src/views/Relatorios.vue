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
                                <p>ALimentação: {{medias.alimentacao}}</p>
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

<script>
import Title from "../components/Title.vue";
import TableHead from "../components/TableHead.vue";
export default {
    name:"Relatorios",
    components:{
        Title,
        TableHead
    },
    data(){
        return{
            titulo:"Relatórios",
            fontawesome: "fa-sharp fa-solid fa-chart-column",
            url: "http://127.0.0.1:8000/api/sobreviventes/relatorio/",
            medias:{},
            infectados:null,
            naoInfectados:null
        }
    },
    methods:{
        async getRelatorioInfectados(){
            const url = this.url + 'infectados/';
            const req = await fetch(url);
            const res = await req.json();
            this.infectados = res.infectados;

        },
        async getRelatorioNaoInfectados(){
            const url = this.url + 'nao-infectados/';
            const req = await fetch(url);
            const res = await req.json();
            this.naoInfectados = res.nao_infectados;
        },
        async getRelatorioMediaDosRecursos(){
            const url = this.url + 'medias-dos-inventarios/';
            const req = await fetch(url);
            const res = await req.json();
            const dados = res.medias_dos_inventarios;
            this.medias = {...dados};
        },
    },
    mounted(){
        this.getRelatorioInfectados();
        this.getRelatorioNaoInfectados();
        this.getRelatorioMediaDosRecursos();
    }
}
</script>