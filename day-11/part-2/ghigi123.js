const _ = require('lodash');

const distance = ({s_n: s_n, nw_se: nw_se, ne_sw: ne_sw}) =>
    (Math.abs(nw_se - ne_sw) + Math.abs(ne_sw + s_n) + Math.abs(-s_n - nw_se)) / 2;

const next_step = ({s_n: s_n, nw_se: nw_se, ne_sw: ne_sw}, step) => ({
    s_n: s_n + (step === 'n') - (step === 's'),
    nw_se: nw_se + (step === 'nw') - (step === 'se'),
    ne_sw: ne_sw + (step === 'ne') - (step === 'sw'),
});

const run = s => {
    const steps = _.split(s, ',');
    return _.reduce(
        steps,
        ({max: max, pos: pos}, step) => ({
            max: Math.max(max, distance(next_step(pos, step))),
            pos: next_step(pos, step)
        }),
        {
            max: 0,
            pos: {s_n: 0, nw_se: 0, ne_sw: 0}
        }
    ).max;
};
