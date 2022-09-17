<template>
    <div class="main-container">
        <div class="container">
            <Title :titulo="titulo" :fontawesome="fontawesome" />
            <div class="button-container">
                <div class="button">
                    <router-link to="/sobreviventes/adicionar">
                        <i class="fa-solid fa-plus"></i> Adicionar
                    </router-link>
                </div>
            </div>
            <div class="table-container">
                <table>
                    <TableHead col1="Id" col2="Nome" col3="Idade" col4="Sexo" col5="Infectado" col6="Denúncias" col7="Adicionais"/>
                    <tbody>
                        <tr v-for="sobrevivente in sobreviventes" :key="sobrevivente.id">
                            <td>
                                {{sobrevivente.id}}
                            </td>
                            <td>
                                {{sobrevivente.nome}}
                            </td>
                            <td>
                                {{sobrevivente.idade}}
                            </td>
                            <td>
                                {{sobrevivente.sexo}}
                            </td>
                            <td>
                                <span v-if="sobrevivente.infectado">
                                    <i class="fa-solid fa-skull-crossbones"></i>
                                </span>
                                <span v-else>
                                    <i class="fa-solid fa-shield"></i>
                                </span>
                            </td>
                            <td>
                                {{sobrevivente.denuncias}}
                            </td>
                            <td>
                                <div v-if="sobrevivente.infectado" class="itens-container">
                                    <div class="infectado">
                                        <i class="fa-solid fa-location-dot"></i>
                                    </div>
                                    <div class="infectado">
                                        <i class="fa-solid fa-briefcase"></i>
                                    </div>
                                    <div class="infectado">
                                        <i class="fa-solid fa-triangle-exclamation"></i>
                                    </div>
                                </div>
                                <div v-else class="itens-container">
                                    <router-link  class="item local" :to="{
                                        name:'alterar-local',
                                        query:{id:sobrevivente.id}
                                    }">
                                        <i class="fa-solid fa-location-dot"></i>
                                    </router-link>
                                    <div class="item inventario-btn" @click="getInventario(sobrevivente)">
                                        <i class="fa-solid fa-briefcase"></i>
                                    </div>
                                    <div class="item denunciar" @click="popUp(sobrevivente)">
                                        <i class="fa-solid fa-triangle-exclamation"></i>
                                    </div>
                                </div>
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
import Mensagem from "../components/Mensagem.vue";
export default {
    name:"Sobreviventes",
    components:{
    Title,
    TableHead,
    Mensagem,
    Mensagem
},
    data(){
        return{
            titulo:"Sobreviventes",
            fontawesome: "fa-solid fa-users",
            sobreviventes: null,
            cssClassLocal:"item local",
            cssClassInventario: "item inventario",
            cssClassDenunciar: "item ",
            msg:null,
        }
    },
    methods:{
        async getSobreviventes(){
            const url = "http://127.0.0.1:8000/api/sobreviventes/";
            const req = await fetch(url)
            const dados = await req.json();
            this.sobreviventes = dados;
        },
        async denunciarSobrevivente(id){
            const url = `http://127.0.0.1:8000/api/sobreviventes/${id}/denunciar/`;
            const res = await fetch(url);
            if(res == 201){
                this.msg = "Denúncia de infectado realizada com sucesso!";
            }
        },
        verificaPrompt(sobreviventeId){
            let id = prompt("Informe o id do sobrevivente a ser denunciado!");
            if(id == null) return null;
            id = Number(id);
            while(id <= 0 || isNaN(id) || id==sobreviventeId){
                id = prompt("Você precica inserir um id válido e um sobrevivente não pode denunciar ele mesmo!");
                if(id == null) return null;
                id = Number(id);
            }
            return id;
        },
        popUp(sobrevivente){
            if(sobrevivente.infectado){
                alert("Um zumbie não pode realizar uma denúncia!");
            }
            else{
                const id = this.verificaPrompt(sobrevivente.id);
                if(id){
                    this.denunciarSobrevivente(id);
                }
            }
        },
        getInventario(sobrevivente){
            const msg = `
                Inventario do Sobrevivente ${sobrevivente.id}:
                    Água: ${sobrevivente.inventario.agua},
                    Alimentação: ${sobrevivente.inventario.alimentacao},
                    Medicação: ${sobrevivente.inventario.medicacao},
                    Munição: ${sobrevivente.inventario.municao}
            `;
            alert(msg);
        }
    },
    mounted(){
        this.getSobreviventes();
    }
}
</script>