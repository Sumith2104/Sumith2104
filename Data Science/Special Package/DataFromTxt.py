import tabulate

class Dataset:
    def __init__(self):
        self.file = file
        self.heading = heading
        self.mode = mode

    def disp_info(self, mode, heading):
        data_from_file = []
        with open(self, mode) as file:
            lines = file.readlines()
        for line in lines[1:]:
            words = line.strip().split()
            data_from_file.append(words)

        print(tabulate.tabulate(data_from_file, headers=heading, tablefmt='grid'))
        print(f"{len(data_from_file)} Dataset printed")

file = ""
heading = []
mode = 'r'

#Dataset.disp_info(#file, #mode, #heading)
