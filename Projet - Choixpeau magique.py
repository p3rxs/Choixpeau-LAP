with "Characters.csv"(mode = 'r', coding = 'utf-8') as f:
    tab = []
    lines = f.readlines()
    key_line = lines[0].strip()
    keys = key_line.split(';')
    for line in lines[1:]:
        line = line.strip()
        values = line.split(';')
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = values[i].strip()
        tab.append(dic)