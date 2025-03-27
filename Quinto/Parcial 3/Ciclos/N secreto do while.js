let i=0, secreto=1;
do { 
    if(i==secreto){
        i=secreto;
        break
    }
    i++;
} while(i<1000);
console.log("el numero secreto es",i);