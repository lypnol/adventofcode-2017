const _ = require('lodash');

function run(s) {
    return _.sum(
        _.map(s.split('\n'), line => {
            const t = _.map(_.split(line, '\t'), a => parseInt(a));
            return _.reduce(
                t,
                (acc, i) =>
                    acc === 0
                        ? _.reduce(
                        t,
                        (acc2, j) =>
                            (acc2 === 0 && i !== j && i % j === 0)
                                ? i / j
                                : acc2
                        , 0)
                        : acc
                , 0);
        })
    );
}