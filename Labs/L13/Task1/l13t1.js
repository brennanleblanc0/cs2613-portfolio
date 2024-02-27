const t1 = "This is a test";
const t2 = "This Is A Test";
const t3 = "This is";
const t4 = "Margaret Ryan";
const t5 = "Catherine Elaine Guil";

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

console.log('capitals("This is a test"):', capitals(t1));
console.log('capitals("This Is A Test"):', capitals(t2));
console.log('oneSapce("This Is A Test"):', oneSpace(t1));
console.log('oneSpace("This is"):', oneSpace(t3));
console.log('sameChar("Margaret Ryan"):', sameChar(t4));
console.log('sameChar("Catherine Elaine Guil"):', sameChar(t5));