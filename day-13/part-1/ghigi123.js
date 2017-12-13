const _ = require('lodash')

const run = s => {
	const lines = _.keyBy(_.map(
		_.split(s, '\n'),
		line => {
			const [, id, range] = /(\d+)\:\s(\d+)/g.exec(line);
			return {
				id: parseInt(id),
				range: parseInt(range)
			}
		}
	), 'id');

	const indices = _.range(1 + _.max(_.map(lines, 'id')));
	const firewall = _.map(indices, idx => idx in lines ? lines[idx] : { id: idx, range: 0 });
	const positions = _.map(indices, () => ({ pos: 0, speed: 1 }));

	return _.reduce(
		indices,
		(acc, packet_pos) => {			
			if(positions[packet_pos].pos === 0) {
				acc += firewall[packet_pos].id * firewall[packet_pos].range;
			}
			_.forEach(positions, (pos, idx) => {
				(pos.pos === 0) && (pos.speed = 1);
				(pos.pos === firewall[idx].range - 1) && (pos.speed = -1);
				pos.pos += pos.speed
			});
			return acc;
		},
		0
	)
};
