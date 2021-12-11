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

def cripto(arquivo = None,output = None):
    cript = {"a":"zx2","e":"cvl","i":"2=z","o":"=A|","u":"0+i"," ":"=+"}
    content_arq = open(arquivo,'r')
    out_file = open(output,'w+')
    saida = content_arq.readlines()
    i = 0
    for line in saida:
        saida_line = line
        for letter in saida_line:
            if letter in cript:
                saida_line = saida_line.replace(letter,cript[letter])
        print(saida_line)
        out_file.writelines(saida_line)
    
    '''
    for l in nome:
        if l in cript:
            n_pos = saida.find(l)
            saida = saida.replace(l,cript[l])
            
        else:
            pass
    print(saida)
    '''
def main():
    line_command = argparse.ArgumentParser(description= "|MJencryptor|\nEncriptador de arquivos texto")
    line_command.add_argument('-path','-p',required=True,help= "Caminho ou nome do arquivo (caso esteja no mesmo diretorio)")
    args = line_command.parse_args()
    try:
        path_r = open(args.path,'r')
        print("Caminho do arquivo:{}".format(path_r))
    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO\nVERIFIQUE O NOME OU O CAMINHO!")

cripto('arquivo_teste.txt','said.txt')