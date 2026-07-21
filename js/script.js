// ----------------------
// GSAP HERO ANIMATION
// ----------------------

gsap.from(".logo", {
  y: -50,
  opacity: 0,
  duration: 1
});

gsap.from(".menu-btn", {
  y: -50,
  opacity: 0,
  duration: 1,
  delay: 0.2
});

gsap.from(".hero-tag", {
  x: -100,
  opacity: 0,
  duration: 1,
  delay: 0.5
});

gsap.from(".hero h1", {
  y: 100,
  opacity: 0,
  duration: 1.2,
  delay: 0.7
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

// ----------------------
// NETWORK BACKGROUND
// ----------------------

const canvas = document.getElementById("network-bg");
const ctx = canvas.getContext("2d");

const spacing = 80;
const influence = 180;

let cols;
let rows;
let nodes = [];

const mouse = {
  x: -1000,
  y: -1000
};

window.addEventListener("mousemove", (e) => {
  mouse.x = e.clientX;
  mouse.y = e.clientY;
});

window.addEventListener("resize", createGrid);

function createGrid() {

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  cols = Math.ceil(canvas.width / spacing) + 1;
  rows = Math.ceil(canvas.height / spacing) + 1;

  nodes = [];

  for (let x = 0; x < cols; x++) {

    for (let y = 0; y < rows; y++) {

      nodes.push({

        ox: x * spacing,
        oy: y * spacing,

        x: x * spacing,
        y: y * spacing

      });

    }

  }

}

createGrid();

function animate() {

  ctx.clearRect(0,0,canvas.width,canvas.height);

  // Move nodes

  nodes.forEach(node=>{

    const dx = mouse.x-node.ox;
    const dy = mouse.y-node.oy;

    const distance = Math.sqrt(dx*dx+dy*dy);

    if(distance<influence){

      const force=(1-distance/influence)*12;

      const angle=Math.atan2(dy,dx);

      node.x=node.ox-Math.cos(angle)*force;
      node.y=node.oy-Math.sin(angle)*force;

    }else{

      node.x += (node.ox-node.x)*0.08;
      node.y += (node.oy-node.y)*0.08;

    }

  });

  // Draw connections

  ctx.lineWidth=1;

  for(let x=0;x<cols;x++){

    for(let y=0;y<rows;y++){

      const index=x*rows+y;

      const node=nodes[index];

      if(x<cols-1){

        const right=nodes[(x+1)*rows+y];

        const mx=(node.x+right.x)/2;
        const my=(node.y+right.y)/2;

        const d=Math.hypot(mouse.x-mx,mouse.y-my);

        const glow=Math.max(0,1-d/influence);

        ctx.strokeStyle=`rgba(77,163,255,${0.05+glow*0.35})`;

        ctx.beginPath();

        ctx.moveTo(node.x,node.y);

        ctx.lineTo(right.x,right.y);

        ctx.stroke();

      }

      if(y<rows-1){

        const bottom=nodes[x*rows+y+1];

        const mx=(node.x+bottom.x)/2;
        const my=(node.y+bottom.y)/2;

        const d=Math.hypot(mouse.x-mx,mouse.y-my);

        const glow=Math.max(0,1-d/influence);

        ctx.strokeStyle=`rgba(77,163,255,${0.05+glow*0.35})`;

        ctx.beginPath();

        ctx.moveTo(node.x,node.y);

        ctx.lineTo(bottom.x,bottom.y);

        ctx.stroke();

      }

    }

  }

  // Draw nodes

  nodes.forEach(node=>{

    const d=Math.hypot(mouse.x-node.x,mouse.y-node.y);

    const glow=Math.max(0,1-d/influence);

    const size=2+glow*3;

    ctx.beginPath();

    ctx.arc(node.x,node.y,size,0,Math.PI*2);

    ctx.fillStyle=`rgba(77,163,255,${0.2+glow*0.8})`;

    ctx.fill();

  });

  requestAnimationFrame(animate);

}

animate();