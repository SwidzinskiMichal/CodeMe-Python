import sys


class Database:
    def __init__(self):
        self.__people_list = []
        self.open_list = []
        self.temp_open_list = []

    def list_append(self):
        temp_person = []
        temp_person.append(input("Podaj imię: "))
        temp_person.append(input("Podaj nazwisko: "))
        temp_person.append(input("Podaj zawód: "))
        error_check = input("Podaj wiek: ")
        temp_person.append(error_check)
        try:
            error_check_int = int(error_check)

        except Exception:
            print("Wpisany wiek nie jest liczbą")
            sys.exit(1)

        self.__people_list.append(temp_person)

    def __str__(self):
        a = ""
        for i in self.__people_list:
            a += f"Dane: Imię: {i[0]} | Nazwisko: {i[1]} | Zawód: {i[2]} | Wiek: {i[3]}\n"
        return a

    def search_job(self):
        temp_job = input("Podaj zawdów: ")
        for i in self.__people_list:
            if temp_job in i:
                print(i)

    def search_age(self):
        temp_age = input("Podaj wiek: ")
        for i in self.__people_list:
            if temp_age in i:
                print(i)

    def open_data(self):
        with   open("f:/Users/Admin/PycharmProjects/database.txt", "r") as file_handler:
            self.open_list = file_handler.read().splitlines()
            for i in range(int(len(self.open_list) // 4)):
                for j in range(4):
                    self.temp_open_list.append(self.open_list[j])
                self.__people_list.append(self.temp_open_list)
                self.temp_open_list = []
                for j in range(4):
                    self.open_list.remove(self.open_list[0])

        file_handler.close()

    def save(self):
        with   open("f:/Users/Admin/PycharmProjects/database.txt", "w") as file_handler_2:
            for i in self.__people_list:
                for j in i:
                    file_handler_2.write(j)
                    file_handler_2.write("\n")
        file_handler_2.close()


database = Database()
database.open_data()
database.list_append()
print(database.__str__())
