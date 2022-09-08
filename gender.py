def gender_match(age1,age2):
    if(age2==age1):
        return 100
    else:
         return 0

def encode(file1):
    import pandas as pd

    name1 = file1["name1"]
    name2 = file1["name2"]
    l=[]
    for i in range(len(file1)):
        l.append(gender_match(name1[i],name2[i]))

    new_df = pd.DataFrame(list(zip(name1,name2,l)))
    return new_df

def main():
    print("imported")

if __name__ == "__main__":
    main()


