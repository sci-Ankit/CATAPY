"""
Version 0.1

Creator - Ankit Bansal (MS Student)
Association - IIT Madras, Chennai, India | Harish Chandra Mehta Research Insitute (Allahabad), Prayagraj, India

Supporter

Prof. Ravi Kumar NV
Laboratory of High Performance Ceramics, Department of Metallurgical and Materials Engineering, IIT Madras, Chennai, India

Dr. Sudip Chakraborty
Materials Theroy for Energy Scavenging group, Physics, Harish Chandra Mehta Research Institute (Allahabad), Prayagraj, India


Date  - 21-05-22
"""

"""
This code take pristine POSCAR and Specially formated Adsorbate file "ADSOR" as input. ADSOR contains all the possible adsorption site which should be tested for given pristine condition system. These lines are formated in similar way any reglar POSCAR will be formated and considering currently same coordinate system, 
later some addition to include specification with resect to 1, 2 or 3 atoms could be included in code.

"""
import os

## Test code
a = 2

PRINT_PATH = "/"
POSCAR_FPATH = "/media/sf_Machine_-_shared_folder/Catapy/examples/hepo_1/POSCAR"
ADSOR_FPATH = "/media/sf_Machine_-_shared_folder/Catapy/examples/hepo_1/ADSOR"

def tprint(tmp_name,tmp):
    return #uncomment when no need for testing
    #print(tmp_name,"  -->  ",tmp, "\n")

def main(PRINT_PATH,POSCAR_FPATH, ADSOR_FPATH):

    tprint("PRINT_PATH",PRINT_PATH)
    tprint("POSCAR_PATH",POSCAR_FPATH)
    tprint("ADSOR_PATH",ADSOR_FPATH)
    tmp = PRINT_PATH + "/test"

    seek = 2

    
    head_values = head_reader(ADSOR_FPATH,0)
    count = count_atoms(head_values)
    tprint("count_atoms",count)

    head_values_POSCAR = head_reader(POSCAR_FPATH,5)
    count_pos = count_atoms(head_values_POSCAR)
    tprint("count_atoms",count_pos)

    adsorbate_segment = file_reader_after_header(ADSOR_FPATH,seek,count)    

    poscar_with_header = poscar_header_changer(POSCAR_FPATH,head_values,head_values_POSCAR)
    tprint("PRINT_PATH",PRINT_PATH)

    i = 0 
    for ads in adsorbate_segment:
        tmp_path = PRINT_PATH + "/"+str(i)
        tprint("FILE PATH",tmp_path)
        os.mkdir(tmp_path)
        tmp_path = tmp_path + "/POSCAR"
        f = open(tmp_path,"w")
        for string in poscar_with_header:
            f.write(string)
        f.write(ads)
        f.close()
        i +=1

def head_reader(file,offset): ## this code reads the bare poscar, list of tuple with all adsorbate and there qty
    f = open(file,"r")
    for i in range (offset):
        f.readline()
    atoms_symbol = f.readline().split()
    atoms_num = f.readline().split()
    tprint("atoms_num", atoms_num)
    tprint("atoms_sym",atoms_symbol)
    atoms_num = list(map(int,atoms_num))
    tmp =list(zip(atoms_symbol,atoms_num))
    f.close()
    return (tmp)

def count_atoms(tmp):  ### given the header list, number of atoms in system is counted
    atoms = 0
    for tup in tmp:
        atoms += int(tup[1])
    return(atoms)

def poscar_header_changer(poscar,head,head_pos): ### this segment will take bare poscar and and changer header and return entire file as string
    f = open (poscar,"r")
    tmp = []
    i = 0 
    while True:
        tmp2 = f.readline()
        if not tmp2:
            break
        i +=1
        if not tmp2.split() and i > 7:
            break
        
        tmp.append(tmp2)
    head_pos.extend(head)
    tmp2 = ""
    tmp3 = ""
    for a,b in head_pos:
        tmp2 += a + "\t"
        tmp3 += str(b) + "\t"
    tmp[5]=tmp2 + "\n"
    tmp[6]=tmp3 + "\n"
    #print(tmp[-1])
    return(tmp)


def file_reader_after_header(file_name,offset,counting):
    tmp = []
    tprint("file_name",file_name)
    tprint("offset",offset)
    tprint("Count", counting)
    fil = open(file_name,"r")
    for i in range(offset):
        #print("this is i",i)
        a = fil.readline()
        #print (a)
    while True:     
        l = fil.readline()
        #print("this is l",l)
        if not l:
            break
        first_letter = l[0]
        #print(first_letter)
        if first_letter == "P" or first_letter == "p":
            tmp2 = ""
            for i in range(counting):
                tmp2 += fil.readline()
            tmp.append(tmp2)

    tprint("TMP", tmp)
    fil.close
    return (tmp)    

print("MODULE_2_COMPLETED_SUCCESSFULLY")