console.log("animations.js loaded");


function scrambleText(element, finalText, duration = 2000) {

    if (!element) return;


    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    let start = null;


    function animate(time) {


        if (!start) start = time;


        let progress = (time - start) / duration;


        let revealed = Math.floor(progress * finalText.length);


        let output = "";


        for(let i = 0; i < finalText.length; i++){


            if(i < revealed){

                output += finalText[i];

            }
            else if(finalText[i] === " "){

                output += " ";

            }
            else{

                output += chars[Math.floor(Math.random() * chars.length)];

            }

        }


        element.innerHTML = output;



        if(progress < 1){

            requestAnimationFrame(animate);

        }
        else{

            element.innerHTML = finalText;

        }

    }


    requestAnimationFrame(animate);

}




function initAnimations(){


    console.log("initAnimations running");



    gsap.from(".menu-btn",{

        y:-50,

        opacity:0,

        duration:1

    });



    gsap.from(".hero-tag",{

        x:-100,

        opacity:0,

        duration:1,

        delay:.3

    });



    const name = document.querySelector(".hero h1");

    const title = document.querySelector(".hero h2");



    // make visible

    gsap.set(name,{
        opacity:1
    });


    gsap.set(title,{
        opacity:1
    });



    // START NAME

    scrambleText(

        name,

        "Benjamin Pham",

        2500

    );



    // START TITLE AFTER NAME


    setTimeout(()=>{


        scrambleText(

            title,

            "Cybersecurity Analyst",

            2500

        );


    },1500);





    gsap.from(".hero-description",{

        y:40,

        opacity:0,

        duration:1,

        delay:4

    });


}