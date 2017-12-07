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
    const findRoot = node => node.parent ? findRoot(nodes[node.parent]) : node.id;
    const exploreSum = node => node.sum = node.weight + _.sum(_.map(node.children, child => exploreSum(nodes[child])));
    const exploreDepth = (node, i) => { node.depth = i; _.forEach(node.children, child => exploreDepth(nodes[child], i + 1))};
    const root = nodes[findRoot(nodes[_.keys(nodes)[0]])];
    exploreSum(root);
    exploreDepth(root, 0);
    const errorNode = _.maxBy(_.values(nodes), node => node.depth * (_.size(_.uniq(_.map(node.children, child => nodes[child].sum))) > 1));
    const childrenSumCount = _.countBy(_.map(errorNode.children, child => nodes[child].sum));
    const errorChildIdx = _.minBy(_.range(errorNode.children.length), idx => childrenSumCount[nodes[errorNode.children[idx]].sum]);
    return nodes[errorNode.children[errorChildIdx]].weight
        - nodes[errorNode.children[errorChildIdx]].sum
        + nodes[errorNode.children[(errorChildIdx + 1) % errorNode.children.length]].sum;
};
