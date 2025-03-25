//variables
var nombre = "andres";
let apellido;
const pi = 3.1416;
/*son tipos de variables para poder utilizar en java la mas recomendable es la (let) ya que es menos facil que 
falle el documento con errores o dicho programa la variable const es para contante (se refiere a que no cambia de valor)*/

//ejemplos de fallas de var

console.log(x);//underfired
var x =1;
console.log(x);

//problemas de utilizar var y let 
//esto al inicio no te marca error pero depues de tiempo causa problemas 
var x=1
var x=3
//vamos con let 
//podria decirse que esto es mas correcto que utilizar var es mas recomendable utilizar let
let x =1
let x =2

//(escope)          (funcion), bloque {}
//(redeclaración) 
//(hoisting)

//ejemplo de bloque

/*ejemplo(){
    var x;}
    conmsole.log(x);
    ejemplo()*/