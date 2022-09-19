function criarRangeDePaginacao(rangeDePaginas, quantPaginas, paginaAtual){
    let meio = Math.ceil(quantPaginas / 2);
    let inicio = paginaAtual - meio;
    let fim = paginaAtual + meio;
    let parada = rangeDePaginas.length;
    let offset;

    offset = inicio < 0 ? Math.abs(inicio) : 0;

    if(inicio < 0){
        inicio = 0;
        fim = fim + offset;
    }

    if(fim >= parada){
        inicio -= Math.abs(fim - parada);
    }

    return {
        range: rangeDePaginas.slice(inicio, fim),
        primeiraPaginaForaDoRange: paginaAtual > meio,
        ultimaPaginaForaDoRange: fim < parada
    }
}

function getRangeDePaginas(totalDePaginas){
    const array = [];

    for(let i = 1 ; i <= totalDePaginas ; i++){
        array.push(i);
    }

    return array;
}

export {criarRangeDePaginacao, getRangeDePaginas};