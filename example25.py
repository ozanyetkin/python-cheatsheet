encoded_str = "6 14 14 3,9 14 1,8 13,3 4 2 17 24 15 19 8 13 6,19 7 8 18"
en_alphabet = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"

en_letters = en_alphabet.replace(" ", "").split(",")

decode_dict = {}
for i in range(26):
    decode_dict.update({i + 1: en_letters[i]})

encoded_msg = encoded_str.split(",")
message = ""
for msg in encoded_msg:
    for i in range(25, 0, -1):
        msg = msg.replace(f"{i}", decode_dict[i + 1])
    message += msg.replace(" ", "") + " "

print(message)
