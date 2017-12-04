const _ = require('lodash');

run = s =>
    _.size(_.filter(
        _.split(s, '\n'),
        line =>
            _.size(_.uniq(_.split(line, ' '))) === _.size(_.split(line, ' '))
    ));