let txt="BYE BYE hope to see you again :) !";
let i=0;
let speed= 70;

function Typewriter() {

        if (i < txt.length) {
            document.getElementById("BYE").innerHTML += txt.charAt(i);
            i++;
            setTimeout(Typewriter, speed);
        }
    }
