# python libs
import argparse
import traceback
import glob, sys, imp, inspect, datetime, re
import os.path
from os import walk

from submission import Submission

show_debug = False
author_list = None
except_list = None
restricted_mode = False

# To print colors in terminal
class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


DAY_PATH_PATTERN  = 'day-[0-9]*'
CONTEST_PATH_PATTERN = 'part-[0-9]*'

class DifferentAnswersException(Exception): pass

def _context_name(context_path):
    return context_path.replace('/','_').replace('-','_')

# Return the list of the contests
# It should be the list of the directories matching day-<a number>
def _get_days():
    return sorted(glob.glob(DAY_PATH_PATTERN), key=lambda x: abs(int(x[-2:])))

# Return the list of the contests path for the given day path
def _get_contests_path_for_day(day_path):
    return glob.glob(day_path + '/' + CONTEST_PATH_PATTERN)

# Return contest number from path
def _get_constest_number(contest_path):
    return int(contest_path.split('-')[-1])

# Returns the lists of possible submission files for the given contest
def _find_submissions_for_contest(contest_path):
    submission_files = []
    for _, _, files in walk(contest_path):
        for filename in files:
            submission, ext = os.path.splitext(filename)
            if ext == '.py':
                submission_files.append(submission)
    return submission_files

def _load_submission(contest_path, submission):
    submission_path = '%s/%s.py' % (contest_path, submission)
    contest = _context_name(contest_path)
    submission_module = imp.load_source('submission_%s_%s' % (contest, submission), submission_path)

    submission_class = None
    classes = inspect.getmembers(submission_module, inspect.isclass)
    for _, cls_submission in classes:
        if issubclass(cls_submission, Submission):
            return cls_submission

    return None

def load_submissions_for_contest(contest_path):
    submission_files = _find_submissions_for_contest(contest_path)
    contest = _context_name(contest_path)
    submissions = []
    for submission_file in submission_files:
        author = os.path.basename(submission_file).split('.')[0]
        submission = None
        try:
            submission = _load_submission(contest_path, submission_file)
        except:
            if show_debug:
                print(bcolors.RED + ''.join(traceback.format_exc()) + bcolors.ENDC, file=sys.stderr)
        if submission is not None:
            submissions.append((author, submission))
    return submissions

def get_inputs_for_contest(contest_path):
    if not os.path.exists(os.path.join(contest_path, 'inputs')):
        return []
    inputs = []
    for input_file in glob.glob(contest_path + '/inputs/*.txt'):
        with open(input_file, 'r') as content_file:
            input_name = os.path.os.path.basename(input_file).split('.')[0].lower()
            inputs.append((input_name, content_file.read().rstrip()))
    return inputs

def _run_submission(author, submission, input):
    result = None
    try:
        result = submission.run(input)
    except:
        if show_debug and len(submission.get_debug_stack()) > 0:
            print(bcolors.RED + "Debug trace for %s " % author, file=sys.stderr)
            stack = submission.get_debug_stack()
            print('\n'.join(submission.get_debug_stack()[:15]), file=sys.stderr)
            if len(stack) > 15:
                print('and %s other lines...' % (len(stack) - 15), file=sys.stderr)
            print(bcolors.ENDC)
    return result

def run_submissions_for_contest(contest_path):
    print("\n" + bcolors.MAGENTA + bcolors.BOLD + "* contest %s:" % os.path.basename(contest_path) + bcolors.ENDC)
    submissions = load_submissions_for_contest(contest_path)
    inputs = get_inputs_for_contest(contest_path)

    try:
        for input_author, input_content in inputs:
            prev_ans = None
            answers = []
            if not restricted_mode:
                print("---------------------------------------------------")
                print("On input from {yellow}{author}{end}".format(
                    yellow=bcolors.YELLOW,
                    end=bcolors.ENDC,
                    author=input_author))
                print("---------------------------------------------------")
            for author, submission in submissions:
                time_before = datetime.datetime.now()
                submission_obj = submission()
                if restricted_mode and author != input_author:
                    continue
                if author_list is not None and author not in author_list:
                    continue
                if except_list is not None and author in except_list:
                    continue
                answer = _run_submission(author, submission_obj, input_content)
                time_after = datetime.datetime.now()
                msecs = (time_after - time_before).total_seconds() * 1000
                print("\t{green}{author}{end}\t | {blue}{answer}{end} \t | {msecs:8.2f} ms".format(
                    green=bcolors.GREEN,
                    author=author,
                    end=bcolors.ENDC,
                    blue=bcolors.BLUE,
                    answer=answer,
                    yellow=bcolors.YELLOW,
                    msecs=msecs))

                if prev_ans != None and prev_ans != str(answer):
                    raise DifferentAnswersException("we don't agree for {}".format(contest_path))
                prev_ans = str(answer)
    except DifferentAnswersException as e:
        print(bcolors.RED, "ERROR", e, bcolors.ENDC, file=sys.stderr)
        sys.exit(1)

def run_submissions_for_day(day, day_path, part=None):
    first_run = True
    contest_paths = _get_contests_path_for_day(day_path)
    for contest_path in contest_paths:
        if part is not None and _get_constest_number(contest_path) != part:
            continue
        if except_list != None and day in except_list:
            continue

        if first_run:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(bcolors.RED + bcolors.BOLD + "Running submissions for day %s:" % day +bcolors.ENDC)
            first_run = False

        run_submissions_for_contest(contest_path)
        print("\n")

def run_submissions():
    for day_path in _get_days():
        day = day_path[4:]
        run_submissions_for_day(day, day_path)


def main():
    global show_debug
    global author_list
    global except_list
    global restricted_mode

    day = None
    part = None

    parser = argparse.ArgumentParser(description='Runs contest submissions')
    parser.add_argument("--last", help="Runs submissions from last day", action="store_true")
    parser.add_argument("-d", "--day", help="Runs submissions for specific day", type=int)
    parser.add_argument("-p", "--part", help="Runs submissions for specific day part", type=int)
    parser.add_argument("-a", "--authors", help="Runs submissions from specific authors, ex: user1,user2", type=str)
    parser.add_argument("-i", "--ignore", help="Ignores submissions from specific authors", type=str)
    parser.add_argument("-r", "--restricted", help="Restricts inputs on specified author", action="store_true", default=False)
    parser.add_argument("-v", "--verbose", help="Enable debug mode", action="store_true")
    args = parser.parse_args()

    restricted_mode = args.restricted
    show_debug = args.verbose

    if args.last:
        day = _get_days()[-1][4:]
    elif args.day:
        day = args.day

    if args.part:
        part = args.part

    if args.authors:
        author_list = args.authors.split(',')

    if args.ignore:
        except_list = args.ignore.split(',')


    if day is None and part is not None:
        for day_path in _get_days():
            day = day_path[4:]
            run_submissions_for_day(day, day_path, part)
    elif day is None and part is None:
        # Full test
        run_submissions()
    elif part is None:
        run_submissions_for_day(day, 'day-%02d' % day)
    else:
        run_submissions_for_day(day,'day-%02d' % day, part)

if __name__ == "__main__":
   main()
