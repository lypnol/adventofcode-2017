const _ = require('lodash');

function run(s) {
    return _.sum(
        _.map(s,
            (e, i) =>
                parseInt(e) === parseInt(s[(i + (s.length / 2)) % s.length])
                    ? parseInt(e)
                    : 0)
    );
}