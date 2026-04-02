import numpy as np
import os
print(os.getcwd())

def main():
    base_dir = os.path.dirname(__file__)
    filename = os.path.join(base_dir, "data3.csv")
    print(read_csv_to_dict(filename))



def read_csv_to_dict(filename):
    with open(filename, "r") as f:
        # Read header
        header = f.readline().strip().split(",")

        # Initialize dictionary with empty lists
        data = {key: [] for key in header}

        # Process rows
        for line in f:
            values = line.strip().split(",")

            for key, value in zip(header, values):
                try:
                    data[key].append(int(value))
                except ValueError:
                    data[key].append(None)

        # Convert lists to numpy arrays
        for key in data:
            data[key] = np.array(data[key])

        return data
    

if __name__ == "__main__":
    main()