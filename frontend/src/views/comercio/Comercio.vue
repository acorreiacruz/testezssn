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

<script src="./comercio.js"></script>
