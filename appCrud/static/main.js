(function(win, doc){
    'use-strict';
    //Verifica se o usuario realmente quer apagar o dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i = 0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja realmente deletar os dados?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }
    //Ajax do form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {   
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.onreadystatechange = function(){
                if(ajax.status === 200 && ajax.readyState === 4){
                    //console.log('Cadastrou!');
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Operação realizada com Sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                    
                }
            }
            console.log(form);
            ajax.send(data);
            form.load();
            form.reset();
        }
        form.addEventListener('submit', sendForm, false);
    }
    //Filtro de busca
    let filtro = doc.querySelectorAll('input');
    // console.log(filtro[2].value);
})(window, document);
