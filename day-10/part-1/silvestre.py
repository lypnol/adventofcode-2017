from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        lengths = list(map(int,s.split(",")))
        main_list = list(range(256))
        current_position = 0
        skip_size = 0           
        for length in lengths:
            i1 = current_position
            i2 = (current_position + length) % 256

            if i1 < i2:
                sublist = main_list[i1 : i2]
                sublist.reverse()

                l1 = main_list[:i1]
                l2 = main_list[i2:]

                main_list = l1 +sublist + l2
            elif i1 > i2:
                sublist = main_list[i1:] + main_list[:i2]
                assert(len(sublist) == length)
                sublist.reverse()

                if i2 != 0:
                    main_list = sublist[-i2:] + main_list[i2:i1] + sublist[:(256-i1)]
                else :
                    main_list = main_list[i2:i1] + sublist[:(256-i1)]

            current_position = (current_position + length + skip_size) % 256
            skip_size += 1
            assert(len(main_list)==256)
            

        return main_list[0] * main_list[1] 

            
            

