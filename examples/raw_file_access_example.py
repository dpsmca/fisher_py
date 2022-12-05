import os
import sys
from fisher_py.data import Device, TrayShape
from fisher_py.raw_file_reader import RawFileReaderAdapter

filename = "my_file.raw"

if __name__ == "__main__":
    # Check to see if the RAW file name was supplied as an argument to the program
    args = list(sys.argv)[1:]
    argc = len(args)
    if argc > 0:
        filename = args[0]
    if filename == '':
        print('No RAW file specified!')
        sys.exit(0)

    # Check to see if the specified RAW file exists
    if not os.path.exists(filename):
        print(f"The file doesn't exist in the specified location - {filename}")
        sys.exit(0)

    # Create the RawFileAccess object for accessing the RAW file
    raw_file = RawFileReaderAdapter.file_factory(filename)

    instrument_methods_count = raw_file.instrument_methods_count
    
    raw_file.select_instrument(Device.MS, 1)
    
    print(f'User labels: {", ".join(raw_file.user_label)}')
    print(raw_file.scan_events)
    print(raw_file)
