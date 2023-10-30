krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

#alias => kredi
for kredi in krediler:
    print(kredi)

for i in range(10):
    print(i)

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3,10):
    print(i)

for i in range(0,11,2):
    print(i)

for kredi in krediler:
    print("<option>" + kredi + "<option>")