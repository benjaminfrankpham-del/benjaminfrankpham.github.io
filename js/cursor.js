function initCursor(){

    const glow =
    document.querySelector(".cursor-glow");


    let mouseX = 0;
    let mouseY = 0;

    let glowX = 0;
    let glowY = 0;



    window.addEventListener(
        "mousemove",
        (e)=>{

            mouseX = e.clientX;
            mouseY = e.clientY;

            glow.style.opacity = 1;

        }
    );



    function animate(){


        // smooth floating movement

        glowX += 
        (mouseX - glowX) * 0.08;


        glowY +=
        (mouseY - glowY) * 0.08;



        glow.style.left =
        glowX + "px";


        glow.style.top =
        glowY + "px";



        requestAnimationFrame(animate);

    }



    animate();



    window.addEventListener(
        "mouseleave",
        ()=>{

            glow.style.opacity = 0;

        }
    );


}