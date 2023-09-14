document.getElementById("onexb").setAttribute("onclick", "showx()");
onex = document.getElementById("onex");
onew = document.getElementById("onewin");

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