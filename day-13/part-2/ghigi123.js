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

	let delay = 0
	let caught = true
	while (caught) {
		caught = false;
		_.forEach(lines, ({id: layer, range:range})=>{
			if((delay + layer) % (2*range - 2) == 0){
				caught = true;
				delay += 1;
				return true;
			}
		});
	}
	return delay;
};
