class Tokenizer:


    @staticmethod
    def tokenize(string):
        token_list = []
        for char in string:
            if char in ["+", "-", "<", ">", ".", "[", "]", ","]:
                token_list.append(char)
        return token_list
