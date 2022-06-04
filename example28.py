from re import L
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

def contact_check(start, dictionary, contact_dict):
    stop = len(dictionary.keys())
    for i in range(start, stop + 1):
        if edis(f"atom{start}", f"atom{i}", dictionary) <= 4:
            contact_dict[f"atom{start}"].update({f"atom{i}": edis(f"atom{start}", f"atom{i}", dictionary)})
            contact_dict[f"atom{i}"].update({f"atom{start}": edis(f"atom{start}", f"atom{i}", dictionary)})
        else:
            contact_dict[f"atom{start}"].update({f"atom{i}": edis(f"atom{start}", f"atom{i}", dictionary)})
            contact_dict[f"atom{i}"].update({f"atom{start}": edis(f"atom{start}", f"atom{i}", dictionary)})
    if start == stop:
        return contact_dict
    else:
        return contact_check(start + 1, dictionary, contact_dict)

if __name__ == "__main__":
    atom_dict = gen_dict("atom_file")
    print(edis("atom7", "atom3", atom_dict))
    c_dict = dict.fromkeys(atom_dict.keys(), {})
    for key in c_dict.keys():
        c_dict[key] = {}
    print(contact_check(1, atom_dict, c_dict))
