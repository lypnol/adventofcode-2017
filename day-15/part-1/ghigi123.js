const _ = require('lodash')

const GenAMul = 16807;
const GenBMul = 48271;

const Mod = 2147483647;
const Mod2 = 65535;

const run = s => {
	let [, a, b] = /(\d+)\n.*?(\d+)/g.exec(s);
	let A = parseInt(a), B = parseInt(b), N = 0;
	for (let i = 0; i < 40000000; i++) {
		A = (A * GenAMul) % Mod, B = (B * GenBMul) % Mod;
		N += ((A & Mod2) ^ (B & Mod2)) === 0;
	}
	return N;
};
