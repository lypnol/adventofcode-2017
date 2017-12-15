const _ = require('lodash')

const GenAMul = 16807;
const GenBMul = 48271;

const Mod = 2147483647;
const Mod2 = 65535;

const run = s => {
	let [, a, b] = /(\d+)\n.*?(\d+)/g.exec(s);
	let A = parseInt(a), B = parseInt(b), N = 0;
	for (let i = 0; i < 5000000; i++) {
		do A = (A * GenAMul) % Mod; while(A & 3)
		do B = (B * GenBMul) % Mod; while(B & 7)
		N += ((A & Mod2) ^ (B & Mod2)) === 0;
	}
	return N;
};
