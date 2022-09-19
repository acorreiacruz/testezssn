import Title from "../../components/Title.vue";

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
