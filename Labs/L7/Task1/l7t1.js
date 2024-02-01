const fs = require("node:fs");

let calcs = {
    name: new Array(3),
    diff: [0.0,0.0,0.0]
};
// TODO: Use try-catch loop
for (fi = 1; fi <= 4; fi++) {
    const fileData = fs.readFileSync("calculations".concat(fi, ".json"));
    const data = JSON.parse(fileData);
    let trueVal = parseFloat(data.data.calculations[0].calc);
    for (i = 1; i < 4; i++) {
        let iVal = parseFloat(data.data.calculations[i].calc);
        if (fi == 1)
            calcs.name[i-1] = data.data.calculations[i].performer;
        calcs.diff[i-1] += (trueVal - iVal >= 0) ? trueVal - iVal : iVal - trueVal;
    }
}
for (i = 0; i < 3; i++) {
    for (j = 0; j < 2; j++) {
        if (calcs.diff[j] > calcs.diff[j+1]) {
            let temp1 = calcs.diff[j], temp2 = calcs.name[j];
            calcs.diff[j] = calcs.diff[j+1];
            calcs.name[j] = calcs.name[j+1];
            calcs.diff[j+1] = temp1;
            calcs.name[j+1] = temp2;
        }
    }
}
for (i = 0; i < 3; i++) {
    console.log("%d.\t%s\t(%d)", i+1, calcs.name[i], calcs.diff[i]);
}
