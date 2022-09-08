# import pandas as pd 
def remove_prefix(data):
    word = ["Mrs", "Ms", "Mr", "Smt", "Shree", "Shri", "Dr", "ER", "Prof", "I.A.S"]
    for j in word:
        if data.find(j)==0:
            data = data[len(j):]
    return data
def remove_whitespace(df2):
    df1 = []
    for x in df2:
        x = ''.join(filter(str.isalpha, remove_prefix(x)))
        df1.append(x)
    return df1


# remove_whitespace(["manav","shif$a","Bhak t"])
# print(remove_whitespace(["Mr Manav42","Mr Shubham ","Ms Bhak2ti"]))