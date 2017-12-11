const _ = require('lodash');

copyTo = (table, subtable, index) => {
    const copy = _.clone(table);
    _.forEach(subtable, (e, i) => copy[(index + i) % table.length] = e);
    return copy;
};

copyFrom = (table, index, length) => _.map(_.range(length), i => table[(index + i) % table.length]);

round = (lengths, prevAcc) => _.reduce(
    lengths,
    (acc, length) => ({
        index: (acc.index + length + acc.skip) % acc.list.length,
        skip: acc.skip + 1,
        list: copyTo(acc.list, _.reverse(copyFrom(acc.list, acc.index, length)), acc.index)
    }),
    prevAcc);

run = s => {
    const lengths = _.concat(_.map(s, c => c.charCodeAt(0)), [17, 31, 73, 47, 23]);
    const sparseHash = _.reduce(
        _.range(64),
        acc => round(lengths, acc),
        {
            index: 0,
            skip: 0,
            list: _.range(256)
        }
    ).list;
    const xoredHash = _.map(
        _.chunk(sparseHash, 16),
        chunk => _.reduce(chunk, (a, i) => a ^ i, 0)
    );
    return _.join(
        _.map(xoredHash, n => ('0' + n.toString(16)).slice(-2))
        , ''
    );
};
