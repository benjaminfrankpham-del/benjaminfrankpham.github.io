function initBackground(){

    const canvas = document.getElementById("network-bg");
    const ctx = canvas.getContext("2d");


    let width;
    let height;


    const mouse = {

        x: -1000,
        y: -1000,
        radius: 180

    };


    const spacing = 90;

    let nodes = [];



    function resize(){

        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;


        nodes = [];


        const cols = Math.ceil(width / spacing) + 1;
        const rows = Math.ceil(height / spacing) + 1;


        for(let x = 0; x < cols; x++){

            for(let y = 0; y < rows; y++){

                nodes.push({

                    originalX: x * spacing,
                    originalY: y * spacing,

                    x: x * spacing,
                    y: y * spacing,

                    glow: 0

                });

            }

        }

    }


    window.addEventListener("resize", resize);


    window.addEventListener("mousemove",(event)=>{

        mouse.x = event.clientX;
        mouse.y = event.clientY;

    });



    function animate(){


        ctx.clearRect(
            0,
            0,
            width,
            height
        );


        // Move nodes toward cursor

        nodes.forEach(node=>{


            const dx = mouse.x - node.originalX;
            const dy = mouse.y - node.originalY;


            const distance = Math.sqrt(
                dx * dx +
                dy * dy
            );


            if(distance < mouse.radius){


                const force =
                    (1 - distance / mouse.radius) * 18;


                node.x =
                    node.originalX -
                    (dx / distance) * force;


                node.y =
                    node.originalY -
                    (dy / distance) * force;



                node.glow =
                    1 - distance / mouse.radius;


            }
            else{


                node.x +=
                    (node.originalX - node.x) * .08;


                node.y +=
                    (node.originalY - node.y) * .08;



                node.glow *= .9;


            }


        });



        // Draw connections

        ctx.lineWidth = 1;


        for(let i = 0; i < nodes.length; i++){


            const node = nodes[i];



            for(let j = i + 1; j < nodes.length; j++){


                const other = nodes[j];


                const distance = Math.hypot(
                    node.x - other.x,
                    node.y - other.y
                );



                if(distance < spacing * 1.5){


                    const glow =
                        Math.max(
                            node.glow,
                            other.glow
                        );


                    ctx.strokeStyle =
                    `rgba(77,163,255,${
                        .04 + glow * .35
                    })`;



                    ctx.beginPath();

                    ctx.moveTo(
                        node.x,
                        node.y
                    );


                    ctx.lineTo(
                        other.x,
                        other.y
                    );


                    ctx.stroke();


                }


            }


        }




        // Draw nodes

        nodes.forEach(node=>{


            const size =
                2 + node.glow * 3;



            ctx.beginPath();


            ctx.arc(
                node.x,
                node.y,
                size,
                0,
                Math.PI * 2
            );


            ctx.fillStyle =
            `rgba(77,163,255,${
                .15 + node.glow
            })`;



            ctx.fill();


        });



        requestAnimationFrame(animate);


    }



    resize();

    animate();


}

gsap.registerPlugin(
    ScrollTrigger,
    MorphSVGPlugin
);



const down = 
'M0-0.3C0-0.3,464,156,1139,156S2278-0.3,2278-0.3V683H0V-0.3z';



const center =
'M0-0.3C0-0.3,464,0,1139,0s1139-0.3,1139-0.3V683H0V-0.3z';



ScrollTrigger.create({

    trigger:".footer",

    start:"top bottom",

    toggleActions:"play pause resume reverse",


    onEnter:self=>{


        const velocity = self.getVelocity();

        const variation = velocity / 10000;



        gsap.fromTo(

            "#bouncy-path",

            {
                morphSVG:down
            },

            {

                duration:2,

                morphSVG:center,

                ease:
                `elastic.out(${1 + variation}, ${1 - variation})`,

                overwrite:true

            }

        );

    }

});