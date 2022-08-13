import pandas

data_1 = pandas.read_csv("database1.csv")
data_2 = pandas.read_csv("database2.csv")

name_2 = data_2["name2"]

data_1["name2"] = name_2

data_1.drop('marks', inplace=True, axis=1)

print(data_1)

# final_data = pandas.read_csv("final_data.csv")

# list of name1, roll, name2

n1 = data_1["name1"].tolist()
n2 = data_2["name2"].tolist()
roll = data_1["roll number"].tolist()

# dict of list

dict = {
    'name_1': n1, 'name_2': n2, 'roll number': roll
}

fd = pandas.DataFrame(dict)

#saving the dataframe

fd.to_csv("final_data.csv")


# output1 = pandas.merge(data_1, data_2,
#                    on='name1',
#                    how='right')
#
# print(output1)


