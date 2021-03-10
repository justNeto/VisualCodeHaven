import pandas as pd
df = pd.read_excel(r"excel_file.xslx")
df = df.truncate(before=120, after=149)
aux1 = df.loc[df['Uso'] == "Florero"]['#'].tolist()
aux = list()
# [1, 2, 4, 54, 65, 8]
for i in range(len(aux1)):
    for j in range(i+1, len(aux1)):
        aux.append([aux1[i], aux1[j]])
aux = ' '.join(map(str, aux))
aux = aux.replace("[", "(")
print(aux.replace("]", ")"))
