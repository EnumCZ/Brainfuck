class Brainfuck:


    # creating cell list
    cell_list = [0] * 10000
    

    def __init__(self, token_list):
        self.tokens = token_list


    def evaluate(self):
        # current token
        pos_counter = 0
        # current cell
        current_cell = 0
	# parasing tokens
        while pos_counter in range(0, len(self.tokens) - 1):
            # +
            if self.tokens[pos_counter] == "+":
                self.cell_list[current_cell] += 1
                pos_counter += 1
            # -
            elif self.tokens[pos_counter] == "-":
                self.cell_list[current_cell] -= 1
                pos_counter += 1
            # <
            elif self.tokens[pos_counter] == "<":
                current_cell -= 1
                pos_counter += 1
            # >
            elif self.tokens[pos_counter] == ">":
                current_cell += 1
                pos_counter += 1
            # .
            elif self.tokens[pos_counter] == ".":
                print(chr(self.cell_list[current_cell]))
                pos_counter += 1
            # ,
            elif self.tokens[pos_counter] == ",":
                self.cell_list[current_cell] = ord(input())
                pos_counter += 1
            # [
            elif self.tokens[pos_counter] == "[":
                if self.cell_list[current_cell] == 0:
                    while self.tokens[pos_counter] != "]":
                        pos_counter += 1
                else:
                    pos_counter += 1
            # ]
            elif self.tokens[pos_counter] == "]":
                if self.cell_list[current_cell] != 0:
                    while self.tokens[pos_counter] != "[":
                        pos_counter -= 1
                else:
                    pos_counter += 1
                    
