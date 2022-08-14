def main():
    import pandas as pd
    import abydos.phonetic as pho

    file = pd.read_csv('test-purpose.csv')

    print("\nNumber of rows is :", len(file), end="\n\n")

    name1 = file["name1"]
    name2 = file["name2"]
    isSame = file["isSame"]

    # make algo function array
    rus = pho.RussellIndex()
    sdx = pho.Soundex()
    ref = pho.RefinedSoundex()
    dmo = pho.DaitchMokotoff()
    nys = pho.NYSIIS()
    mtc = pho.MRA()
    mta = pho.Metaphone()
    met = pho.DoubleMetaphone()
    cav = pho.Caverphone()
    alp = pho.AlphaSIS()

    fuz = pho.FuzzySoundex()
    phi = pho.Phonex()
    nem = pho.Phonem()
    pix = pho.Phonix()
    nic = pho.PHONIC()
    #fre = pho.SPFC()
    can = pho.StatisticsCanada()
    lei = pho.LEIN()
    sou = pho.MetaSoundex()
    rog = pho.RogerRoot()

    eud = pho.Eudex()
    par = pho.ParmarKumbharana()
    dav = pho.Davidson()
    sda = pho.SoundD()
    fir = pho.PSHPSoundexFirst()
    dol = pho.Dolby()
    eng = pho.NRL()
    ans = pho.Ainsworth()
    bda = pho.BeiderMorse()
    onc = pho.ONCA()
    msd = pho.MetaSoundex()

    algo_name = ["Russell Index", "Soundex", "RefinedSoundex", "DaitchMokotoff", "NYSIIS", "MRA",
                "Metaphone", "Double Metaphone", "Caverphone", "AlphaSIS", "FuzzySoundex", "Phonex",
                "Phonem", "Phonix", "Phonic", "StatisticsCanada", "LEIN", "MetaSoundex",
                "RogerRoot", "Eudex", "ParmarKumbharana", "Davidson", "SoundD", "PSHPSoundexFirst",
                "Dolby", "NRL", "Ainsworth", "BeiderMorse", "ONCA", "MetaSoundex"]

    algo = [rus, sdx, ref, dmo, nys, mtc, mta, met, cav, alp,
            fuz, phi, nem, pix, nic, can, lei, sou, rog,
            eud, par, dav, sda, fir, dol, eng, ans, bda, onc, msd]

    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(file)):

        for j in range(len(algo)):

            t1 = algo[j].encode(name1[i])
            t2 = algo[j].encode(name2[i])
            # print(i, j, t1, t2)
            if t1 == t2 and isSame[i] == "yes" or t1 != t2 and isSame[i] == "no":
                # print('algo was successful', i, j)
                # else:
                # print("algo was not successful", i, j)

                count[j] += 1
            # print(f'{t1}  {t2}')

    for i in range(len(count)):
        eff = count[i] / len(file) * 100
        print(f'Efficiency of {algo_name[i]} is : {eff}%')
        if eff >= 95:
            print(f'{algo_name[i]} algorithm works best!!!')

if __name__ == "__main__":
    main()
