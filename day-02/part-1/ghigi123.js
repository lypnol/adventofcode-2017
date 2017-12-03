const _ = require('lodash');

function run(s) {
    return _.sum(
        _.map(s.split('\n'), line => {
            const t = _.map(_.split(line, '\t'), a => parseInt(a));
            return _.max(t) - _.min(t);
        })
    );
}