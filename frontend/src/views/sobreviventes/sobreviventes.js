import Title from "../../components/Title.vue";
import TableHead from "../../components/TableHead.vue";
import Mensagem from "../../components/Mensagem.vue";

export default {
    name:"Sobreviventes",
    components:{
    Title,
    TableHead,
    Mensagem,
    Mensagem
},
    data(){
        return{
            titulo:"Sobreviventes",
            fontawesome: "fa-solid fa-users",
            sobreviventes: null,
            msg:null,
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
        async getSobreviventes(page=1){

            const url = "http://127.0.0.1:8000/api/sobreviventes/?page=" + page;
            const req = await fetch(url)
            const dados = await req.json();

            return {
                dados: dados.results,
                totalDeObjetos: dados.count,
                next: dados.next
            }
        },
        async denunciarSobrevivente(id){

            const url = `http://127.0.0.1:8000/api/sobreviventes/${id}/denunciar/`;
            const res = await fetch(url);

            if(res == 201){
                this.msg = "Denúncia de infectado realizada com sucesso!";
            }
        },
        verificaPrompt(sobreviventeId){

            let id = prompt("Informe o id do sobrevivente a ser denunciado!");

            if(id == null) return null;

            id = Number(id);

            while(id <= 0 || isNaN(id) || id==sobreviventeId){
                id = prompt("Você precica inserir um id válido e um sobrevivente não pode denunciar ele mesmo!");
                if(id == null) return null;
                id = Number(id);
            }

            return id;
        },
        popUp(sobrevivente){
            if(sobrevivente.infectado){
                alert("Um zumbie não pode realizar uma denúncia!");
            }
            else{
                const id = this.verificaPrompt(sobrevivente.id);
                if(id){
                    this.denunciarSobrevivente(id);
                }
            }
        },
        getInventario(sobrevivente){
            const msg = `
                Inventario do Sobrevivente ${sobrevivente.id}:
                    Água: ${sobrevivente.inventario.agua},
                    Alimentação: ${sobrevivente.inventario.alimentacao},
                    Medicação: ${sobrevivente.inventario.medicacao},
                    Munição: ${sobrevivente.inventario.municao}
            `;
            alert(msg);
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

            const resultado = await this.getSobreviventes(page);
            this.sobreviventes = resultado.dados;
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