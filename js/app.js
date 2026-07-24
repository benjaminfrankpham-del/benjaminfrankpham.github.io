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


    const detailsButton = document.getElementById("project-details-btn");

    const modal = document.getElementById("project-modal");

    const closeButton = document.getElementById("modal-close");


    const modalImage = document.getElementById("modal-image");

    const modalTitle = document.getElementById("modal-title");

    const modalDescription = document.getElementById("modal-description");

    const modalLink = document.getElementById("modal-link");


    const projects = document.querySelectorAll(".project-item");



    if(
        !detailsButton ||
        !modal ||
        !closeButton
    ){

        console.log("Project modal elements missing");

        return;

    }




    let activeProject = projects[0];



    /*
       Detect active project
       when scrolling changes project
    */

    projects.forEach(project=>{


        project.addEventListener("click",()=>{

            activeProject = project;

        });


    });



    /*
       OPEN MODAL
    */

    detailsButton.addEventListener("click",()=>{


        if(!activeProject) return;



        const image =
        activeProject.dataset.image;


        const title =
        activeProject.dataset.title;


        const description =
        activeProject.dataset.description;


        const link =
        activeProject.dataset.link;




        modalImage.src = image;

        modalTitle.textContent = title;

        modalDescription.textContent = description;

        modalLink.href = link;



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




    /*
       CLICK OUTSIDE TO CLOSE
    */

    modal.addEventListener(
        "click",
        (e)=>{


            if(e.target === modal){

                closeModal();

            }


        }
    );





    /*
       ESC KEY CLOSE
    */

    document.addEventListener(
        "keydown",
        (e)=>{


            if(e.key==="Escape"){

                closeModal();

            }


        }
    );


});