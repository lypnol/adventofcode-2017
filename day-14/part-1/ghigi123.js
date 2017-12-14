const _ = require('lodash');

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
	)
	return _.countBy(_.flatten(grid), i => i === '1')[true];
};