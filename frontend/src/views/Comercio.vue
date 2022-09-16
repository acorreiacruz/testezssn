<template>
    <div class="main-container">
        <div class="container">
            <Title :titulo="titulo" :fontawesome="fontawesome"/>
        </div>
        <div class="main-form-container">
            <form action="#" @submit="buscarInventarios">
                <div class="form-container">
                    <div class="input-container comercio">
                        <label for="survivor01">Id Sobrevivente 1:</label>
                        <input type="number" id="survivor01" min="1" v-model="id1">
                    </div>
                    <div class="input-container">
                        <label for="survivor01">Id Sobrevivente 2:</label>
                        <input type="number" id="survivor01" min="1" v-model="id2">
                    </div>
                    <div v-show="flagInputs" class="input-container">
                        <label for="item1">Item do Sobrevivente 1:</label>
                        <select name="item1" id="item1" v-model="item1" @change="alterarPontos">
                            <option value="">Selecione um item</option>
                            <option value="agua">Água</option>
                            <option value="alimentacao">Alimentação</option>
                            <option value="medicacao">Medicação</option>
                            <option value="municao">Munição</option>
                        </select>
                    </div>
                    <div v-show="flagInputs" class="input-container">
                        <label for="item2">Item do Sobrevivente 2:</label>
                        <select name="item2" id="item2" v-model="item2" @change="alterarPontos">
                            <option value="">Selecione um item</option>
                            <option value="agua">Água</option>
                            <option value="alimentacao">Alimentação</option>
                            <option value="medicacao">Medicação</option>
                            <option value="municao">Munição</option>
                        </select>
                    </div>
                    <div v-show="flagInputs" class="input-container">
                        <label for="qnt1">Quantidade do Item 1:</label >
                        <input type="number" id="qnt1" min="0" name="qnt1" v-model="qnt1" @change="alterarPontos">
                    </div>
                    <div v-show="flagInputs" class="input-container">
                        <label for="qnt2">Quantidade do Item 2:</label>
                        <input type="number" id="qnt2" min="0" name="qnt2" v-model="qnt2" @change="alterarPontos">
                    </div>
                    <div v-show="flagInputs" class="input-container">
                        <button>Pontuação Total 1 = {{pontos1}}</button>
                    </div>
                    <div v-show="flagInputs" class="input-container">
                        <button>Pontuação Total 2 = {{pontos2}}</button>
                    </div>
                </div>
                <div class="inventarios-container">
                        <div class="inventario" v-for="sobrevivente in sobreviventes" :key="sobrevivente.id">
                            <p class="inventario-title">Inventário do Sobrevivente de Id {{sobrevivente.id}}</p>
                            <div class="grid-inventario">
                                <div class="inventario-item">Água: {{sobrevivente.inventario.agua}}</div>
                                <div class="inventario-item">Alimentação: {{sobrevivente.inventario.alimentacao}}</div>
                                <div class="inventario-item">Medicação: {{sobrevivente.inventario.medicacao}}</div>
                                <div class="inventario-item">Munição: {{sobrevivente.inventario.municao}}</div>
                            </div>
                        </div>
                </div>
                <div class="button-container">
                    <div class="btn-save">
                        <button type="submit" @click="btnComercio">
                            <i :class="btnImg"></i> {{btnTexto}}
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import Title from "../components/Title.vue";
export default {
    name:"Comercio",
    components:{
        Title
    },
    data(){
        return {
            titulo:"Comércio",
            btnTexto: "Buscar Inventários",
            btnImg:"fa-sharp fa-solid fa-magnifying-glass",
            flagInputs:false,
            fontawesome: "fa-solid fa-cart-shopping",
            id1:null,
            item1:null,
            qnt1:null,
            id2:null,
            item2:null,
            qnt2:null,
            sobreviventes: null,
            tabelaDePontos:{
                agua:5,
                alimentacao:4,
                medicacao:3,
                municao:2,
            },
            pontos1: null,
            pontos2: null,
            contador: 0,
        }
    },
    methods:{
        async buscarInventarios(e){
            e.preventDefault();
            const url1 = `http://127.0.0.1:8000/api/sobreviventes/${this.id1}`;
            const req1 = await fetch(url1);
            const sobrevivente1 = await req1.json();

            const url2 = `http://127.0.0.1:8000/api/sobreviventes/${this.id2}`;
            const req2 = await fetch(url2);
            const sobrevivente2 = await req2.json();

            this.flagInputs = true;
            this.btnTexto = "Realizar Troca"
            this.btnImg = "fa-solid fa-arrow-right-arrow-left"

            this.sobreviventes = [sobrevivente1, sobrevivente2];
        },
        async realizarTroca(){
            const url = `http://127.0.0.1:8000/api/sobreviventes/trocas/${this.id1}/${this.item1}/${this.qnt1}/${this.id2}/${this.item2}/${this.qnt2}/`;
            const req = await fetch(url);
            const res = await req.json();
            console.log(res);
        },
        alterarPontos(){
            this.pontos1 = this.qnt1 * this.tabelaDePontos[this.item1];
            this.pontos2 = this.qnt2 * this.tabelaDePontos[this.item2];
        },
        btnComercio(){
            if(this.contador == 2){
                this.realizarTroca();
            }else{
                this.contador += 1;
            }
        }
    },
}
</script>