const fs = require("fs");

function writeStrings(strArr, fileOut) {
    let retval = 0;
    let strOut = "";
    for (i = 0; i < strArr.length; i++) {
        retval += strArr[i].length;
        strOut += strArr[i] + "\n";
    }
    fs.writeFileSync(fileOut, strOut);
    return retval;
}

console.log(writeStrings(["Hello", "world", "test"], "Output.txt"));