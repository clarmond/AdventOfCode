let x = 37;
let y = 43;
let maxX = 129;
let maxY = 129;
let direction = "up";

function moveGuard() {
    if (direction == "up") {
        y--;
    } else if (direction == "down") {
        y++; 
    } else if (direction == "right") {
        x++;
    } else if (direction == "left") {
        x--;
    }
    const spot = $(`#r${y}c${x}`);
    const text = spot.text();
    if (text == "#") {
        if (direction == "up") {
            direction = "right";
            y++;
        } else if (direction == "down") {
            direction = "left";
            y--;
        } else if (direction == "right") {
            direction = "down";
            x--;
        } else if (direction == "left") {
            direction = "up";
            x++;
        }
    } else {
        spot.text('X').addClass('x');
    }
    if ($(`#r${y}c${x}`).text() == "#") {
        moveGuard();
        return;
    }
    if (x < 0 || x > maxX) {
        return true
    }
    if (y < 0 || y > maxY) {
        return true
    }
    return false;
}

let intervalID;
$(function() {
    intervalID = window.setInterval(function() {
        const result = moveGuard();
        if (result) {
            clearInterval(intervalID);
            console.log($('.x').length)
        }
    }, 0);
})