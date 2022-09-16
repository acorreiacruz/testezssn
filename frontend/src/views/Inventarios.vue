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
        </div>
    </div>
</template>

<script>
import Title from "../components/Title.vue";
import TableHead from "../components/TableHead.vue";
export default {
    name:"Inventarios",
    components:{
        Title,
        TableHead
    },
    data(){
        return{
            titulo:"Iventários",
            fontawesome: "fa-solid fa-boxes-stacked",
            inventarios: null
        }
    },
    methods:{
        async getInventarios(page=8){
            const url = "http://127.0.0.1:8000/api/sobreviventes/?page=" + page;
            const req = await fetch(url);
            const dados = await req.json();
            this.inventarios = dados.results;
        }
    },
    mounted(){
        this.getInventarios();
    }
}
</script>