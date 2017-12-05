
/**
* @param {{string}} s puzzle input in string format
* @returns solution flag
*/
function run(s) {
	const offsets = s.split('\n').map(x => parseInt(x));
	let index = 0, steps = 0,
		currentOffset;

	while (index >= 0 && index < offsets.length) {
		currentOffset = offsets[index];
		offsets[index] += offsets[index] < 3 ? 1 : -1;
		index += currentOffset;
		steps++;
	}

	return steps;
}