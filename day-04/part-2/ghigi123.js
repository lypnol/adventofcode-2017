const _ = require('lodash');

run = s =>
    _.size(_.filter(
        _.split(s, '\n'),
        line => {
            const words = _.map(
                _.split(line, ' '),
                word => _.join(_.sortBy(word), '')
            );
            return _.size(_.uniq(words)) === _.size(words);
        }
    ));