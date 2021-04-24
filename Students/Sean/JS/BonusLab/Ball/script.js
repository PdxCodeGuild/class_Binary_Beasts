let width = document.getElementById("square").width;
let height = document.getElementById("square").height;
let ctx = document.getElementById("square").getContext("2d");
let grav = .1


let ball = {
    radius: 30,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*5,
    vy: (2*Math.random()-1)*5
};

let ball2 = {
    radius: 30,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*5,
    vy: (2*Math.random()-1)*5
};



function main_loop() {
    // update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;

    ball2.px += ball2.vx;
    ball2.py += ball2.vy;

    // check if it hit a boundary, reset it within bounds, and change the velocity
    if(ball.px<=0){ball.px=2;ball.vx*=-.99;}
    if(ball.py<=0){ball.py=2;ball.vy*=-.99;}
    if(ball.px>=width){ball.px=width-1;ball.vx*=-.99;}
    if(ball.py>=height){ball.py=height-1;ball.vy*=-.99;}

    if(ball2.px<=0){ball2.px=2;ball2.vx*=-.99;}
    if(ball2.py<=0){ball2.py=2;ball2.vy*=-.99;}
    if(ball2.px>=width){ball2.px=width-1;ball2.vx*=-.99;}
    if(ball2.py>=height){ball2.py=height-1;ball2.vy*=-.99;}

    // collision check
    if(ball.px+ball.radius+ball2.radius>ball2.px
        &&ball.px<ball2.px+ball.radius+ball2.radius
        &&ball.py+ball.radius+ball2.radius>ball2.py
        &&ball.py<ball2.py+ball.radius+ball2.radius){
            distance=Math.sqrt(
                ((ball.px-ball2.px)*(ball.px-ball2.px))+
                ((ball.py-ball2.py)*(ball.py-ball2.py)));
            if(distance<ball.radius+ball2.radius){
                collisionPointX=((ball.px*ball2.radius)+(ball2.px*ball.radius))/(ball.radius+ball2.radius);
                collisionPointY=((ball.py*ball2.radius)+(ball2.py*ball.radius))/(ball.radius+ball2.radius);

                newVelX1=(ball.vx*(ball.radius-ball2.radius)+(2*ball2.radius*ball2.vx))/(ball.radius+ball2.radius);
                newVelY1=(ball.vy*(ball.radius-ball2.radius)+(2*ball2.radius*ball2.vy))/(ball.radius+ball2.radius);
                newVelX2=(ball2.vx*(ball2.radius-ball.radius)+(2*ball.radius*ball.vx))/(ball.radius+ball2.radius);
                newVelY2=(ball2.vy*(ball2.radius-ball.radius)+(2*ball.radius*ball.vy))/(ball.radius+ball2.radius);
                //console.log(newVelX1 + newVelX2 + newVelY1 + newVelY2)
            
                ball.px = ball.px + newVelX1;
                ball.py = ball.py + newVelY1;
            
                ball2.px = ball2.px + newVelX2;
                ball2.py = ball2.py + newVelY2;
            }
    }

    // draw the ball
    ctx.clearRect(0,0,width,height);
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.arc(ball2.px, ball2.py, ball2.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle='black';
    ctx.fill();
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);