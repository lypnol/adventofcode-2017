const _ = require('lodash');

run = s => {
    const lines = _.split(s, '\n');
    const nodes = _.keyBy(_.map(lines, line => {
        const res = /^(\w+)\s*\((\d+)\)(?:\s*->\s+((?:,?\s*\w+)*))?$/gm.exec(line);
        return {
            id: res[1],
            weight: parseInt(res[2]),
            children: res[3] ? _.split(res[3], ', ') : []
        };
    }), 'id');
    _.forEach(nodes, node =>
        _.forEach(node.children, child =>
            nodes[child].parent = node.id
        )
    );
    const findRoot = node => !node.parent ? node.id : findRoot(nodes[node.parent]);
    return findRoot(nodes[_.keys(nodes)[0]]);
};