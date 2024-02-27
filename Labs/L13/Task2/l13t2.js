const arr = ["Test Test", "This is a test", "This Is A Test", "Catherine Elaine", "Catherine Elaine Guil", "", "Does this pass?", "Question Node.js"];

function filter(msg, funcs) {
    correctList = [];
    for (let i = 0; i < msg.length; i++) {
        let isCorrect = true;
        for (let j = 0; j < funcs.length; j++) {
            if (!funcs[j](msg[i])) {
                isCorrect = false;
                break;
            }
        }
        if (isCorrect)
            correctList.push(msg[i]);
    }
    return correctList;
}

const capitals = (msg) => {
    if (msg.length == 0)
        return false;
    tokens = msg.split(" ");
    for (let i = 0; i < tokens.length; i++) {
        if (tokens[i][0].toUpperCase() != tokens[i][0])
            return false;
    }
    return true;
};

const oneSpace = (msg) => msg.split(" ").length == 2;

const sameChar = (msg) => {
    tokens = msg.split(" ");
    return (tokens.length >= 2) ? (tokens[0][tokens[0].length - 1].toLowerCase() == tokens[1][0].toLowerCase()) : false;
};

const filtArr = filter(arr, [capitals, oneSpace, sameChar]);

console.log(filtArr);