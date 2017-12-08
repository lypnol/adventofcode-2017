const _ = require('lodash');

comp = (op, v1, v2) => {
    switch (op) {
        case '==':
            return v1 === v2;
        case '<=':
            return v1 <= v2;
        case '>=':
            return v1 >= v2;
        case '!=':
            return v1 !== v2;
        case '>':
            return v1 > v2;
        case '<':
            return v1 < v2;
    }
};

run = s => {
    const lines = _.split(s, '\n');
    const instructions = _.map(lines, line => {
        const res = /(\w+)\s(\w+)\s(-?\d+)\sif\s(\w+)\s([=<>!]+)\s(-?\d+)/g.exec(line);
        return {
            slot: res[1],
            op: res[2],
            val: parseInt(res[3]),
            compSlot: res[4],
            compOp: res[5],
            compVal: parseInt(res[6])
        };
    });
    const regs = {};
    let max = parseFloat('-inf');
    _.forEach(instructions, instruction => regs[instruction.slot] = 0);
    _.forEach(instructions, instruction => {
        if(comp(instruction.compOp, regs[instruction.compSlot], instruction.compVal)) {
            instruction.op === 'inc' && (regs[instruction.slot] += instruction.val);
            instruction.op === 'dec' && (regs[instruction.slot] -= instruction.val);
        }
        max = _.max([max, _.max(_.values(regs))]);
    });

    return max;
};
