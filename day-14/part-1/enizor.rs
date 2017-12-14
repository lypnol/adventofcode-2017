use std::env::args;


fn main() {
	println!("{}", run(args().nth(1).expect("Please provide an input")))
}

fn run(mut line: String) -> usize {
    line.push('-');
    let mut res: usize = 0;
    for x in 0..128 {
        res += knot_hash(&(line.clone() + &format!("{}", x))).iter().fold(
            0,
            |x,
             y| {
                x + y.count_ones()
            },
        ) as usize;
    }
    res
}

fn knot_hash(input: &str) -> Vec<usize> {
    let mut v = (0..256).collect::<Vec<usize>>();
    let mut lengths: Vec<usize> = input.chars().map(|c| c as usize).collect::<Vec<usize>>();
    lengths.append(&mut vec![17, 31, 73, 47, 23]);

    let mut pos = 0;
    let mut skip = 0;
    for _ in 0..64 {
        let res = knot(&mut v, &lengths, pos, skip);
        pos = res.0;
        skip = res.1;
    }
    // v is now the sparse hash, transform it in dense hash
    let mut dense_hash = vec![];
    for i in 0..16 {
        dense_hash.push(v[i * 16..(i + 1) * 16].iter().fold(0, |acc, &x| acc ^ x));
    }
    dense_hash
    // format in hex notation isn't needed
}

fn knot(mut v: &mut Vec<usize>, lengths: &[usize], pos: usize, skip: usize) -> (usize, usize) {
    let mut pos_res = pos;
    let mut skip_res = skip;
    let n = v.len();
    for &len in lengths {
        reverse(&mut v, pos_res, len);
        pos_res = (pos_res + len + skip_res) % n;
        skip_res += 1;
    }
    (pos_res, skip_res)
}

fn reverse(v: &mut Vec<usize>, pos: usize, len: usize) {
    let n = v.len();
    for i in 0..(len / 2) {
        let x = v[(pos + i) % n];
        v[(pos + i) % n] = v[(pos + len - 1 - i) % n];
        v[(pos + len - 1 - i) % n] = x;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn run_test() {
        assert_eq!(run("flqrgnkx".to_string()), 8108)
    }
}
