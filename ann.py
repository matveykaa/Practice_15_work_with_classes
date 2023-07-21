from functools import total_ordering

@total_ordering
class RealString:
    def __init__(self, string):
        self.string = str(string)

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.string) < len(other.string)
        return False

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.string) == len(other.string)
        return False


if __name__ == '__main__':
    str1 = RealString('Молоко')
    str2 = RealString('Абрикосы растут')
    str3 = RealString('Золото')
    str4 = RealString([1, 2, 3])
    print(str1 < str4)
    print(str1 >= str2)
    print(str1 == str3)