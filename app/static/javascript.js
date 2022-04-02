(function(win,doc){
    'use strict'
    //verifica se o usuario quer mesmo deletar a informação
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i<btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('deseja mesmo apagar esse dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            })
        }
    }

    //Ajax do Form

    if(doc.querySelector('#form')){                 //pesquisa se tem form
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
        event.preventDefault(); //previne o comportamento padrão do formulario
        let data = new FormData(form); //api do formulario que vai facilitar o envio do formulario
        let ajax = new XMLHttpRequest(); //inicia o AJAX
        let token = doc.querySelectorAll('input')[0].value; //seta o token do formulário, se nao setar o django por segurança bloqueia o envio
        ajax.open('POST', form.action); //são as ações do nosso formulario
        ajax.setRequestHeader('X-CSRF-TOKEN', token); //token do nosso formulario
        ajax.onreadystatechange = function(){
            if(ajax.status === 200 && ajax.readyState ===4){
            let result = doc.querySelector('#result');
            result.innerHTML = "Operação realizada com sucesso!"
            result.classList.add('alert');
            result.classList.add('alert-success');
            }
        }
        ajax.send(data); //Envia tudo que foi capturado (imput) na função 'let data'
        form.reset();
        }
        form.addEventListener('submit', sendForm, false)
    }
}) (window,document);