import Title from "../../components/Title.vue";
import TableHead from "../../components/TableHead.vue";

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
        getRange(totalDePaginas){

            const array = [];

            for(let i = 1 ; i <= totalDePaginas ; i++){
                array.push(i);
            }

            return array;
        },
        criarRangeDePaginacao(rangeDePaginas, quantPaginas, paginaAtual){

            let meio = Math.ceil(quantPaginas / 2);
            let inicio = paginaAtual - meio;
            let fim = paginaAtual + meio;
            let parada = rangeDePaginas.length;
            let falta;

            falta = inicio < 0 ? Math.abs(inicio) : 0;

            if(inicio < 0){
                inicio = 0;
                fim += falta;
            }

            if(fim >= parada){
                inicio -= Math.abs(fim - parada);
            }

            return {
                primeiraPaginaForaDoRange : paginaAtual > meio,
                ultimaPaginaForaDoRange : fim < parada,
                range : rangeDePaginas.slice(inicio, fim)
            }
        },
        async carregarDados(page){

            const resultado = await this.getInventarios(page);
            console.log("Pagina", page);
            this.inventarios = resultado.dados;
            this.totalDePaginas = Math.ceil(resultado.totalDeObjetos / this.porPagina);

            // Criando a páginação da página
            const rangeDePaginas = this.getRange(this.totalDePaginas);
            const paginacao = this.criarRangeDePaginacao(rangeDePaginas, this.quantPaginas, page);
            this.range = paginacao.range;
            this.primeiraPaginaForaDoRange = paginacao.primeiraPaginaForaDoRange;
            this.ultimaPaginaForaDoRange = paginacao.ultimaPaginaForaDoRange;
        }
    },
    mounted(){
        this.carregarDados(1);
    }
}