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