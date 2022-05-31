
"""
Calling various module at different times, this will be developed as other modules are developed
"""

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

import module2
import os

### Test code
a = 0


## This code will be changed to include the path of working directory
#MAIN_PATH = os.getcwd() 

MAIN_PATH = "/media/sf_Machine_-_shared_folder/Catapy/examples/hepo_1"

#########


############
a_POSCAR_FPATH = "/media/sf_Machine_-_shared_folder/Catapy/examples/hepo_1/POSCAR"
a_ADSOR_FPATH = "/media/sf_Machine_-_shared_folder/Catapy/examples/hepo_1/ADSOR"

tmp = MAIN_PATH + "/Generated_files"

os.mkdir(tmp)

a_PRINT_PATH = tmp

module2.main(a_PRINT_PATH,a_POSCAR_FPATH, a_ADSOR_FPATH)
###############
