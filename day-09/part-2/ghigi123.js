const _ = require('lodash');

const handleExclamation = input => _.replace(input, /!./g, '');
const stringToGarbages = input => input.match(/<.*?>/g);
run = s => {
    return _.sum(_.map(stringToGarbages(handleExclamation(s)), i => i.length - 2));
};
