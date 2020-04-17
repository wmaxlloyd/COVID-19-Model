from typing import List

class PrimeGenerator:
    def __init__(self):
        self.current = 2
        self.list: List[int] = [self.current]
    
    def next(self):
        while not self.__is_prime(self.current):
            self.current += 1
        self.list.append(self.current) 
        return self.current

    def __is_prime(self, num):
        for prime in self.list:
            if num % prime == 0:
                return False
        return True