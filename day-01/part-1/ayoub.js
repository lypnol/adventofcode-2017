
/**
* @param {{string}} s puzzle input in string format
* @returns solution flag
*/
function run(s) {
	let r = 0;
	for (let i = 0; i < s.length; i++) {
		if (parseInt(s[i]) == parseInt(s[(i+1) % s.length]))
			r += parseInt(s[i]);
	}
	return r;
}

