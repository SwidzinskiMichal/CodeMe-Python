with   open("f:/Users/Admin/PycharmProjects/test.txt") as file_handler:
    with   open("f:/Users/Admin/PycharmProjects/res.txt", "w") as file_handler_2:
        result = 0
        for line in file_handler:
            clean_line = line.strip()
            num_1 = int(clean_line[2])
            num_2 = int(clean_line[4])
            arg_1 = clean_line[0]
            match arg_1:
                case "+":
                    result = num_1 + num_2
                case "-":
                    result = num_1 - num_2
                case "/":
                    result = num_1 / num_2
                case "*":
                    result = num_1 * num_2
            result_file = f"Result: {result}"
            print(result_file)
            file_handler_2.write(result_file)
            file_handler_2.write("\n")


file_handler_2.close()
file_handler.close()