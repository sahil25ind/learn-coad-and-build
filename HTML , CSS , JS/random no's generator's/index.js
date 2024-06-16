//random number generator but just in code though

const toshbtn=document.getElementById("toshbtn");
const reset=document.getElementById("reset");
let h1=document.getElementById("h1");
let h2=document.getElementById("h2");
let h3=document.getElementById("h3");
let RandomNum1;
let RandomNum2;
let RandomNum3;
const setzero = 0;
const max=89;
const min=10;

toshbtn.onclick=function(){
RandomNum1=Math.round(Math.random()*max)+min;
RandomNum2=Math.round(Math.random()*max)+min;
RandomNum3=Math.round(Math.random()*max)+min;

h1.textContent=RandomNum1;
h2.textContent=RandomNum2;
h3.textContent=RandomNum3;
}

reset.onclick=function(){
h1.textContent=setzero;
h2.textContent=setzero;
h3.textContent=setzero;
}