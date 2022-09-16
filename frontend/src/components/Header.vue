<template>
    <header class="header-container">
        <h1 class="header-title">ZSSN</h1>
        <div class="menu-container">
            <div class="link-container">
                <router-link to="/">Sobreviventes</router-link>
            </div>
            <div class="link-container">
                <router-link to="/inventarios">Inventários</router-link>
            </div>
            <div class="link-container">
                <router-link to="/comercio">Comércio</router-link>
            </div>
            <div class="link-container">
                <router-link to="/relatorios">Relatórios</router-link>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name:"NavBar",
    data(){
        return {
            link_sobreviventes: "#",
            link_inventarios: "#",
            link_comercio: "#",
            link_relatorios: "#"
        }
    }
}
</script>
