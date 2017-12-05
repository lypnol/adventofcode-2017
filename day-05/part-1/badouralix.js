
/**
* @param {{string}} s puzzle input in string format
* @returns solution flag
*/
function run(s) {
	const offsets = s.split('\n');
	let index = 0,
		steps = 0;

	while (index >= 0 && index < offsets.length) {
		index += offsets[index]++;
		steps++;
	}

	return steps;
}
