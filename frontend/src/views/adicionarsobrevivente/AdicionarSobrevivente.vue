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
<script src="./adicionarsobrevivente.js"></script>