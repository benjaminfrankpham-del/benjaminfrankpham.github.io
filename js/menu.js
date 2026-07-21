const menuButton = document.querySelector("#menuToggle");
const menuOverlay = document.querySelector(".menu-overlay");

let menuOpen = false;


// =============================
// OPEN ANIMATION
// =============================

const openTL = gsap.timeline({
    paused:true
});


openTL

.set(menuOverlay,{
    visibility:"visible",
    pointerEvents:"auto"
})


.to(".panel-top",{

    x:0,

    duration:.6,

    ease:"back.out(1.5)"

})


.to(".panel-middle",{

    x:0,

    duration:.5,

    ease:"power3.out"

},"-=.35")


.to(".panel-bottom",{

    y:0,

    duration:.5,

    ease:"power3.out"

},"-=.3");





// =============================
// CLOSE ANIMATION
// =============================

const closeTL = gsap.timeline({

    paused:true,

    onComplete:()=>{

        gsap.set(menuOverlay,{

            visibility:"hidden",

            pointerEvents:"none"

        });

    }

});


closeTL


// bottom falls first

.to(".panel-bottom",{

    y:"120vh",

    rotation:15,

    duration:.6,

    ease:"power3.in"

})


// middle falls

.to(".panel-middle",{

    y:"120vh",

    rotation:-10,

    duration:.7,

    ease:"power3.in"

},"-=.35")


// top falls last

.to(".panel-top",{

    y:"120vh",

    rotation:20,

    duration:.9,

    ease:"power3.in"

},"-=.45");






// =============================
// BUTTON CONTROL
// =============================

menuButton.addEventListener("click",()=>{


    menuOpen = !menuOpen;



    if(menuOpen){


        closeTL.pause(0);

        openTL.restart();



        // hamburger -> X

        gsap.to(".bar-top",{

            rotation:45,

            y:8,

            duration:.3

        });


        gsap.to(".bar-middle",{

            opacity:0,

            duration:.3

        });


        gsap.to(".bar-bottom",{

            rotation:-45,

            y:-8,

            duration:.3

        });



    } 
    
    else {


        openTL.pause();

        closeTL.restart();



        // X -> hamburger

        gsap.to(".bar-top",{

            rotation:0,

            y:0,

            duration:.3

        });


        gsap.to(".bar-middle",{

            opacity:1,

            duration:.3

        });


        gsap.to(".bar-bottom",{

            rotation:0,

            y:0,

            duration:.3

        });


    }


});