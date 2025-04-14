class Calculator:
    def add(self, string: str) -> float:
        negative_numbers = []
        sum = 0.0
        string = string.strip()  # remove all left and right whitespaces
        if not string:  # for empty/whitespaces
            return sum

        # // [delimiter] \n [numbers…] 
        # delimiter check 
        delimiter = ','
        if string[0:2] == '//':
            delimiter = string[2]
            string = string[4:]  # skip over "//<delimiter>\n"

        string = string.replace('\n', delimiter)  # replace \n with delimiter
        ls = string.split(delimiter)
        for i in ls:
            i = i.strip()
            if i:
                num = float(i)
                if num < 0:
                    negative_numbers.append(num)
                sum += num

        if negative_numbers:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negative_numbers))}")

        return sum


if __name__ == "__main__":
    print(Calculator().add("//;\n1;2"))  
    print(Calculator().add("//;\n1;-2"))  
