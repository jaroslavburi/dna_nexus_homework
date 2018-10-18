
import sys, getopt

class Utility:

    HELP_MESSAGE = 'dna_converter.py -p <path_to_file> -l <frag_length>'

    @staticmethod
    def get_args(argv):
        path_to_file = ''
        frag_length = ''

        try:
            opts, args = getopt.getopt(argv,"hp:l:")
        except getopt.GetoptError:
            print(Utility.HELP_MESSAGE)
            sys.exit(2)
        if(len(opts) != 2):
            print(Utility.HELP_MESSAGE)
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print(Utility.HELP_MESSAGE)
                sys.exit()
            elif opt in ("-p"): #TODO check string
                path_to_file = arg
            elif opt in ("-l"): #TODO check int
                frag_length = arg

        return path_to_file, frag_length

    def read_file(path):
        with open(path, 'r') as myfile:
            data = myfile.read()

        return data
