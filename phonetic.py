def main(file1):
    import pandas as pd
    import abydos.phonetic as pho
    import abydos.distance as dis

    print("\nNumber of rows is :", len(file1), end="\n\n")

    name1 = file1["name1"]
    name2 = file1["name2"]

    s = pho.FuzzySoundex()
    d = dis.Cosine()
    l=[]

    for i in range(len(file1)):
        # generating soundex codes
        t1 = s.encode(name1[i])
        t2 = s.encode(name2[i])

        #checking percentage similarity of names and checking percentage similarity of soundex values and taking the greater values
        l.append(max(dis.sim(name1[i], name2[i]), dis.sim(t1,t2)))

    #creating a new dataframe to provide to return
    new_df = pd.DataFrame(list(zip(name1,name2,l)))
    return new_df



    #Russell Index (95) , Soundex (96) , RefinedSoundex (97), FuzzySoundex (99),
    #LEIN(96), Davidson(96), SoundD(96), Dolby(97),

if __name__ == "__main__":
    main()
