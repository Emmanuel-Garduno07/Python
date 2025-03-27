let contador = 0;

for (let i = 1; i <= 50; i++) {
    if (i % 2 === 0) {
        contador++;
    }
}

console.log("Cantidad de números pares entre 1 y 50:", contador);