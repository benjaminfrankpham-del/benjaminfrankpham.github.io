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
   PROJECT SHOWCASE SCROLL
========================= */

function initProjects(){

    console.log("Project showcase loading");


    const section = document.querySelector(".projects-showcase");

    const header = document.querySelector(".projects-header");

    const projects = document.querySelectorAll(".project-item");

    const image = document.querySelector(".project-image img");



    if(!section || !header || !projects.length || !image){

        console.log("Projects missing");

        return;

    }



    if(typeof ScrollTrigger === "undefined"){

        console.log("ScrollTrigger missing");

        return;

    }



    gsap.registerPlugin(ScrollTrigger);



    let currentProject = 0;



    image.src = projects[0].dataset.image;

    projects[0].classList.add("active");





    function changeProject(index){


        if(index === currentProject) return;


        currentProject = index;



        projects.forEach(project=>{

            project.classList.remove("active");

        });



        projects[index].classList.add("active");



        gsap.to(image,{

            opacity:0,

            y:40,

            duration:.25,


            onComplete:()=>{


                image.src =
                projects[index].dataset.image;



                gsap.fromTo(image,

                {

                    opacity:0,

                    y:-40

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


        trigger:header,


        start:"top 40px",


        end:()=>"+=" + (projects.length * 650),


        pin:section,


        scrub:true,



        onUpdate:(self)=>{


            let index = Math.floor(

                self.progress * projects.length

            );



            if(index >= projects.length){

                index = projects.length - 1;

            }



            changeProject(index);


        }



    });



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

    const name = document.querySelector(".hero h1");
    const title = document.querySelector(".hero h2");

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

}