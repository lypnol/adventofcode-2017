const _ = require('lodash');

disCos = angle => [1, 0, -1, 0][angle % 4];
disSin = angle => [0, 1, 0, -1][angle % 4];

neighbors = (x, y) => {
    const res = [];
    _.forEach(_.range(-1, 2), i =>
        _.forEach(_.range(-1, 2), j => {
                if (i !== 0 || j !== 0) {
                    res.push((x + i) + '_' + (y + j))
                }
            }
        )
    );
    return res;
};

function run(s) {
    const input = parseInt(s);
    let coords = {x: 0, y: 0};
    let values = {'0_0': 1};
    let angle = 0;
    let last = 1;

    while (last < input) {
        coords = {x: coords.x + disCos(angle), y: coords.y + disSin(angle)};

        if (coords.x === coords.y || (coords.x < 0 && coords.x === -coords.y) || coords.x > 0 && coords.x === -coords.y + 1) {
            angle += 1;
        }

        const neighborIndices = neighbors(coords.x, coords.y);
        last = _.sum(_.map(neighborIndices, iStr =>
            values[iStr] ? values[iStr] : 0
        ));
        values[coords.x + '_' + coords.y] = last;
    }
    return last;
}