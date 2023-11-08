#!/bin/bash

if [-f "POSCAR_org"];then  
cp POSCAR_og POSCAR
else 
cp POSCAR POSCAR_org
fi

echo -e "400 \n 3 0 0 \n 0 3 0 \n 0 0 1"| vaspkit

cp SUPERCELL.vasp POSCAR

S_pos=$(head -14 POSCAR | tail -1 | awk '{print $1,$2,$3}')
F_pos=$(head -19 POSCAR | tail -1 | awk '{print $1,$2,$3}')

python generator.py $S_pos 1.0 $F_pos -1.0
