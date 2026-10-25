class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.cookie = 0

    def __str__(self):
        n = self.cookie
        ans = ""
        while n > 0:
            ans += "🍪"
            n -= 1
        return ans

    def deposit(self, n):
        if (self.capacity - n) < 0:
            raise ValueError("Cannot add more cookies")
        self.cookie += n
        self.capacity -= n

    def withdraw(self, n):
        if (self.cookie - n) < 0:
            raise ValueError("Cannot withdraw more cookies")
        self.cookie -= n
        self.capacity -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self.cookie

# def main():
#     jar = Jar()
#     jar.deposit(5)
#     print(str(jar))


# if __name__ == "__main__":
#     main()
    


    