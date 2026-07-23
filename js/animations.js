console.log("animations.js loaded");



/* =========================
   SCRAMBLE TEXT EFFECT
========================= */


function scrambleText(element, finalText, duration = 2000) {


    if(!element) return;


    const chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";


    let frame = 0;


    const totalFrames = duration / 50;



    const interval = setInterval(()=>{


        let output = "";



        for(let i = 0; i < finalText.length; i++){


            if(i < (frame / totalFrames) * finalText.length){


                output += finalText[i];


            }
            else{


                output += chars[
                    Math.floor(Math.random() * chars.length)
                ];


            }


        }



        element.innerHTML = output;


        frame++;



        if(frame >= totalFrames){


            clearInterval(interval);


            element.innerHTML = finalText;


        }


    },50);


}







/* =========================
   HORIZONTAL PROJECT SCROLL
========================= */


function initProjectScroll(){


    console.log("Project scroll loading");



    const track =
    document.querySelector(".projects-track");



    if(!track){

        console.log("No project track found");

        return;

    }



    if(typeof ScrollTrigger === "undefined"){


        console.log("ScrollTrigger missing");


        return;


    }




    gsap.registerPlugin(ScrollTrigger);




    let amount =
    track.scrollWidth - window.innerWidth;




    gsap.to(track,{


        x:-amount,


        ease:"none",



        scrollTrigger:{


            trigger:".projects-section",


            start:"top top",



            end:()=>"+=" + amount,



            scrub:1,



            pin:true,



            anticipatePin:1



        }


    });



}








/* =========================
   PAGE ANIMATIONS
========================= */


function initAnimations(){


    console.log("initAnimations running");




    // MENU BUTTON


    gsap.from(".menu-btn",{


        y:-50,


        opacity:0,


        duration:1


    });







    // HERO TAG


    gsap.from(".hero-tag",{


        x:-100,


        opacity:0,


        duration:1,


        delay:.3


    });







    // HERO TEXT


    const name =
    document.querySelector(".hero h1");


    const title =
    document.querySelector(".hero h2");






    if(name){


        gsap.set(name,{

            opacity:1

        });



        scrambleText(

            name,

            "Benjamin Pham",

            2000

        );


    }







    if(title){


        gsap.set(title,{

            opacity:1

        });



        setTimeout(()=>{


            scrambleText(

                title,

                "Cybersecurity Analyst",

                2000

            );


        },1800);



    }








    // HERO DESCRIPTION


    gsap.from(".hero-description",{


        y:40,


        opacity:0,


        duration:1,


        delay:4



    });






    // START PROJECT SCROLL


    initProjectScroll();



}