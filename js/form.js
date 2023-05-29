//FORMULARIO DE CONTACTO

function habilitar(){
    campo1 = document.getElementById("campo1").value;
    campo2 = document.getElementById("campo2").value;
    campo3 = document.getElementById("campo3").value;
    val = 0;
    
    if(campo1 == ""){
        val++; 
    }
    if(campo2 == ""){
        val++; 
    }
    if(campo3 == ""){
        val++; 
    }
    
    if(val == 0){
        document.getElementById("enviar").disabled = false;
    }else{
        document.getElementById("enviar").disabled = true;
    }
     
    }
    
    document.getElementById("campo1").addEventListener("keyup", habilitar);
    document.getElementById("campo2").addEventListener("keyup", habilitar);
    document.getElementById("campo3").addEventListener("keyup", habilitar);