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

def cripto(arquivo = None,output = None, flag = None):
    cript = {"a":"zx2","e":"cvl","i":"2=z","o":"=A|","u":"0+i"," ":"=+="}
    descript = {"zx2":"a","cvl":"e","2=z":"i","=A|":"o","0+i":"u","=+=":" "}
    content_arq = open(arquivo,'r')
    out_file = open(output,'w+')
    if flag == '-c':
        saida = content_arq.readlines()
        for line in saida:
            saida_line = line
            for letter in saida_line:
                if letter in cript:
                    saida_line = saida_line.replace(letter,cript[letter])
            print(saida_line)
            out_file.writelines(saida_line)
    elif flag == '-d':
        saida = content_arq.readlines()
        for line in saida:
            saida_line = line
            for key in descript:
                if key in saida_line:
                    pos = saida_line.find(key)
                    value_key = saida_line[pos:pos+3]
                    saida_line = line.replace(value_key,descript[value_key])
                    line = saida_line
            out_file.writelines(saida_line)
    else:
        print("Insira uma flag de codificação(-c) ou descodificação(-d)!")

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
cripto('saida.txt','descriptografado.txt','-d')
'''
descript = {"zx2":"a","cvl":"e","2=z":"i","=A|":"o","0+i":"u","=+":" "}
string = "zx2lcvlxzx2ndr=A|"
saida = ''

for key in descript:
    if key in string:
        pos = string.find(key)
        new_value = string[pos:pos+3]
        saida = string.replace(new_value, descript[new_value])
        string = saida
print(saida)
'''