'''
Encriptador de Textos
Criado por Jonatas Miguel


'''


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Importação de bibliotecas

import os
import sys
import argparse
from typing import get_args

def main():
    line_command = argparse.ArgumentParser(description= "|MJencryptor|\nEncriptador de arquivos texto")
    line_command.add_argument('-path','-p',required=True,help= "Caminho ou nome do arquivo (caso esteja no mesmo diretorio)")
    args = line_command.parse_args()
    path_r = open(args.path,'r')
    print("Caminho do arquivo:{}".format(path_r))

main()
