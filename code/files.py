from typing import TextIO
DUMMY_FILE1_NAME : str ="dummy/dummy_file1.csv"
#using with - automatically handles close files

try:
    with open(DUMMY_FILE1_NAME, 'r+') as df1:
        for line in df1.read().replace(' ','').split('\n')[1:]: #[1:] - skipping headline
            for col in line.split(','):
                print(col)

except FileNotFoundError:
        print(f"Error: File '{DUMMY_FILE1_NAME}' not found.")
except PermissionError:
    print(f"Error: Permission denied for file '{DUMMY_FILE1_NAME}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

DUMMY_FILE2_NAME : str ="dummy/dummy_file2.txt"


def write_logic(f : TextIO) -> None:
     f.seek(0,0)
     f.write("x")
try:
    with open(DUMMY_FILE2_NAME, "r+") as df2:
        write_logic(df2)

except FileNotFoundError:
    with open(DUMMY_FILE2_NAME, "w") as df2:
        write_logic(df2)
except PermissionError:
    print(f"Error: Permission denied for file '{DUMMY_FILE1_NAME}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")