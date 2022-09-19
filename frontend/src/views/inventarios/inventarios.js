import Title from "../../components/Title.vue";
import TableHead from "../../components/TableHead.vue";
import {criarRangeDePaginacao,getRangeDePaginas} from "../../utils/paginacao.js";

export default{
    name:"Inventarios",
    components:{
        Title,
        TableHead
    },
    data(){
        return{
            titulo:"Iventários",
            fontawesome: "fa-solid fa-boxes-stacked",
            inventarios: null,
            range: null,
            primeiraPaginaForaDoRange: null,
            ultimaPaginaForaDoRange: null,
            quantPaginas: 4,
            totalDeObjetos: null,
            porPagina: 5,
            paginaAtual: null,
            totalDePaginas: null
        }
    },
    methods:{
        async getInventarios(page=1){

            const url = "http://127.0.0.1:8000/api/sobreviventes/?page=" + page;
            const req = await fetch(url);
            const dados = await req.json();

            return {
                dados: dados.results,
                totalDeObjetos: dados.count,
                next: dados.next
            }
        },
        async carregarDados(page){

            const resultado = await this.getInventarios(page);
            this.inventarios = resultado.dados;
            this.totalDePaginas = Math.ceil(resultado.totalDeObjetos / this.porPagina);

            const rangeDePaginas = getRangeDePaginas(this.totalDePaginas);
            const paginacao = criarRangeDePaginacao(rangeDePaginas, this.quantPaginas, page);

            this.range = paginacao.range;
            this.primeiraPaginaForaDoRange = paginacao.primeiraPaginaForaDoRange;
            this.ultimaPaginaForaDoRange = paginacao.ultimaPaginaForaDoRange;
        }
    },
    mounted(){
        this.carregarDados(1);
    }
}