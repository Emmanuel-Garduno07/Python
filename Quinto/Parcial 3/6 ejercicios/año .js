// Programa para verificar si un año es bisiesto o no

let anio =1800

if ((anio % 4 === 0 && anio % 100 !== 0) || (anio % 400 === 0)) {
    console.log(anio + " es un año bisiesto.");
} else {
    console.log(anio + " no es un año bisiesto.");
}