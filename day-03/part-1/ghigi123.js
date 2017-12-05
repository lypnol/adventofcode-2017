const _ = require('lodash');

function run(s) {
    const input = parseInt(s);
    const circleIdHelper = Math.ceil(Math.sqrt(input));
    const circleId = circleIdHelper % 2 === 0 ? circleIdHelper + 1 : circleIdHelper;
    const mod = input % (circleId - 1) - 1;
    const twist = Math.abs(mod - (circleId - 1 ) / 2);
    return twist + (circleId - 1) / 2;
}

