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
            console.log("formulario");
            console.log(form);
            console.log("formulario");
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            console.log("toke");
            console.log(token);
            console.log("fim_toke");
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
            ajax.send(data);
            // form.load();
            // form.reset();
        }
        form.addEventListener('submit', sendForm, false);
    }

    if (doc.querySelector('#form')) {
        let form = doc.querySelector('#form');
    
        function sendForm(event) {
            event.preventDefault();
    
            let formData = {
                modelo: form.querySelector('#id_modelo').value,
                marca: form.querySelector('#id_marca').value,
                ano: form.querySelector('#id_ano').value
            };

            console.log(formData);
            
            fetch(form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRF-TOKEN': form.querySelector('input[name="csrfmiddlewaretoken"]').value
                },
                body: JSON.stringify(formData)
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Erro ao enviar os dados. Por favor, tente novamente.');
                }
            })
            .then(data => {
                let result = doc.querySelector('#result');
                result.innerHTML = 'Operação realizada com Sucesso!';
                result.classList.add('alert');
                result.classList.add('alert-success');
            })
            .catch(error => {
                console.error('Erro:', error);
                alert(error.message);
            });
    
            form.reset();
        }
    
        form.addEventListener('submit', sendForm);
    }

    //Filtro de busca
    let filtro = doc.querySelectorAll('input');
    // console.log(filtro[2].value);
})(window, document);
