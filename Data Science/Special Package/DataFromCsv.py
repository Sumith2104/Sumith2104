def disp_from_csv(file_name, *heading):
    data = pandas.read_csv(file_name)
    data_from_file = data.values.tolist()

    print(tabulate(data_from_file,headers = heading,tablefmt="grid"))
    print(f"{len(data_from_file)} dataset printed")
