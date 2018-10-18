#!/usr/bin/python
from utility.Utility import *
from utility.DnaData import *

def main(argv):
    path_to_file, frag_length = Utility.get_args(argv)

    print('Path to file: ', path_to_file)
    print('Frag length: ', frag_length)
    print('Output path: ', output_path)
    
    dnaParser = DnaData(path_to_file)
    dnaParser.print_FASTQ(frag_length)

if __name__ == "__main__":
    main(sys.argv[1:])
