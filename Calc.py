class Calculator:
    def add(self, string: str) -> float:
        string = string.strip()
        if not string:                              # empty string check
            return 0.0

        string, delimiter = self.delimiter_check(string)    # fetching custom delimiter and modified string 
        string = string.replace('\n', delimiter)
        numbers = string.split(delimiter)

        sum = 0.0                                 
        negative_numbers = []

        sum , negative_numbers = self._add_calculator(numbers,sum,negative_numbers) # calculate sum

        if negative_numbers:
            raise ValueError(
                f"negative numbers not allowed {', '.join(map(str, negative_numbers))}"
            )

        return sum
    
    def _add_calculator(self,numbers,sum,negative_numbers):
        for value in numbers:
            value = value.strip()
            if not value:   # skipping invalid noise
                continue

            try:
                num = float(value)  # try to convert to float
            except ValueError:  # if it's not a valid float, raise an error
                raise ValueError(f"Invalid character(s) in input: {value}")

            if num < 0:
                negative_numbers.append(num)    # fetching negative numbers
            sum += num

        return sum , negative_numbers

    def delimiter_check(self, string: str)-> str:
        # detect custom delimiter using the format: //;<delimiter>\n...
        default_delimiter = ','
        if string.startswith('//'):
            return string[4:], string[2]  # skip "//<delimiter>\n"
        return string, default_delimiter


if __name__ == "__main__":
    print(Calculator().add("//;\n1;2"))     
    print(Calculator().add("//;\n1;-2"))    
