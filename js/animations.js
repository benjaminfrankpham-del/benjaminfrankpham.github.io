console.log("animations.js loaded");


/* =========================
   SCRAMBLE TEXT EFFECT
========================= */

function scrambleText(element, finalText, duration = 2000){

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

            }else{

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
   FEATURED PROJECT SCROLL
========================= */


function initProjects(){


    console.log("Projects loading");


    const section =
    document.querySelector(".projects-showcase");


    const header =
    document.querySelector(".projects-header");


    const projects =
    document.querySelectorAll(".project-item");


    const image =
    document.querySelector("#project-preview");


    const title =
    document.querySelector("#project-title");


    const description =
    document.querySelector("#project-description");



    if(
        !section ||
        !header ||
        !projects.length ||
        !image
    ){

        console.log("Project elements missing");

        return;

    }



    gsap.registerPlugin(ScrollTrigger);



    let current = 0;



    function updateProject(index){


        if(index === current) return;


        current = index;



        projects.forEach(item=>{

            item.classList.remove("active");

        });



        projects[index].classList.add("active");



        const newImage =
        projects[index].dataset.image;


        const newTitle =
        projects[index].dataset.title;


        const newDescription =
        projects[index].dataset.description;



        gsap.to(image,{

            opacity:0,

            y:30,

            duration:.25,


            onComplete:()=>{


                image.src = newImage;


                title.textContent = newTitle;


                description.textContent =
                newDescription;



                gsap.fromTo(image,

                {
                    opacity:0,
                    y:-30
                },

                {
                    opacity:1,
                    y:0,
                    duration:.5,
                    ease:"power3.out"
                });


            }

        });



    }




ScrollTrigger.create({

    trigger: section,

    start: "top 20px",

    end: () => "+=" + (projects.length * 800),

    pin: true,

    scrub: 1,

    anticipatePin: 1,

    onUpdate(self){

        let index = Math.floor(
            self.progress * projects.length
        );


        if(index >= projects.length){

            index = projects.length - 1;

        }


        updateProject(index);

    }

});



}







/* =========================
   PROJECT CARD TILT
========================= */


function initProjectTilt(){


    console.log("Project tilt loaded");


    const card =
    document.querySelector(".project-card");



    if(!card) return;



    card.addEventListener(
        "mousemove",
        (e)=>{


            const rect =
            card.getBoundingClientRect();



            const x =
            e.clientX - rect.left;


            const y =
            e.clientY - rect.top;



            const rotateX =
            ((y - rect.height / 2) /
            rect.height) * -15;



            const rotateY =
            ((x - rect.width / 2) /
            rect.width) * 15;



            gsap.to(card,{

                rotateX:rotateX,

                rotateY:rotateY,

                scale:1.03,

                duration:.3,

                ease:"power2.out",

                transformPerspective:1000

            });



        }
    );





    card.addEventListener(
        "mouseleave",
        ()=>{


            gsap.to(card,{

                rotateX:0,

                rotateY:0,

                scale:1,

                duration:.5,

                ease:"power3.out"

            });


        }
    );


}







/* =========================
   PAGE ANIMATIONS
========================= */


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





    gsap.from(".hero-description",{

        y:40,

        opacity:0,

        duration:1,

        delay:4

    });





    initProjects();


    initProjectTilt();



}