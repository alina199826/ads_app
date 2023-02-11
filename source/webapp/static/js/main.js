function onButtonClickClose() {
    let div2 = document.getElementById('change');
    let child = div2.children[0];
    div2.removeChild(child);
}

async function buttonClick(event) {
        let target = event.target;
        let url = target.dataset['indexLink'];
        let response = await fetch(url);
        let index_text = await response.json();
    console.log(index_text);

        let div = document.createElement('div');
        div.className='alert';
        div.innerHTML= `<strong>Обьявление ${index_text['data']} изменено</strong><button class='button'  onclick='onButtonClickClose()'><i class='bi bi-x-circle'></i></button>`;
        let div2 = document.getElementById('change');
        div2.appendChild(div);
        setTimeout(onButtonClickClose, 5000);
    }

    async function onLoad(){

        const button = document.querySelectorAll([id="button"]);
        if(button){
        for(let i of button){
            i.onclick = buttonClick;
        }
        }
    }
    window.addEventListener('load', onLoad);


