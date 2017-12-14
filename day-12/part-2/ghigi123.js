const _ = require('lodash');

class UF {
    constructor(n) {
        this.sets = {};
        this.map = {};
        _.forEach(_.range(n), i => {
            this.sets[i] = {};
            this.sets[i][i] = 1;
            this.map[i] = i;
        });
    }

    union(i, j) {
        const iSet = this.find(i), jSet = this.find(j);
        if(iSet !== jSet) {
            _.assign(this.sets[iSet], this.sets[jSet]);
            _.forEach(this.sets[jSet], (i, k) => this.map[k] = iSet);
            delete this.sets[jSet];
        }
    }

    find(i) {
        return this.map[i];
    }
}

const run = s => {
    const lines = _.map(
        _.split(s, '\n'),
        line => {
            const [, id, list] = /(\d+)\s<->\s([\d\s,]+)/g.exec(line);
            return {
                id: parseInt(id),
                links: _.map(_.split(list, ', '), a => parseInt(a))
            }
        }
    );
    const uf = new UF(lines.length);
    _.forEach(lines, line => _.forEach(line.links, link => uf.union(link, line.id)));
    return _.size(uf.sets);
};
