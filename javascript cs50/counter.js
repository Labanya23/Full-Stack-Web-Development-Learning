
//let counter = 0

if (!localStorage.getItem('counter')){
   localStorage.SetItem('counter',0);
}

function count(){
    let counterr = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter',counter);

    //if (counter%10 === 0){
        //alert('Count is now ${counter}');
    //}
}
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('h1').innerhtml = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;

    //setInterval(count, 1000);
});
