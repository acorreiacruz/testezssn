<template>
    <header class="header-container">
        <h1 class="header-title">ZSSN</h1>
        <div class="menu-container">
            <div class="link-container">
                <router-link id="sobreviventes" to="/" @click="botaoAtual($event)">Sobreviventes</router-link>
            </div>
            <div class="link-container">
                <router-link id="inventarios" to="/inventarios" @click="botaoAtual($event)">Inventários</router-link>
            </div>
            <div class="link-container">
                <router-link id="comercio" to="/comercio" @click="botaoAtual($event)">Comércio</router-link>
            </div>
            <div class="link-container">
                <router-link id="relatorios" to="/relatorios" @click="botaoAtual($event)">Relatórios</router-link>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name:"NavBar",
    data(){
        return {
            flag: true,
            anterior: null,
        }
    },
    methods:{
        botaoAtual(e){
            const el = e.target;
            if(!this.anterior){
                el.style.backgroundColor = "rgb(36, 36, 36)";
                this.anterior = el.id;
            }
            const anterior = document.getElementById(this.anterior);
            anterior.style.backgroundColor = "rgb(0, 0, 0)";
            el.style.backgroundColor = "rgb(36, 36, 36)";
            this.anterior = el.id;
        }
    },
}
</script>
