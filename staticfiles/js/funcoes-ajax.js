function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}

function naoutilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/naoutilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
            
        }
    });
}

function atualizaPainel(){
    console.log(id);
    token = "teste";

    $.ajax({
        type: 'GET',
        url: '/core/index.html/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#painel1").text(result.painel1);
            $("#painel2").text(result.painel2);
            $("#painel3").text(result.painel3);
            
        }
    });
}