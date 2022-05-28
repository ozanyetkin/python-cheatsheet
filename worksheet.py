# glucose_concentration	blood_pressure	serum_insulin	Body_mass_index	Age
# 148	72	NA	33.6	50
# 85	66	NA	26.6	31

dict_example = {
    "glucose_concentration": 148,
    "blood_pressure": 72,
}
dict_example.update({"glucose_concentration": 85})
print(dict_example)