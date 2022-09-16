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

<script>
import Title from "../components/Title.vue";
export default {
    name:"AlterarLocal",
    components:{
        Title,
    },
    data(){
        return {
            titulo:"Alterar Local",
            fontawesome:"fa-sharp fa-solid fa-map-location-dot",
            latitude: null,
            longitude: null,
            id: this.$route.query.id
        }
    },
    methods:{
        async getLocal(){
            const url = `http://127.0.0.1:8000/api/sobreviventes/${this.id}/`;
            const req = await fetch(url);
            const res = await req.json();
            this.latitude = res.ultimo_local.latitude;
            this.longitude= res.ultimo_local.longitude;
        },
        async updateLocal(e){

            e.preventDefault();

            const dadosJSON = JSON.stringify({
                latitude: this.latitude,
                longitude: this.longitude
            })

            console.log(dadosJSON);

            const url = `http://127.0.0.1:8000/api/sobreviventes/${this.id}/`;
            const req = await fetch(
                url,
                {
                    method:"PATCH",
                    headers:{"Content-Type" : "application/json"},
                    body: dadosJSON
                }
            );

            const res = await req.json();
            console.log('Resposta', res);
            this.$router.push('/');
        }
    },
    mounted(){
        this.getLocal();

    }
}
</script>