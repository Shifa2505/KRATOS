def main():
    import pandas as pd
    import abydos.phonetic as pho

    file = pd.read_csv('final_data.csv')
    
    print("\nNumber of rows is :",len(file),end="\n\n")
    
    name1 = file["name1"]
    name2 = file["name2"]
    isSame = file["isSame"]

    #make algo function array
    cav = pho.Caverphone()
    sdx = pho.Soundex()
    met = pho.DoubleMetaphone()
    nys = pho.NYSIIS()
    algo = [cav,sdx,met,nys]
    algoName = ["Caverphone","Soundex","Metaphone","NYSIIS"]
    count = [0,0,0,0]

    for i in range (len(file)):
        
        for j in range(len(algo)):
            
            t1 = algo[j].encode(name1[i])
            t2 = algo[j].encode(name2[i])
            # print(i,j,t1,t2)
            if((t1==t2 and isSame[i]=="yes") or (t1!=t2 and isSame[i]=="no")):
                count[j]+=1
            if(j==0):
                print(f'{t1}  {t2}')
        

    for i in range(len(count)):
        print(f'Efficiency of {algoName[i]} is {count[i]/len(file)*100}%')

if __name__=="__main__":
    main()