let prom = new Promise((res, rej) => {
    console.log('Asynchronously executed');
    if(Math.random() > 0.5) {
        res('Success');
    } else {
        rej('Error')
    }
})

prom.then((val) => {
    console.log('Asynchronously exeuted: ' + val);

}).catch((err) => {
    console.log('Asynchronously executed: ' + err);
}).finally(() => {
    console.log('Promise Done executing');
});

console.log('last log');