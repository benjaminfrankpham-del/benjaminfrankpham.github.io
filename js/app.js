document.addEventListener("DOMContentLoaded", () => {

    console.log("APP STARTED");


    if(typeof initBackground === "function"){
        initBackground();
    }


    if(typeof initCursor === "function"){
        initCursor();
    }


    if(typeof initMenu === "function"){
        initMenu();
    }


    if(typeof initAnimations === "function"){
        initAnimations();
    }


});

const sendButton = document.querySelector(".send-button");


if(sendButton){

    sendButton.addEventListener("click", function(e){

        sendButton.classList.add("sending");


        gsap.to(sendButton, {

            scale:0.95,

            duration:0.15,

            yoyo:true,

            repeat:1

        });



        setTimeout(()=>{


            sendButton.classList.remove("sending");

            sendButton.classList.add("success");


            gsap.fromTo(
                sendButton,
                {
                    scale:0.8
                },
                {
                    scale:1,
                    duration:.5,
                    ease:"back.out"
                }
            );


        },800);



    });

}

document.addEventListener("DOMContentLoaded", () => {


    const form = document.querySelector(".contact-right form");
    const sendButton = document.querySelector(".send-button");


    if(form && sendButton){


        form.addEventListener("submit", async function(e){


            e.preventDefault(); // stops Formspree redirect


            sendButton.classList.add("sending");


            const formData = new FormData(form);



            try {


                const response = await fetch(
                    form.action,
                    {
                        method:"POST",
                        body:formData,
                        headers:{
                            "Accept":"application/json"
                        }
                    }
                );



                if(response.ok){


                    sendButton.classList.remove("sending");

                    sendButton.classList.add("success");



                    gsap.fromTo(
                        sendButton,
                        {
                            scale:0.8
                        },
                        {
                            scale:1,
                            duration:0.5,
                            ease:"back.out"
                        }
                    );


                    form.reset();



                    setTimeout(()=>{

                        sendButton.classList.remove("success");

                    },3000);



                }

                else {

                    alert("Something went wrong. Please try again.");

                }



            } catch(error){


                alert("Unable to send message.");

            }



        });


    }


});


/* =========================
   PROJECT DETAILS MODAL
========================= */

document.addEventListener("DOMContentLoaded", () => {


    const projects = document.querySelectorAll(".project-item");

    const detailsButton = document.getElementById("project-details-btn");

    const modal = document.getElementById("project-modal");

    const closeButton = document.getElementById("modal-close");


    const modalImage = document.getElementById("modal-image");

    const modalTitle = document.getElementById("modal-title");

    const modalDescription = document.getElementById("modal-description");

    const modalLink = document.getElementById("modal-link");



    if(
        !projects.length ||
        !detailsButton ||
        !modal
    ){

        console.log("Project modal missing elements");
        return;

    }



    let activeProject = document.querySelector(".project-item.active");



    /*
        CHANGE ACTIVE PROJECT
    */

    projects.forEach(project => {


        project.addEventListener("click", ()=>{


            projects.forEach(item => {

                item.classList.remove("active");

            });


            project.classList.add("active");


            activeProject = project;



            // Update preview image

            document.getElementById("project-preview").src =
            project.dataset.image;



            document.getElementById("project-title").textContent =
            project.dataset.title;



            document.getElementById("project-description").textContent =
            project.dataset.description;



        });


    });





    /*
        OPEN MODAL
    */

    detailsButton.addEventListener("click", ()=>{


        if(!activeProject) return;



        modalImage.src =
        activeProject.dataset.image;



        modalTitle.textContent =
        activeProject.dataset.title;



        modalDescription.textContent =
        activeProject.dataset.description;



        modalLink.href =
        activeProject.dataset.link;



        modal.classList.add("active");


        document.body.style.overflow="hidden";


    });






    /*
        CLOSE MODAL
    */

    function closeModal(){

        modal.classList.remove("active");

        document.body.style.overflow="";

    }



    closeButton.addEventListener(
        "click",
        closeModal
    );



    modal.addEventListener(
        "click",
        (e)=>{

            if(e.target === modal){

                closeModal();

            }

        }
    );



    document.addEventListener(
        "keydown",
        (e)=>{

            if(e.key === "Escape"){

                closeModal();

            }

        }
    );


});