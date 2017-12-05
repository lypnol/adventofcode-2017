const _ = require('lodash');

function run(s) {
    return _.sum(
        _.map(s,
            (e, i) =>
                parseInt(e) === parseInt(s[i === s.length - 1 ? 0 : i + 1])
                    ? parseInt(e)
                    : 0)
    );
};