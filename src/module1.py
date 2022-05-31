"""
Version 0.1

Creator - Ankit Bansal (MS Student)
Association - IIT Madras, Chennai, India | Harish Chandra Mehta Research Insitute (Allahabad), Prayagraj, India

Supporter

Prof. Ravi Kumar NV
Laboratory of High Performance Ceramics, Department of Metallurgical and Materials Engineering, IIT Madras, Chennai, India

Dr. Sudip Chakraborty
Materials Theroy for Energy Scavenging group, Physics, Harish Chandra Mehta Research Institute (Allahabad), Prayagraj, India


Date  - 23-05-22
"""

"""  
This code will take POSCAR file as input and another file named "DOPAL" as input to create multiple POSCAR file which has varing doping and 
"""
comparison_dict = {"R":[1,1],"A":[0,0],"F"=[0,1]} #R = Random, A = All, F = First, First bit is if shuffling to be done, Second bit if next character is important or not

def main(PRINT_PATH,POSCAR_FPATH, DOPAL_FPATH):

    Shuffle, Iterations, Atomic_conf_symb, Atomic_configration = DOPAL_reader(DOPAL_FPATH)

    OUTPUT = POSCAR_Reader(POSCAR_FPATH)




############### END of MAIN #####################    


def DOPAL_reader(file_path):
    f = open(file_path,"r")
    line1 = f.readline().split()
    First_letter = line1[0][0]                              ## read first character of first word in string
    First_letter_meaning = comparison_dict[First_letter]    ## compare from dictionary to look for next steps
    next_char_read = First_letter_meaning[1]                ## is next word in first line important or not
    if next_char_read == 1:                                 ## if 1 then it is important and read letter
        structure_num = int(line1[1])
    else:
        structure_num = 1000000                             ## ELSE put a high value
    shuffle = First_letter_meaning[0]
    atoms_symbol = f.readline().split()
    atoms_num = f.readline().split()
    atoms_num = list(map(int,atoms_num))
    tmp =list(zip(atoms_symbol,atoms_num))                  ## Read the next two line and create tuple of atomic symbol and quantity

    atomic_conf_symb = f.readline().split()
    A = []
    while True:
        conf = f.readline()
        if not conf:
            break
        conf = conf.split()   
        conf = list(map(int,conf))
        A.append(conf)
    return (shuffle,structure_num,atomic_conf_symb,A)