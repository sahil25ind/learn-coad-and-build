// take user input (html) make it look nice (css) use if to compare the ages.
// according to age let them enter or not do it by printing on console.

const sub = document.getElementById("sub");
const reset = document.getElementById("reset");
const txt = document.getElementById("txt");
let dis1 = document.getElementById("dis1");
let dis2 = document.getElementById("dis2");

let distxt;



sub.onclick=function()
{
distxt= txt.value;
distxt=Number(distxt);


console.log(distxt, typeof distxt);


if(distxt >= 18)
	{
		if(distxt <= 60){
		dis1.textContent=`you are eligable to enter this site.`;
		dis2.textContent=`you are 18+ .`;

		}
		else if(distxt <= 80 && distxt > 60){

		dis1.textContent=`you are eligable to enter this site.`;
		dis2.textContent=`not recemended at your age old man.`;

		}
		else if(distxt < 100 && distxt > 80){
		
		dis1.textContent=`you are TOO OLD to enter this site gramps.`;
		dis2.textContent=`   `;

		}
		else if(distxt >= 100){

		dis1.textContent=`you are already on your death door why are you tying to enter this site.`;
		dis2.textContent=`go rest up you might strangle yourself!`;
		}

	}

    else{
		if(distxt < 18 && distxt > 0){

		dis1.textContent=`you are not eligable to enter this site.`;
		dis2.textContent=`you age is below 18.`;
		}
		else if(distxt == 0){

		dis1.textContent=`you cant enter this site.`;
		dis2.textContent=`i mean you were just born.`;
		}
		else if(distxt < 0){
		
		dis1.textContent=`you can't be below 0`;
		dis2.textContent=``;
		}

	 }

}

reset.onclick=function(){
	
	txt.value=``;
	distxt = 0;
	dis1.textContent=``;
	dis2.textContent=``;


}