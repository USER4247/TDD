class Calculator:
    def add(self,string : str)-> float:
        sum = 0.0
        
        if not string.strip(): # for empty/ whitespaces
            return sum
        
        ls = string.split(',')
        for i in ls:
            sum += int(i)
        return sum

if __name__ == "__main__":
    print(Calculator().add('1,5'))