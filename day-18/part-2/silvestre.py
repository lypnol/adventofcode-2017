from collections import defaultdict
from time import sleep
from threading import Thread
from queue import Queue
from submission import Submission


code_stopped_1 = False
code_stopped_2 = False

queue1 = Queue()
queue2 = Queue()

class SilvestreSubmission(Submission):

    def run(self, s):
        instructions, registers = self.read_input(s)

        

        running_code_1 = SilvestreThread(
            queue1, queue2, 
            code_stopped_1, code_stopped_2,
            instructions, registers, 0)
        running_code_2 = SilvestreThread(
            queue2, queue1,
            code_stopped_1, code_stopped_2,
            instructions, registers, 1)

        running_code_1.start()
        running_code_2.start()

        running_code_1.join()
        running_code_2.join()

        return running_code_1.counter


    def read_input(self, s):
        inputs = s.split("\n")
        instructions = list()
        registers = defaultdict(int)
        for row in inputs:
            rl = row.split()
            if rl[0] == "snd" or rl[0] == "rcv":
                instructions.append((rl[0], rl[1], None))
            else:
                instructions.append((rl[0], rl[1], rl[2]))
        return instructions, registers


class SilvestreThread(Thread):

    def __init__(self, own_queue, other_queue, own_stopped, other_stopped, instructions, registers, program_id):
        Thread.__init__(self)
        self.own_queue = own_queue
        self.other_queue = other_queue
        self.own_stopped =own_stopped
        self.other_stopped = other_stopped
        self.instructions = instructions.copy()
        self.registers = registers.copy()
        self.counter = 0
        self.program_id = program_id

    def run(self):
        instructions = self.instructions
        registers = self.registers
        registers['p'] = self.program_id

        i = 0  # index de curr dans instructions
        while i <= len(instructions):
            curr = instructions[i]
            cmd, x, y = curr

            try:
                x_val = int(x)
            except ValueError:
                x_val = registers[x]
            try:
                y_val = int(y)
            except ValueError:
                y_val = registers[y]
            except TypeError:
                pass

            if cmd == "jgz" and x_val != 0:
                i = i + y_val
                continue
            if cmd == "snd":
                self.counter += 1
                self.other_queue.put(x_val)
                #print(Thread.getName(self),' has put the item ', x_val)
                #import pdb; pdb.set_trace()
            elif cmd == "set":
                registers[x] = y_val
            elif cmd == "add":
                registers[x] = x_val + y_val
            elif cmd == "mul":
                registers[x] = x_val * y_val
            elif cmd == "mod":
                registers[x] = x_val % y_val
            elif cmd == "rcv":
                recieved = False
                self.own_stopped = True
                print(Thread.getName(self), self.own_queue.qsize(), self.other_queue.qsize(), self.own_stopped, self.other_stopped)
                while not recieved:
                    if not self.own_queue.empty():
                        #import pdb; pdb.set_trace() 
                        item = self.own_queue.get()
                        self.own_queue.task_done()
                        recieved = True
                        self.own_stopped = False
                        #print(Thread.getName(self),' has consumned the item ', item)
                    else:
                        if self.other_stopped and self.own_stopped:
                            return
                        #print(Thread.getName(self), ' is waiting...')
                        sleep(1)

            i += 1