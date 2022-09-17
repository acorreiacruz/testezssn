<template>
    <div class="main-container">
        <div class="container">
            <Title :titulo="titulo" :fontawesome="fontawesome"/>
            <Mensagem :msg="msg" v-show="flagMsg"/>
            <div class="main-form-container">
                <form action="#" @submit="btnComercio">
                    <div class="form-container">
                        <div class="input-container comercio">
                            <label for="survivor01">Id Sobrevivente 1:</label>
                            <input type="number" id="survivor01" min="1" v-model="id1" required>
                        </div>
                        <div class="input-container">
                            <label for="survivor01">Id Sobrevivente 2:</label>
                            <input type="number" id="survivor01" min="1" v-model="id2" required>
                        </div>
                        <div v-show="flagInputs" class="input-container">
                            <label for="item1">Item do Sobrevivente 1:</label>
                            <select name="item1" id="item1" v-model="item1" @change="limparInputs(true),setLimitadores(),limparPontos(true)">
                                <option value="agua">Água</option>
                                <option value="alimentacao">Alimentação</option>
                                <option value="medicacao">Medicação</option>
                                <option value="municao">Munição</option>
                            </select>
                        </div>
                        <div v-show="flagInputs" class="input-container">
                            <label for="item2">Item do Sobrevivente 2:</label>
                            <select name="item2" id="item2" v-model="item2" @change="limparInputs(false),setLimitadores(),limparPontos(false)">
                                <option value="agua">Água</option>
                                <option value="alimentacao">Alimentação</option>
                                <option value="medicacao">Medicação</option>
                                <option value="municao">Munição</option>
                            </select>
                        </div>
                        <div v-show="flagInputs" class="input-container">
                            <label>Quantidade do Item 1:</label >
                            <div class="flex">
                                <input type="button" class="btn-add" @click="btnAddUmItem(true),updatePontos(),updateInventarios(true, true)" value="+ 1x">
                                <input type="button" class="btn-remove" @click="btnRemoveUmItem(true),updatePontos(),updateInventarios(true, false)" value="- 1x">
                                <input type="button" class="btn-result" :value="qnt1">
                            </div>
                        </div>
                        <div v-show="flagInputs" class="input-container">
                            <label for="qnt2">Quantidade do Item 2:</label>
                            <div class="flex">
                                <input type="button" class="btn-add" @click="btnAddUmItem(false),updatePontos(),updateInventarios(false, true)" value="+ 1x">
                                <input type="button" class="btn-remove" @click="btnRemoveUmItem(false),updatePontos(),updateInventarios(false, false)" value="- 1x">
                                <input type="button" class="btn-result" :value="qnt2">
                            </div>
                        </div>
                        <div v-show="flagInputs" class="input-container">
                            <button>Pontuação Total 1 = {{pontos1}}</button>
                        </div>
                        <div v-show="flagInputs" class="input-container">
                            <button>Pontuação Total 2 = {{pontos2}}</button>
                        </div>
                    </div>
                    <div v-show="flagInputs" class="inventarios-container">
                            <div class="inventario" v-for="sobrevivente in sobreviventes" :key="sobrevivente.id">
                                <p class="inventario-title">
                                    Inventário do Sobrevivente de Id {{sobrevivente.id}}
                                </p>
                                <div class="grid-inventario">
                                    <div class="inventario-item">
                                        Água: {{sobrevivente.inventario.agua}}
                                    </div>
                                    <div class="inventario-item">
                                        Alimentação: {{sobrevivente.inventario.alimentacao}}
                                    </div>
                                    <div class="inventario-item">
                                        Medicação: {{sobrevivente.inventario.medicacao}}
                                    </div>
                                    <div class="inventario-item">
                                        Munição: {{sobrevivente.inventario.municao}}
                                    </div>
                                </div>
                            </div>
                    </div>
                    <div class="button-container">
                        <div class="btn-save">
                            <button type="submit" @click="realizarTroca">
                                <i :class="btnImg"></i> {{btnTexto}}
                            </button>
                        </div>
                        <div v-show="flagInputs" class="btn-reset">
                            <button type="button" @click="resetar">
                                <i class="fa-solid fa-arrows-rotate"></i> Resetar
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
    name:"Comercio",
    components:{
    Title,
    Mensagem
},
    data(){
        return {
            titulo:"Comércio",
            fontawesome: "fa-solid fa-cart-shopping",
            btnTexto: "Buscar Inventários",
            btnImg:"fa-sharp fa-solid fa-magnifying-glass",
            flagBtn: false,
            id1:null,
            item1:null,
            qnt1:0,
            id2:null,
            item2:null,
            qnt2:0,
            sobreviventes: null,
            tabelaDePontos:{
                agua:5,
                alimentacao:4,
                medicacao:3,
                municao:2,
            },
            pontos1: null,
            pontos2: null,
            msg:null,
            flagMsg:false,
            flagInputs: false,
            baseUrl: "http://127.0.0.1:8000/api/sobreviventes/",
            max1: null,
            max2: null,
        }
    },
    methods:{
        btnAddUmItem(flag){
            if(flag && this.qnt1 < this.max1){
                this.qnt1 += 1;
            }
            if(!flag && this.qnt2 < this.max2){
                this.qnt2 += 1;
            }
        },
        btnRemoveUmItem(flag){
            if(flag && this.qnt1 > 0){
                this.qnt1 -= 1;
            }
            if(!flag && this.qnt2 > 0){
                this.qnt2 -= 1;
            }
        },
        async getResponse(url){
            const req = await fetch(url);
            // const res = await req.json();
            return req;
        },
        async getDados(response){
            const dados = await response.json();
            return dados;
        },
        setMsgFromStatusCode(response1, response2){
            if(response1.status == 403 || response2.status == 403){
                this.showMsg("Um zumbi não pode comercializar itens!");
                return false;
            }
            if(response1.status == 404 || response2.status == 404){
               this.showMsg("Sobrevivente(s) não encontrado(s)!");
               return false;
            }
            return true;
        },
        hideMsg(time){
            setTimeout(()=>{
                this.flagMsg = false;
            },time);
        },
        showMsg(msg){
            this.msg = msg;
            this.flagMsg = true;
        },
        resetarBtn(){
            this.btnTexto = "Buscar Inventários";
            this.btnImg = "fa-sharp fa-solid fa-magnifying-glass";
            this.flagBtn = false;
        },
        resetarForm(){
            this.id1 = null;
            this.item1 = null;
            this.qnt1 = 0;
            this.id2 = null;
            this.item2 = null;
            this.qnt2 = 0;
            this.flagInputs = false;
            this.pontos1 = null;
            this.pontos2 = null;
            this.sobreviventes = null;
        },
        resetar(){
            this.resetarBtn();
            this.resetarForm();
        },
        async realizarTroca(){
            if(this.flagBtn && this.verificaPontos()){
                const url = this.baseUrl + `trocas/${this.id1}/${this.item1}/${this.qnt1}/${this.id2}/${this.item2}/${this.qnt2}/`;
                const res = await this.getResponse(url);
                this.resetar();
                this.showMsg("Operação realizada com sucesso!");
            }
            if(this.flagBtn || this.flagInputs){
                this.showMsg("Operação inválida, pontuações diferentes!");
            }
        },
        limparInputs(flag){
            if(flag){
                this.qnt1 = 0
            }
            else{
                this.qnt2 = 0;
            }
        },
        limparPontos(flag){
            if(flag){
                this.pontos1 = 0;
            }
            else{
                this.pontos2 = 0;
            }
        },
        setLimitadores(){
            this.max1 = this.sobreviventes[0].inventario[this.item1];
            this.max2 = this.sobreviventes[1].inventario[this.item2];
        },
        updatePontos(){
            this.pontos1 = this.qnt1 * this.tabelaDePontos[this.item1];
            this.pontos2 = this.qnt2 * this.tabelaDePontos[this.item2];
        },
        verificaPontos(){
            return this.pontos1 == this.pontos2;
        },
        updateBtn(){
            this.flagBtn = true;
            this.btnTexto = "Comercializar Itens";
            this.btnImg = "fa-solid fa-right-left";
        },
        updateInventarios(flag, add){
            const val1 = this.sobreviventes[0].inventario[this.item1];
            const val2 = this.sobreviventes[1].inventario[this.item2];

            if(flag && !add && val1 < this.max1) this.sobreviventes[0].inventario[this.item1] += 1;

            if(flag && add && val1 > 0) this.sobreviventes[0].inventario[this.item1] -= 1;

            if(!flag && !add && val2 < this.max2) this.sobreviventes[1].inventario[this.item2] += 1;

            if(!flag && add && val2 > 0) this.sobreviventes[1].inventario[this.item2] -= 1;
        },
        async btnComercio(e){

            // Previnir o envio do formulário
            e.preventDefault();

            // Tentando obter os dados dos inventários
            const res1 = await this.getResponse(this.baseUrl + this.id1 + '/');
            const res2 = await this.getResponse(this.baseUrl + this.id2 + '/');

            // Carregando os dados dos inventários em tabelas se tudo OK, se não continuar como estava e não alterar o botão de comercializar
            if(this.setMsgFromStatusCode(res1, res2)){
                this.flagInputs = true;

                // Carregando os dados dos inventários
                const dados1 = await this.getDados(res1);
                const dados2 = await this.getDados(res2);

                this.sobreviventes = [dados1, dados2];

                // Alterando o botão para o de comercializar
                this.updateBtn();

                // Alterando a flag do flagBtn
                this.flagBtn = true
            }

            // Chamando a transição de apresentação da mensagem
            this.hideMsg(2000);
        }
    },
}
</script>