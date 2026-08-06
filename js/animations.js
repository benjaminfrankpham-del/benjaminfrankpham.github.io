console.log("animations.js loaded");



/* =========================
   GLOBAL ACTIVE PROJECT
========================= */

let activeProject = null;




/* =========================
   SCRAMBLE TEXT EFFECT
========================= */

function scrambleText(element, finalText, duration = 900){

    if(!element) return;

    const chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    let frame = 0;

    const intervalTime = 25;
    const totalFrames = duration / intervalTime;

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

        element.textContent = output;

        frame++;

        if(frame >= totalFrames){

            clearInterval(interval);

            element.textContent = finalText;

        }

    }, intervalTime);

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



    let current = -1;



    function updateProject(index){


        if(index === current) return;


        current = index;



        projects.forEach(item=>{

            item.classList.remove("active");

        });



        const selectedProject =
        projects[index];

        activeProject = selectedProject;



        selectedProject.classList.add("active");



        // SAVE CURRENT PROJECT


        const newImage =
        selectedProject.dataset.image;


        const newTitle =
        selectedProject.dataset.title;


        const newDescription =
        selectedProject.dataset.description;

        const newLink =
selectedProject.dataset.link;

// activeProject = {
//    image: newImage,
//    title: newTitle,
//    description: newDescription,
//    link: newLink
//};



        gsap.to(image,{

            opacity:0,

            y:30,

            duration:.25,


            onComplete:()=>{


                image.src = newImage;


                title.textContent =
                newTitle;


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





    // LOAD FIRST PROJECT

    updateProject(0);




    ScrollTrigger.create({

        trigger: section,

        start:"top 20px",

        end:()=>"+=" + (projects.length * 800),

        pin:true,

        scrub:1,

        anticipatePin:1,


        onUpdate(self){


            let index =
            Math.floor(
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
   PROJECT DETAILS POPUP
========================= */


function initProjectDetails(){


    console.log("Project details loaded");


    const button =
    document.querySelector("#project-details-btn");


    const modal =
    document.querySelector(".project-modal");



    if(!button || !modal){

        console.log("Modal missing");

        return;

    }




    function setText(id,value){

        const element =
        document.querySelector(id);


        if(element){

            element.textContent =
            value || "";

        }

    }

    function setHTML(id, value){

    const element =
    document.querySelector(id);

    if(element){

        element.innerHTML =
        value || "";

    }

}






    button.addEventListener("click",()=>{


        if(!activeProject){

            console.log("No active project");

            return;

        }




        const data =
        activeProject.dataset;





        // IMAGE

        const modalImage =
        document.querySelector("#modal-image");


        if(modalImage){

            modalImage.src =
            data.image;

        }





        // TEXT SECTIONS

        setText(
            "#modal-title",
            data.title
        );


        setText(
            "#modal-description",
            data.description
        );


        setText(
            "#modal-intro",
            data.intro
        );


        setText(
            "#modal-challenges",
            data.challenges
        );


        setText(
            "#modal-solution",
            data.solution
        );


       setHTML(
    "#modal-features",
    data.features
);


        setText(
            "#modal-learned",
            data.learned
        );







        // TECH STACK TAGS

        const tech =
        document.querySelector("#modal-tech");



        if(tech){


            tech.innerHTML = "";



            if(data.tech){


                data.tech
                .split("|")
                .forEach(item=>{


                    const tag =
                    document.createElement("span");


                    tag.textContent =
                    item.trim();


                    tech.appendChild(tag);


                });


            }


        }






        // BUTTON LINK

        const modalButton =
        document.querySelector("#modal-link");



        if(modalButton){

            modalButton.href =
            data.link || "#";

        }







        // OPEN MODAL

        modal.classList.add("active");



        modal.classList.add("active");



    });








    // Close when clicking outside the popup
modal.addEventListener("click",(e)=>{

    if(e.target === modal){

        modal.classList.remove("active");

    }

});

document.addEventListener("keydown",(e)=>{

    if(e.key === "Escape"){

        modal.classList.remove("active");

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
        duration:0.8
    });

    gsap.from(".hero-tag",{
        x:-80,
        opacity:0,
        duration:0.8,
        delay:0.2
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
            900
        );

    }

    if(title){

        gsap.set(title,{
            opacity:1
        });

        scrambleText(
            title,
            "Cybersecurity Analyst",
            900
        );

    }

    gsap.from(".hero-description",{
        y:30,
        opacity:0,
        duration:0.8,
        delay:1
    });

    initProjects();
    initProjectDetails();
    initProjectTilt();

}

/* =========================
   HIDE SCROLL INDICATOR AT CONTACT
========================= */

const scrollIndicator = document.querySelector(".scroll-indicator");
const contactSection = document.querySelector("#contact");

if (scrollIndicator && contactSection) {

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                gsap.to(scrollIndicator, {
                    opacity: 0,
                    y: 20,
                    duration: 0.4,
                    pointerEvents: "none"
                });

            } else {

                gsap.to(scrollIndicator, {
                    opacity: 1,
                    y: 0,
                    duration: 0.4,
                    pointerEvents: "auto"
                });

            }

        });

    }, {
        threshold: 0.2
    });

    observer.observe(contactSection);

}

