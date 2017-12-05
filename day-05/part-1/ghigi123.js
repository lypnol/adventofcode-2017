const _ = require('lodash');

function rec(instructions, pos) {
    if(pos >= _.size(instructions) || pos < 0)
        return 0;
    instructions[pos]++;
    return 1 + rec(instructions, pos + instructions[pos] - 1);
}

run = s => {
    const instructions = _.map(s.split('\n'), i => parseInt(i));
    let pos = 0;
    let iter = 0;
    while (pos >= 0 && pos < instructions.length) {
        const nextPos = pos + instructions[pos];
        instructions[pos]++;
        pos = nextPos;
        iter++;
    }

    return iter;
};