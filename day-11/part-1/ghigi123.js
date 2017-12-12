const _ = require('lodash');

const run = s => {
    const counts = _.countBy(_.split(s, ','));
    const dirs = {
        s_n: counts['n'] - counts['s'],
        nw_se: counts['nw'] - counts['se'],
        ne_sw: counts['ne'] - counts['sw']
    };
    return (Math.abs(dirs.nw_se - dirs.ne_sw)
        + Math.abs(dirs.ne_sw + dirs.s_n)
        + Math.abs(-dirs.s_n - dirs.nw_se)) / 2;
};
