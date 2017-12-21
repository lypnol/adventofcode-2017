import math
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        initial_configs, final_configs = self.read_input(s)

        current_config = (('.','#','.'),('.','.','#'),('#','#','#'))

        n = 0 # iterations number
        while n <= 5:
            # Split
            # import pdb; pdb.set_trace()
            blocks = self.split_config(current_config)

            for k, block in enumerate(blocks):                
                # Tester current config pour matcher
                t = 0
                while not block in initial_configs:
                    block = self.transform_block(block, t)
                    print(block , t)
                    t += 1
                    assert t < 7, f'An error occured, block: {block}'

                i = initial_configs.index(block)

                # Effectuer la transformation
                blocks[k] = final_configs[i]

            # Recoller les morceaux
            current_config = self.merge_block(current_config, blocks)
            n += 1

        # Compter les points "#"
        return sum(i.count('#') for i in current_config)

    def transform_block(self, block, t):
        if t < 3 or t > 3:
            block = self.rotate_block(block)
        elif t == 3:
            block = self.flip_block(block)
        return block

    def rotate_block(self, block):
        new_block = []
        for i in range(len(block)):
            if len(block) == 2:
                # import pdb; pdb.set_trace()
                pass
            new_block.append(tuple([row[i] for row in reversed(list(block))]))
        return tuple(new_block)

    def flip_block(self, block):
        new_block = []
        for i in range(len(block)):
            row = list(block[i])
            row.reverse()
            new_block.append(tuple(row))
        return tuple(new_block)

    def merge_block(self, old_config, blocks):
        new_config_len = len(old_config) + int(math.sqrt(len(blocks)))
        block_len = len(blocks[0])
        new_config = []
        for i in range(new_config_len):
            k = int((i//block_len)*math.sqrt(len(blocks)))
            raw_row = [block[i%block_len] for block in blocks[k:k+2]]
            row = [y for x in raw_row for y in x]
            new_config.append(tuple(row))
            # import pdb; pdb.set_trace()
        return new_config

    def split_config(self, current_config):
        config_len = len(current_config[0])
        blocks = []
        if config_len % 3 == 0:
            for i in range(config_len//3):
                for j in range(config_len//3):
                    blocks.append(tuple([row[j:j+3] for row in current_config[i:i+3]]))
        elif config_len % 2 == 0:
            for i in range(config_len//2):
                for j in range(config_len//2):
                    blocks.append(tuple([row[j:j+2] for row in current_config[i:i+2]]))        
        return blocks

    def read_input(self, s):
        """
        On crée deux listes de configuration.
        Une rule est un tuple (initial_config, final_config)
        une config est un tuple de tuple ((row1),(row2)) par exemple

        """
        initial_configs = []
        final_configs = []
        for str_row in s.split("\n"):
            str_configs = str_row.split(" => ")
            for i, str_config in enumerate(str_configs):
                config = []
                rows = str_config.split("/")
                for row in rows:
                    config.append(tuple(row))
                if i == 0:
                    initial_configs.append(tuple(config))
                else:
                    final_configs.append(tuple(config))
        
        return initial_configs, final_configs
