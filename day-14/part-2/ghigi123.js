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
		if (iSet !== jSet) {
			_.assign(this.sets[iSet], this.sets[jSet]);
			_.forEach(this.sets[jSet], (i, k) => this.map[k] = iSet);
			delete this.sets[jSet];
		}
	}

	find(i) {
		return this.map[i];
	}
}

const copyTo = (table, subtable, index) => {
	const copy = _.clone(table);
	_.forEach(subtable, (e, i) => copy[(index + i) % table.length] = e);
	return copy;
};

const copyFrom = (table, index, length) => _.map(_.range(length), i => table[(index + i) % table.length]);

const round = (lengths, prevAcc) => _.reduce(
	lengths,
	(acc, length) => ({
		index: (acc.index + length + acc.skip) % acc.list.length,
		skip: acc.skip + 1,
		list: copyTo(acc.list, _.reverse(copyFrom(acc.list, acc.index, length)), acc.index)
	}),
	prevAcc);

const hash = s => {
	const lengths = _.concat(_.map(s, c => c.charCodeAt(0)), [17, 31, 73, 47, 23]);
	const sparseHash = _.reduce(
		_.range(64),
		acc => round(lengths, acc),
		{
			index: 0,
			skip: 0,
			list: _.range(256)
		}
	).list;
	const xoredHash = _.map(
		_.chunk(sparseHash, 16),
		chunk => _.reduce(chunk, (a, i) => a ^ i, 0)
	);
	return _.join(
		_.map(xoredHash, n => ('0000000' + n.toString(2)).slice(-8))
		, ''
	);
};

const run = s => {
	const grid = _.map(
		_.range(128),
		idx => _.map(hash(s + '-' + idx), a => a)
	);

	const co = (i1, i2) => i2 + 128 * i1;

	const uf = new UF(128 * 128);
	_.forEach(_.range(128), i1 =>
		_.forEach(_.range(128), i2 =>
			_.forEach(_.range(-1, 2), n1 =>
				_.forEach(_.range(-1, 2), n2 =>
					(Math.abs(n1) ^ Math.abs(n2)) &&
					(n1 + i1 < 128 && n2 + i2 < 128 && n1 + i1 >= 0 && n2 + i2 >= 0) &&
					(grid[i1][i2] === '1' && grid[i1 + n1][i2 + n2] === '1') &&
					uf.union(co(i1, i2), co(n1 + i1, n2 + i2))
				)
			)
		)
	);

	return _.size(_.filter(uf.sets, set =>
		_.size(set) > 1 || grid[Math.floor(parseInt(_.keys(set)[0]) / 128)][parseInt(_.keys(set)[0]) % 128] === '1'
	));
};