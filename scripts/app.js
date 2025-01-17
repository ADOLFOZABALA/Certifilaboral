function captura(){
    let nombreest= document.getElementById("user").value;
    let celest= document.getElementById("password").value;
    

if (nombreest==""){
    alert("Este campo no puede quedar vacio")
    document.getElementById("user").focus();
}else{
    if (celest==""){
        alert("Este campo no puede quedar vacio")
        document.getElementById("password").focus();
}else{
    console.log (nombreest+" "+celest);
    document.getElementById("user").value="";
    document.getElementById("password").value="";
    document.getElementById("user").focus();


}
}
}