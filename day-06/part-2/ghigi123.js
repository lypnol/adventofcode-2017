const _ = require('lodash');

exp = (table, set) => {
    while (!(_.join(table, '_') in set)) {
        set[_.join(table, '_')] = 1;
        const maxIdx = _.maxBy(_.range(_.size(table)), idx => table[idx]);
        const val = table[maxIdx];
        table[maxIdx] = 0;
        for (let i = (maxIdx + 1) % table.length, j = 0; j < val; j++, i = (i + 1) % table.length) {
            table[i] += 1;
        }
    }
    return _.size(set);
};

run = s => {
    const table = _.map(_.split(s, '\t'), n => parseInt(n));
    exp(table, {});
    return exp(table, {});
};