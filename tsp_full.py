'''
Travel Cost Matrix:

     1    2    3    4

1    0   10   15   20

2   10    0   35   25

3   15   35    0   30

4   20   25   30    0

'''


class Traveling_Merchant:
    def __init__(self, number_string):
        self.number_string = number_string
        self.f_result = []
        self.temp_list_paths = []
        self.list_paths = []
        self.temp_list = []
        self.x = 0
        self.y = 0
        self.matrix = []

    def fill_matrix(self):
        file_handler = open("tsp_matrix", "r")
        self.matrix = []
        for line in file_handler:
            clean_line = line.strip()
            clean_line_list = clean_line.split()
            self.matrix.append(clean_line_list)
        print(self.matrix)
        file_handler.close()

    def repeats(self, elements):
        s = set(elements)
        lenght = len(elements) == len(s)
        return lenght

    def get_permutation(self, number_string):
        if len(number_string) == 1:
            return [number_string]

        permutation_rec = self.get_permutation(number_string[1:])
        number = number_string[0]
        result = []

        for i in permutation_rec:
            for j in range(len(i) + 1):
                result.append(i[:j] + number + i[j:])
                global f_result
                f_result = result
        return result

    def modify(self, result):
        temporary_list = []
        for i in result:
            for j in i:
                temporary_list.append(int(j))
            self.temp_list_paths.append(temporary_list)
            temporary_list = []
        return self.temp_list_paths

    def clean_paths(self):
        for m in self.temp_list_paths:
            if self.repeats(m) == True and m[0] == 1:
                self.list_paths.append(m)

    def fill_last_point(self):
        for n in self.list_paths:
            n = list(n)
            n.append(1)
            self.temp_list.append(n)

    def reverse_clean_paths(self):
        for o in range(int(len(self.temp_list) / 2)):
            reversed_temp_element = self.temp_list[0][::-1]
            for p in self.temp_list:
                if reversed_temp_element == p:
                    self.temp_list.remove(self.temp_list[0])

    def combinations_run(self):
        self.get_permutation(self.number_string)
        self.modify(f_result)
        self.clean_paths()
        self.fill_last_point()
        self.reverse_clean_paths()

    def path_cost(self):
        for nodes in self.temp_list:
            total_cost = 0
            for j in range(len(nodes) - 1):
                for path in self.matrix:
                    if int(path[0]) == nodes[j] and int(path[1]) == nodes[j + 1]:
                        total_cost += int(path[2])
            print("Total cost of path", nodes, "=", total_cost)

    def program_run(self):
        self.fill_matrix()
        self.combinations_run()
        self.path_cost()


run = Traveling_Merchant("1234")
run.program_run()
