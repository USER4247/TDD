class Calculator:
    def add(self,string):
        sum = 0
        for i in string:
            i = int(i)
            sum += i
        return sum

if __name__ == "__main__":
    Calculator().add()