const _ = require('lodash');

run = s => {
    const instructions = _.map(s.split('\n'), i => parseInt(i));
    let pos = 0;
    let iter = 0;
    while (pos >= 0 && pos < instructions.length) {
        const nextPos = pos + instructions[pos];
        if(instructions[pos] >= 3) {
            instructions[pos]--;
        } else {
            instructions[pos]++;
        }
        pos = nextPos;
        iter++;
    }

    return iter;
};