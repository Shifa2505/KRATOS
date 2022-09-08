def main(file1,file2,file3):
    import pandas as pd
    import trial3

    # file1 = pd.read_csv('test-purpose-1.csv')
    # file2 = pd.read_csv('test-purpose-2.csv')

    #Uniqueid,PanchayatCode,childname,fathername,Gender,Age
    child1 = file1['Firstname']
    child2 = file2['Firstname']
    child3 = file3['Firstname']
    father1 = file1['Lastname']
    father2 = file2['Lastname']
    father3 = file3['Lastname']
    age1 = file1['Age']
    age2 = file2['Age']
    age3 = file3['Age']
    gender1 = file1['Gender']
    gender2=file2['Gender']
    gender3=file3['Gender']
    

    # child=[]

    #count of dataframes
    count_df = []

    #child dataframe
    child_df = pd.DataFrame(list(zip(child1,child2,child3)),columns=['name1','name2','name3'])
    child_df_out=trial3.phonetic_comparison(child_df['name1'],child_df['name2'],child_df['name3'])
    count_df.append(child_df_out)
    # print(child_df)

    #father dataframe
    father_df = pd.DataFrame(list(zip(father1,father2,father3)),columns=['name1','name2','name3'])
    father_df_out=trial3.phonetic_comparison(father_df['name1'],father_df['name2'],father_df['name3'])
    count_df.append(father_df_out)
    # print(father_df)

    # #age dataframe
    age_df = pd.DataFrame(list(zip(age1,age2,age3)),columns=['name1','name2','name3'])
    age_df_out = trial3.age_comparison(age_df['name1'],age_df['name2'],age_df['name3'])
    count_df.append(age_df_out)
    # print(age_df_out)

    #gender dataframe
    gender_df = pd.DataFrame(list(zip(gender1,gender2,gender3)),columns=['name1','name2','name3'])
    gender_df_out = trial3.unique_comparison(gender_df['name1'],gender_df['name2'],gender_df['name3'])
    count_df.append(gender_df_out)
    # print(gender_df_out)
    # print(len(count_df))

    # averaging the percentage
    avg_list = []
    for j in range(len(file1)):#row count
        avg=0
        for i in range(len(count_df)):#col count
            avg+=count_df[i]['percentage']
        avg = round(avg/len(count_df), 2)
        avg_list.append(avg)
    # print(avg_list)
    # print(count_df)

    out_df = pd.DataFrame(list(zip(child1,child2,child3,father1,father2,father3,age1,age2,age3,gender1,gender2,gender3,avg)),columns=['FirstName1','FirstName2','FirstName3','LastName1','LastName2','LastName3','Age1','Age2','Age3','Gender1','Gender2','Gender3','Final Percent'])
    print(out_df)
    out_df.to_csv('output.csv')
    return out_df


if __name__ == "__main__":
    import pandas as pd
    f1 = pd.read_csv('test-purpose-1.csv')
    f2 = pd.read_csv('test-purpose-2.csv')
    f3 = pd.read_csv('test-purpose-3.csv')
    main(f1,f2,f3)