const _ = require('lodash');

const distance = vec =>
    (Math.abs(vec.nw_se - vec.ne_sw)
        + Math.abs(vec.ne_sw + vec.s_n)
        + Math.abs(-vec.s_n - vec.nw_se)) / 2;

const next_step = (vec, step) => ({
    s_n: vec.s_n + (step === 'n') - (step === 's'),
    nw_se: vec.nw_se + (step === 'nw') - (step === 'se'),
    ne_sw: vec.ne_sw + (step === 'ne') - (step === 'sw'),
});

const run = s => {
    const steps = _.split(s, ',');
    return _.reduce(
        steps,
        (acc, step) => ({
            max: Math.max(acc.max, distance(next_step(acc.pos, step))),
            pos: next_step(acc.pos, step)
        }),
        {
            max: 0,
            pos: {s_n: 0, nw_se: 0, ne_sw: 0}
        }
    ).max;
};
