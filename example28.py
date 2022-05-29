from turtle import distance
from example26 import read_file

def gen_dict(filename):
    data = read_file(filename)
    dictionary = {}
    for stuff in data[1:]:
        dictionary.update({stuff[0]: {"x": stuff[1], "y": stuff[2], "z": stuff[3]}})
    return dictionary

def edis(atom1, atom2, dictionary):
    xdiskare = (float(dictionary[atom1]["x"]) - float(dictionary[atom2]["x"])) ** 2
    ydiskare = (float(dictionary[atom1]["y"]) - float(dictionary[atom2]["y"])) ** 2
    zdiskare = (float(dictionary[atom1]["z"]) - float(dictionary[atom2]["z"])) ** 2
    dist = (xdiskare + ydiskare + zdiskare) ** (1 / 2)
    return dist

if __name__ == "__main__":
    atom_dict = gen_dict("atom_file")
    print(edis("atom7", "atom3", atom_dict))