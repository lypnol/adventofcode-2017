#! /usr/bin/env python3

import argparse
import os.path
import sys


class FileNotEmptyException(Exception): pass

def mkdirp(path):
	if not os.path.exists(path):
		os.makedirs(path)

def make_dirs(day, parts):
	dirs = []
	day_dir = "./day-{:02d}".format(day)
	mkdirp(day_dir)
	parts_dirs = [ "{day_dir}/part-{part}".format(day_dir=day_dir, part=part) for part in parts ]
	for part_dir in parts_dirs:
		mkdirp(part_dir)
		inputs_dir = "{part_dir}/inputs".format(part_dir=part_dir)
		mkdirp(inputs_dir)
		dirs.append((part_dir, inputs_dir))
	return dirs

def create_submission(author, path, language):
	class_name = ''.join(x for x in "{} submission".format(author).title() if not x.isspace())
	submission_file = os.path.join(path, author + "." + language)
	if language == 'py':
		submission_content = """from runners.python import Submission

class {class_name}(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		pass

""".format(class_name=class_name)
	elif language == 'js':
		submission_content = """
/**
 * @param {{string}} s puzzle input in string format
 * @returns solution flag
 */
run = s => {
	// Your code goes here
};

"""

	if os.path.exists(submission_file):
		raise FileNotEmptyException("{} not empty".format(submission_file))
	with open(submission_file, 'w') as f:
		f.write(submission_content)
	print("created "+submission_file)

def create_input(author, path):
	input_file = os.path.join(path, author + ".txt")
	if os.path.exists(input_file):
		raise FileNotEmptyException("{} not empty".format(input_file))
	with open(input_file, 'a') as f:
		f.close()
	print("created "+input_file)

def main():
	parser = argparse.ArgumentParser(description='Creates new empty submission')
	parser.add_argument('author', type=str, help='Name of author (github login)')
	parser.add_argument('day', type=int, help='Day of problem (between 1 and 25)')
	parser.add_argument('-p', '--part', type=int, help='Create submission for one day part only', choices=[1, 2])
	parser.add_argument('-l', '--language', help='Use specified language', default="py", choices=["py", "js"])
	args = parser.parse_args()

	author = args.author.lower()
	dirs = make_dirs(args.day, [1, 2] if not args.part else [args.part])
	for submission_path, input_path in dirs:
		try:
			create_submission(author, submission_path, args.language)
		except FileNotEmptyException as e:
			print(e, file=sys.stderr)
			sys.exit(1)
		try:
			create_input(author, input_path)
		except FileNotEmptyException:
			pass
		except Exception as e:
			print(e, file=sys.stderr)
			sys.exit(1)

if __name__ == '__main__':
	main()
