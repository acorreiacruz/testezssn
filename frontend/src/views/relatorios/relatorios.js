import Title from "../../components/Title.vue";
import TableHead from "../../components/TableHead.vue";

export default {
    name:"Relatorios",
    components:{
        Title,
        TableHead
    },
    data(){
        return{
            titulo:"Relatórios",
            fontawesome: "fa-sharp fa-solid fa-chart-column",
            url: "http://127.0.0.1:8000/api/sobreviventes/relatorio/",
            medias:{},
            infectados:null,
            naoInfectados:null
        }
    },
    methods:{
        async getRelatorioInfectados(){
            const url = this.url + 'infectados/';
            const req = await fetch(url);
            const res = await req.json();
            this.infectados = res.infectados;

        },
        async getRelatorioNaoInfectados(){
            const url = this.url + 'nao-infectados/';
            const req = await fetch(url);
            const res = await req.json();
            this.naoInfectados = res.nao_infectados;
        },
        async getRelatorioMediaDosRecursos(){
            const url = this.url + 'medias-dos-inventarios/';
            const req = await fetch(url);
            const res = await req.json();
            const dados = res.medias_dos_inventarios;
            this.medias = {...dados};
        },
    },
    mounted(){
        this.getRelatorioInfectados();
        this.getRelatorioNaoInfectados();
        this.getRelatorioMediaDosRecursos();
    }
}
