
import sys, getopt

class DnaData:

    ASCII_SHIFT = 33
    data_list = []

    def __init__(self, path=""):
        if path != "":
            self.parse_file(path)

    def parse_file(self, path):
        binary_str_list = self.read_from_binary(path)
        self.binary_to_dna(binary_str_list)

    def binary_to_dna(self, binary_str_list):
        #reset the list
        self.data_list = [] 

        for dna in binary_str_list:
            new_dna_dict = {
                "type": self.get_dna_type(dna[:2]),
                "confidence": self.get_dna_confidence(dna[2:])
            }
            self.data_list.append(new_dna_dict)

    #For possibility to test I added printOuptut which in case of False returns final string
    def print_FASTQ(self, frag_length, printOutput=True):
        d = iter(self.data_list)
        l = int(frag_length)

        read_num = 1
        printing = True
        result_output = ""
        while printing:

            dna_sequence = ""
            quality = ""
            i = 0
            while i < l:
                next_dna = next(d, None)

                if next_dna is None: #end
                    printing = False
                    break

                dna_sequence += next_dna["type"]
                quality+= chr(next_dna["confidence"] + self.ASCII_SHIFT)

                i+=1
            
            if printing:
                result_output += self.output_print(read_num, dna_sequence, quality)
                read_num += 1
        
        if printOutput:
            print(result_output, end='')
        else:
            return result_output

    def output_print(self, num, dna_sequence, quality):
        result = ""
        result += f"@READ_{num}\n"
        result += dna_sequence
        result += f"\n+READ_{num}\n"
        result += quality
        result += "\n"
        return result
            
    def get_dna_type(self, data):
        if data == "00":
            return "A"
        elif data == "01":
            return "C"
        elif data == "10":
            return "G"
        elif data == "11":
            return "T"

    #Converts 6bit binary to int
    def get_dna_confidence(self, data):
        return int(data, 2)

    #Reads binary file, returns list of 8 digit binary strings
    def read_from_binary(self, path):
        
        binary_str_list = []

        #TODO check if file exists
        with open(path, "rb") as f:
            
            byte = f.read(1)
            while byte != b"":
                for b in byte:
                    binary_str_list.append(self.get_bin(b,8))
                byte = f.read(1)
            
        return binary_str_list

    #Converts input byte to 8 digit binary string
    def get_bin(self, x, n):
        return format(x, 'b').zfill(n)