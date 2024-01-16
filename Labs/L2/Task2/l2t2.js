function is_factorial(x) {
    if (x < 0) {
        return -1;
    } else if (x == 0) {
        return 0;
    }

    let doneFact = false;
    let divisor = 1;

    while (!doneFact) {
        if (x % divisor == 0 && x / divisor != 1) {
            x /= divisor;
            divisor++;
        } else if (x % divisor == 0 && x / divisor == 1) {
            doneFact = true;
            return divisor;
        } else {
            doneFact = true;
            return 0;
        }
    }
}

const prompt = require('prompt-sync')();

let stopLoop = false;
console.log("Select a command:\n\tn: Check a value.\n\tq: Quit")
let cmd = prompt("");
while (!stopLoop) {
    switch (cmd) {
        case 'n':
            let num = prompt('');
            let result = is_factorial(num);
            if (result == 0) {
                console.log("%d is not the factorial of another number.", num);
            } else if (result == -1) {
                console.log("%d is a negative number.", num);
            } else {
                console.log("%d is the factorial result of: %d", num, result);
            }
            break;
        case 'q':
            stopLoop = true;
            exit(0);
        default:
            console.log("Unknown command.");
    }
    cmd = prompt("New command: ")
}