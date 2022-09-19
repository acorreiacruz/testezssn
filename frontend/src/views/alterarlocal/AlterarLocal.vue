<template>
<div class="main-container">
    <div class="container">
        <Title :titulo="titulo" :fontawesome="fontawesome" />
        <div class="main-form-container">
            <form method="post" @submit="updateLocal">
                <div class="form-container">
                    <div class="input-container">
                        <label for="latitude">Latitude:</label>
                        <input type="number" id="latitude" min="-90" max="90" v-model="latitude">
                    </div>
                    <div class="input-container">
                        <label for="longitude">Longitude:</label>
                        <input type="number" id="longitude" min="-180" max="180" v-model="longitude">
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
<script src="./alterarlocal.js"></script>