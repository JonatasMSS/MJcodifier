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
import time

def cripto(arquivo = None,output = None):
    cript = {"a":"zx2","e":"cvl","i":"2=z","o":"=A|","u":"0+i"," ":"=+"}
    content_arq = open(arquivo,'r')
    out_file = open(output,'w+')
    saida = content_arq.readlines()
    for line in saida:
        saida_line = line
        for letter in saida_line:
            if letter in cript:
                saida_line = saida_line.replace(letter,cript[letter])
        print(saida_line)
        out_file.writelines(saida_line)


def main():
    line_command = argparse.ArgumentParser(description= "|MJencryptor|\nEncriptador de arquivos texto")
    line_command.add_argument('-path','-p',required=True,help= "Caminho ou nome do arquivo (caso esteja no mesmo diretorio)")
    line_command.add_argument('-output','-o', help='Cria um arquivo contendo o texto criptografado!')
    args = line_command.parse_args()
    try:
        cripto(str(args.path),str(args.output))
        print("Caminho adicionado!")
        anim = "="
        for i in range(1,20):
            print("Criptografando {}".format(anim*i))
            time.sleep(0.1)
        print("="*15,"Concluido!","="*15)
    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO\nVERIFIQUE O NOME OU O CAMINHO!")
main()