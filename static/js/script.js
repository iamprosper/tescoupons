document.getElementById("onexb").setAttribute("onclick", "showx()");
onex = document.getElementById("onex");
onew = document.getElementById("onewin");

copy_btn = document.querySelector('#copy_btn');

copy_btn.addEventListener('click', ()=>{
    const active_coupon = document.querySelector('.carousel-item.active')
    if (active_coupon){
        const codeElement = active_coupon.querySelector('.coupon_code');
        if (codeElement){
            const code = codeElement.textContent;
            console.log(code);
            navigator.clipboard.writeText(code).then(() =>{
                console.log("Text copied to clipboard");
                copy_btn.textContent = "Code copié"
                setTimeout(() =>{
                    copy_btn.textContent = "Copier";
                }, 2000);
            }).catch(err => {
                console.error('Could not copy error');
            });
            // copyToClipboard(code);
        }
    }
});

/*function copyToClipboard(text){
    const input = document.createElement('textarea');
    input.value = text;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
}*/
// var modal = document.getElementById("modal");
// var buttons = document.querySelectorAll(".modal-button");
// var modalContent = document.getElementById("modal-content-details");
//
// buttons.forEach(function (button){
//     button.addEventListener("click", function (){
//         var week = button.getAttribute("data-week");
//         var day = button.getAttribute("data-day");
//         var codes = coupons_imgs[week][day];
//
//         modalContent.innerHTML = codes;
//
//         modal.style.display = "block";
//     });
// });
//
// var closeButton = document.querySelector(".close");
// closeButton.addEventListener("click", function (){
//     modal.style.display = "none";
// });

var mediaQuery = window.matchMedia("(min-width: 991.5px)")

function showx(){
    if (!mediaQuery.matches){
        onex.style.display = "flex";
        onew.style.display = "none"; 
    }
    else{
        console.log('Wide screen detected') 
    }
}

document.getElementById("onewb").setAttribute("onclick", "shown()");

function shown(){
    if (!mediaQuery.matches){
        onew.style.display = "flex";
        onex.style.display = "none"; 
    }
    else{
        console.log('Wide screen detected')
    }
}



if (mediaQuery.matches) {
    console.log("Wide screen")
} else {
    console.log("Not met")
}

function handleMediaQueryChange(mediaQuery) {
    if (mediaQuery.matches) {
        onex.style.display = "flex";
        onew.style.display = "flex";
    } else {
        onex.style.display = "flex"
        onew.style.display = "None";
    }
}

mediaQuery.addListener(handleMediaQueryChange);

handleMediaQueryChange(mediaQuery);