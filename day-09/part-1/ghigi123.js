const _ = require('lodash');

const handleExclamation = input => _.replace(input, /!./g, '');
const handleGarbage = input => _.replace(input, /<.*?>/g, '');
const countGroups = input => _.reduce(
    input,
    (acc, letter) => ({
        sum: letter === '{' ? acc.sum + acc.depth : acc.sum,
        depth: acc.depth + (letter === '{') - (letter === '}')
    }),
    {
        depth: 1,
        sum: 0
    })
    .sum;

run = s => {
    return countGroups(handleGarbage(handleExclamation(s)));
};
