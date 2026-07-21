function initAnimations() {

    gsap.from(".logo", {
        y: -50,
        opacity: 0,
        duration: 1
    });

    gsap.from(".menu-btn", {
        y: -50,
        opacity: 0,
        duration: 1,
        delay: .2
    });

    gsap.from(".hero-tag", {
        x: -100,
        opacity: 0,
        duration: 1,
        delay: .5
    });

    gsap.from(".hero h1", {
        y: 100,
        opacity: 0,
        duration: 1.2,
        delay: .7
    });

    gsap.from(".hero h2", {
        y: 60,
        opacity: 0,
        duration: 1,
        delay: 1
    });

    gsap.from(".hero-description", {
        y: 40,
        opacity: 0,
        duration: 1,
        delay: 1.2
    });

    gsap.from(".hero-buttons", {
        y: 40,
        opacity: 0,
        duration: 1,
        delay: 1.4
    });

}