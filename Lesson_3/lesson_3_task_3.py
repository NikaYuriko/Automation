from address import Address
from mailing import Mailing

to_address = Address("14604", "Чехов", "Чехова", "3", "15")
from_address = Address("16547", "Москва", "Ленина", "18", "23")
mailing = Mailing(to_address, from_address, 780, "MCH126")

print(f"Отправление {mailing.track} из {mailing.from_address.postcode}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.buillding}, {mailing.from_address.apartment}"
      f" в {mailing.to_address.postcode}, {mailing.to_address.city}, {mailing.to_address.street}"
      f"{mailing.to_address.buillding}, {mailing.to_address.apartment}, Цена {mailing.cost} рублей")