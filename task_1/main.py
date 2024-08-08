from collections import UserDict


# Field: Базовий клас для полів запису.
class Field:
    def __init__(self, value): 
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


# Name: Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    def __init__(self, name):
        self.value = name
        

# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
class Phone(Field):
    def __init__(self, number):
        self.value = self.validate_number(number)

    def validate_number(self, number):

        if len(number) != 10:
            raise ValueError("The phone number must have 10 digits!")
        
        if not number.isdigit():
            raise ValueError("The phone number must contain only numbers!")
        
        return number
            
 
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name): # ініціалізація за допомогою імені та порожнього списку
        self.name = Name(name)
        self.phones = []

    def __str__(self) -> str: # повертає рядкове представлення Record
        return f"Contact name: {self.name.value}, phones: {";".join(p.value for p in self.phones)}"

    def add_phone(self, number: str): # Додавання номеру телефона до запису Record
        self.phones.append(Phone(number))
    
    def remove_phone(self, number): # Видалення номера телефона з запису.
        self.phone = number
        self.phones = list(filter(lambda phone: phone == number, self.phone))

    def edit_phone(self, old_number, new_number): # Редагування номеру телефона.
        self.old_number = old_number
        self.new_number = new_number
        self.phones = list(map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones))
    
    def find_phone(self, number): # Пошук телефону.
        for phone in self.phones:
            if phone.value == number:
                return phone
      

# AddressBook: Клас для зберігання та управління записами.
class AddressBook(UserDict):
    
    def add_record(self, record): # Додавання записів
        if record.name.value in self.data:
            raise KeyError(f"Record with name {record.name.value}, already exists!")
        self.data[record.name.value] = record

    def find(self, name): # Пошук записів за іменем.
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name {name} not found!")
        return record

    def delete(self, name): # Видалення записів за іменем.
        if name not in self.data:
            raise KeyError(f"Record with name {name} not found!")
        del self.data[name]



    # Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")

for name, record in book.data.items():
    print(record)



