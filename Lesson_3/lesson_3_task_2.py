from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "Iphone", "89578648394")
phone2 = Smartphone("Samsung", "S21", "89156473928")
phone3 = Smartphone("Vivo", "X100s pro", "891048934455")
phone4 = Smartphone("Poco", "F6", "89256378456")
phone5 = Smartphone("Xiaomi", "14", "89034758695")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand}, {phone.model}, {phone.number}")