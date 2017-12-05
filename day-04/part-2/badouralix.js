
/**
* @param {{string}} s puzzle input in string format
* @returns solution flag
*/
function run(s) {
	return s.split('\n').filter(isValid).length;
}

function isValid(passphrase) {
	const set = new Set();
	passphrase.split(' ').forEach(word => {
		set.add(word.split('').sort().join(''));
	});
	return passphrase.split(' ').length == set.size;
}
