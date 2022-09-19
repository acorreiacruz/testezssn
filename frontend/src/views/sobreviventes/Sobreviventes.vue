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
<script src="./sobreviventes.js"></script>
