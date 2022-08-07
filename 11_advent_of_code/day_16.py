from math import prod

with open("hexa.txt") as f:
    lines = f.readlines()

hexa = dict([l.replace("\n", "").split(" = ") for l in lines])
with open("11_advent_of_code/day_16.txt") as f:
    binary = f.readline()
binary_code = ""
for char in binary:
    binary_code += hexa[char]


def binary_to_decimal(binary=str):
    decimal = 0
    for power, char in enumerate(binary[::-1]):
        decimal += int(char) * 2 ** (power)
    return decimal


def literal_value_reader(literal=str):
    flag = True
    i = 0
    binary = ""
    while flag:
        binary += literal[i + 1 : i + 5]
        flag = literal[i] == "1"
        i += 5
    return binary_to_decimal(binary), i


def header_identifier(binary=str):
    version = binary_to_decimal(binary[0:3])
    type_id = binary_to_decimal(binary[3:6])
    return version, type_id


class Packet:
    def __init__(self, binary_code=str):
        self.code = binary_code
        self.version, self.type_id = header_identifier(binary_code)

    def get_length(self):
        if self.type_id == 4:
            return LiteralNumber(self.code).length
        else:
            return Operator(self.code).length

    def sum_versions(self):
        sum = 0
        if self.type_id == 4:
            sum += LiteralNumber(self.code).version
        else:
            sum += Operator(self.code).sum_versions()
        return sum

    def get_value(self):
        if self.type_id == 4:
            return LiteralNumber(self.code).decimal
        else:
            return Operator(self.code).get_value()


class LiteralNumber(Packet):
    def __init__(self, binary_code=str):
        super().__init__(binary_code)
        if self.type_id != 4:
            raise ValueError("Wrong packet type.Mistaken to be Literal")
        self.decimal, jump = literal_value_reader(self.code[6:])
        self.body = self.code[6 : 6 + jump]
        self.length = 6 + jump

    def get_value(self):
        return self.decimal


class Operator(Packet):
    def __init__(self, binary_code=str):
        super().__init__(binary_code)
        if self.type_id == 4:
            raise ValueError("Wrong packet type.Mistaken to be Operator")
        self.subpackets = []
        self.length_type_id = self.code[6]
        if self.length_type_id == "0":
            lengthofsubs = binary_to_decimal(self.code[7:22])
            self.length = 22 + lengthofsubs
            i = 0
            while lengthofsubs - i >= 11:
                self.subpackets.append(Packet(self.code[22 + i : 22 + lengthofsubs]))
                i += Packet(self.code[22 + i : 22 + lengthofsubs]).get_length()

            self.body = self.code[22 : 22 + i]

        if self.length_type_id == "1":
            self.subnum = binary_to_decimal(self.code[7:18])
            i = 0
            for _ in range(self.subnum):
                if binary_to_decimal(self.code[21 + i : 24 + i]) == 4:
                    sub = LiteralNumber(self.code[18 + i :])
                    self.subpackets.append(sub)
                else:
                    sub = Operator(self.code[18 + i :])
                    self.subpackets.append(sub)
                i += self.subpackets[-1].length
            self.length = 18 + i

    def sum_versions(self):
        sum = self.version
        for subpacket in self.subpackets:
            sum += (
                subpacket.sum_versions()
                if subpacket.type_id != 4
                else subpacket.version
            )
        return sum

    def get_value(self):
        values = [sub.get_value() for sub in self.subpackets]
        if self.type_id == 0:
            return sum(values)
        elif self.type_id == 1:
            return prod(values)
        elif self.type_id == 2:
            return min(values)
        elif self.type_id == 3:
            return max(values)
        elif self.type_id == 5:
            return 1 if values[0] > values[1] else 0
        elif self.type_id == 6:
            return 1 if values[0] < values[1] else 0
        else:
            return 1 if values[0] == values[1] else 0

pack = Packet(binary_code)
print(pack.sum_versions())
print(pack.get_value())