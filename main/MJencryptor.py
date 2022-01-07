'''
Encriptador de Textos
Criado por Jonatas Miguel

Tem como função codificar arquivos de texto usando dicionarios python

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
    if flag == 'c':
        print("Caminho adicionado!")
        anim = "="
        for i in range(1,20):
            print("Criptografando {}".format(anim*i))
            time.sleep(0.1)
        
        saida = content_arq.readlines()
        for line in saida:
            saida_line = line
            for letter in saida_line:
                if letter in cript:
                    saida_line = saida_line.replace(letter,cript[letter])
            print(saida_line)
            out_file.writelines(saida_line)
        print("="*15,"Concluido!","="*15)
    elif flag == 'd':
        print("Caminho adicionado!")
        anim = "="
        for i in range(1,20):
            print("Descriptografando! {}".format(anim*i))
            time.sleep(0.1)
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
        print("="*15,"Concluido!","="*15)
    else:
        print("Insira uma flag de codificação(c) ou descodificação(d)!")

def main():
    line_command = argparse.ArgumentParser(description= "|MJcodifier| Codificador de arquivos texto")
    line_command.add_argument('-path','-p',required=True,help= "Caminho ou nome do arquivo (caso esteja no mesmo diretorio)")
    line_command.add_argument('-output','-o', help='Cria um arquivo contendo o texto criptografado!')
    line_command.add_argument('-mode','-m',help='Escolhe se vai codificar(c) ou descodificar(d)')
    args = line_command.parse_args()
    try:
        cripto(str(args.path),str(args.output),args.mode)
        
    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO\nVERIFIQUE O NOME OU O CAMINHO!")
main()
