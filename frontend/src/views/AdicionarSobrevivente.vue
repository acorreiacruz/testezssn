<template>
    <div class="main-container">
        <div class="container">
            <Title :titulo="titulo" :fontawesome="fontawesome"/>
            <Mensagem :msg="msg" v-show="flagMsg"/>
            <div class="form-main-container">
                <form method="post" @submit="criarSobrevivente">
                    <div class="form-container">
                        <div class="input-container">
                            <label for="nome">Nome:</label>
                            <input type="text" id="nome" v-model="nome" required>
                        </div>
                        <div class="input-container">
                            <label for="idade">Idade:</label>
                            <input type="number" id="idade" min="0" v-model="idade" required>
                        </div>
                        <div class="input-container">
                            <label for="latitude">Latitude:</label>
                            <input type="number" id="latitude" min="-90" max="90" v-model="latitude">
                        </div>
                        <div class="input-container">
                            <label for="longitude">Longitude:</label>
                            <input type="number" id="longitude" min="-180" max="180" v-model="longitude">
                        </div>
                        <div class="input-container">
                            <label for="masculino">Masculino:</label>
                            <input class="sexo" type="radio" id="masculino" value="M" v-model="sexo">
                        </div>
                        <div class="input-container">
                            <label for="feminino">Feminino:</label>
                            <input class="sexo" type="radio" id="feminino" value="F" v-model="sexo">
                        </div>
                        <div class="input-container">
                            <label for="agua">Água:</label>
                            <input type="number" min="0" id="agua" v-model="agua" required>
                        </div>
                        <div class="input-container">
                            <label for="alimentacao">Alimentação:</label>
                            <input type="number" min="0" id="alimentacao" v-model="alimentacao" required>
                        </div>
                        <div class="input-container">
                            <label for="medicacao">Medicação:</label>
                            <input type="number" min="0" id="medicacao" v-model="medicacao">
                        </div>
                        <div class="input-container">
                            <label for="municao">Munição:</label>
                            <input type="number" min="0" id="municao" v-model="municao" required>
                        </div>
                    </div>
                    <div class="button-container">
                        <div class="btn-save">
                            <button type="submit"><i class="fa-solid fa-floppy-disk"></i> Salvar</button>
                        </div>
                        <div class="btn-cancel">
                            <button type="button">
                                <router-link to="/">
                                    <i class="fa-solid fa-xmark"></i> Cancelar
                                </router-link>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import Title from "../components/Title.vue";
import Mensagem from "../components/Mensagem.vue";
export default {
    name:"AdicionarSobrevivente",
    components:{
        Title,
        Mensagem
    },
    data(){
        return{
            titulo:"Adicionar Sobrevivente",
            fontawesome:"fa-solid fa-user",
            nome:null,
            idade:null,
            latitude:null,
            longitude:null,
            sexo:null,
            agua:null,
            alimentacao:null,
            medicacao:null,
            municao:null,
            flagMsg: false,
            msg: null
        }
    },
    methods:{
        gerarObjeto(){
            return {
                nome:this.nome,
                idade:this.idade,
                ultimo_local:{
                    latitude:this.latitude,
                    longitude:this.longitude,
                },
                sexo:this.sexo,
                inventario:{
                    agua:this.agua,
                    alimentacao:this.alimentacao,
                    medicacao:this.medicacao,
                    municao:this.municao
                }
            }
        },
        showMsg(msg){
            this.flagMsg = true;
            this.msg = msg;
        },
        removerMsg(time=2000){
            setTimeout(()=>{
                this.flagMsg = false;
            }, time);
        },
        limparCampos(){
            this.nome = null;
            this.idade = null;
            this.latitude = null;
            this.longitude = null;
            this.sexo = null;
            this.agua = null;
            this.alimentacao = null;
            this.medicacao = null;
            this.municao = null;
        },
        async criarSobrevivente(e){
            e.preventDefault();

            const sobrevivente = this.gerarObjeto();
            const dataJSON = JSON.stringify(sobrevivente);

            const req = await fetch(
                "http://127.0.0.1:8000/api/sobreviventes/",
                {
                    method:"POST",
                    headers:{'Content-type':'application/json'},
                    body: dataJSON
                }
            );

            const res = await req.json();

            this.showMsg("Sobrevivente cadastrado com sucesso!");

            this.limparCampos();
            this.removerMsg();
        },
    }
}
</script>