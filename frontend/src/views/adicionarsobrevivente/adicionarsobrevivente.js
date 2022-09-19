import Title from "../../components/Title.vue";
import Mensagem from "../../components/Mensagem.vue";

export default {
    name:"AdicionarSobrevivente",
    components:{
        Title,
        Mensagem
    },
    data(){
        return{
            titulo:"Adicionar Sobrevivente",
            fontawesome:"fa-solid fa-user",
            nome:null,
            idade:null,
            latitude:null,
            longitude:null,
            sexo:null,
            agua:null,
            alimentacao:null,
            medicacao:null,
            municao:null,
            flagMsg: false,
            msg: null
        }
    },
    methods:{
        gerarObjeto(){
            return {
                nome:this.nome,
                idade:this.idade,
                ultimo_local:{
                    latitude:this.latitude,
                    longitude:this.longitude,
                },
                sexo:this.sexo,
                inventario:{
                    agua:this.agua,
                    alimentacao:this.alimentacao,
                    medicacao:this.medicacao,
                    municao:this.municao
                }
            }
        },
        showMsg(msg){
            this.flagMsg = true;
            this.msg = msg;
        },
        removerMsg(time=2000){
            setTimeout(()=>{
                this.flagMsg = false;
            }, time);
        },
        limparCampos(){
            this.nome = null;
            this.idade = null;
            this.latitude = null;
            this.longitude = null;
            this.sexo = null;
            this.agua = null;
            this.alimentacao = null;
            this.medicacao = null;
            this.municao = null;
        },
        async criarSobrevivente(e){
            e.preventDefault();

            const sobrevivente = this.gerarObjeto();
            const dataJSON = JSON.stringify(sobrevivente);

            const req = await fetch(
                "http://127.0.0.1:8000/api/sobreviventes/",
                {
                    method:"POST",
                    headers:{'Content-type':'application/json'},
                    body: dataJSON
                }
            );

            const res = await req.json();

            this.showMsg("Sobrevivente cadastrado com sucesso!");

            this.limparCampos();
            this.removerMsg();
        },
    }
}
