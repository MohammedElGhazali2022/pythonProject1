sample_dict = {"name": "kelly","age": 25,"salary": 8000,"city": "new york"}
keys = ["name", "salary"]

for k in keys:
     del sample_dict[k]

print("Dictionary after removal of keys : " + str(sample_dict))