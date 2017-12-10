const _ = require('lodash');

copyTo = (table, subtable, index) => {
    const copy = _.clone(table);
    _.forEach(subtable, (e, i) => copy[(index + i) % table.length] = e);
    return copy;
};

copyFrom = (table, index, length) => _.map(_.range(length), i => table[(index + i) % table.length]);

run = s => {
    const lengths = _.map(_.split(s, ','), i => parseInt(i));
    const hashedList = _.reduce(
        lengths,
        (acc, length) => ({
            index: (acc.index + length + acc.skip) % acc.list.length,
            skip: acc.skip + 1,
            list: copyTo(acc.list, _.reverse(copyFrom(acc.list, acc.index, length)), acc.index)
        }), {
            index: 0,
            skip: 0,
            list: _.range(256)
        });
    return hashedList.list[0] * hashedList.list[1];
};
