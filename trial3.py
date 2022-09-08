import pandas as pd
import abydos.phonetic as pho
import abydos.distance as dis
import white

def phonetic_comparison(col1,col2,col3):
    """Takes two lists as input and returns the similarity of each row based on phoneti comparison."""
    col1 = white.remove_whitespace(col1)
    col2 = white.remove_whitespace(col2)
    col3 = white.remove_whitespace(col3)
    # for i in col:
    #     i = white.remove_whitespace(i)
    # out_df = pd.DataFrame(list(zip(col1,col2,col3)))
    s = pho.FuzzySoundex()
    d = dis.Cosine()
    l=[]
    for i in range(len(col1)):
    # generating soundex codes
        s1 = s.encode(col1[i])
        s2 = s.encode(col2[i])
        s3 = s.encode(col3[i])

        #checking percentage similarity of names and checking percentage similarity of soundex values and taking the greater values
        l1 = max(dis.sim(col1[i], col2[i]), dis.sim(s1,s2))
        l2 = max(dis.sim(col1[i], col3[i]), dis.sim(s1,s3))
        l_final = ((l1+l2)/2)*100
        l.append(l_final)
    #     print(col1[i],col2[i],col3[i],l1,l2,l_final,end=" ")
    # input()

    #creating a new dataframe to provide to return
    new_df = pd.DataFrame(list(zip(col1,col2,col3,l)),columns=['Name1','Name2','Name3','percentage'])
    return new_df
    # count_df.append(child_df_out)

def age_comparison(col1,col2,col3):
    """Takes two lists as input and returns the similarity of each row based on age."""
    # col1 = white.remove_whitespace(col1)
    # col2 = white.remove_whitespace(col2)
    # col3 = white.remove_whitespace(col3)
    # out_df = pd.DataFrame(list(zip(col1,col2,col3)))
    l=[]

    def age_compare(age1,age2):
        if(age1==age2):
            return 100
        elif(age1==age2-1 or age1==age2+1):
            return 50
        elif(age1==age2-2 or age1==age2+2):
            return 20
        else:
            return 0

    for i in range(len(col1)):
        # generating soundex codes
        t1 = age_compare(col1[i],col2[i])
        t2 = age_compare(col1[i],col3[i])
        l.append((t1+t2)/2)
    #     print(col1[i],col2[i],col3[i],t1,t2)
    # input()

    #creating a new dataframe to provide to return
    new_df = pd.DataFrame(list(zip(col1,col2,col3,l)),columns=['age1','age2','age3','percentage'])
    return new_df

def unique_comparison(col1,col2,col3):
    """Takes two lists as input and returns the similarity of each row based on perfect match."""
    if(type(col1[0])==type('abc')):
        col1 = white.remove_whitespace(col1)
        col2 = white.remove_whitespace(col2)
        col3 = white.remove_whitespace(col3)
    # out_df = pd.DataFrame(list(zip(col1,col2)))
    l=[]
    for i in range(len(col1)):
        x=0
        if(col1[i]==col2[i]):
            x+=1
        # if(col2[i]==col3[i]):
            # x+=1
        if(col1[i]==col3[i]):
            x+=1
        x=(x/2)*100
        l.append(x)
    #     print(col1[i],col2[i],col3[i],x)
    # input()
    #creating a new dataframe to provide to return
    new_df = pd.DataFrame(list(zip(col1,col2,col3,l)),columns=['unq1','unq2','unq3','percentage'])
    return new_df