var purple = document.getElementById(".desc .e-heading"); 

function recolor()
{  
    var a = document.getElementsByClassName("e-heading");
    
    for (var i=0; i<a.length; i++) a[i].style.color = '#732673';

    document.getElementById("test").style.color='#732673';
    document.body.style.backgroundImage = "url('./img/violet.jpg')";
    
}
function recolor2()
{
    var a = document.getElementsByClassName("e-heading");
    for (var i=0; i<a.length; i++) a[i].style.color = '#e74c3c';
    document.getElementById("test").style.color='#e74c3c';
        
    document.body.style.backgroundImage = "url(./img/bg.jpg)";
}