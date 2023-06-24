from math import sqrt, floor
import os
import smtplib
import subprocess
import requests
from bs4 import BeautifulSoup
from ip2geotools.databases.noncommercial import DbIpCity
import json
from scapy.all import ARP, Ether, srp


class Tools():
   def get_domain_information(self, domain):
      url = f"https://who.is/whois/{domain}"
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')

      domain_info = soup.find_all(
          "div", class_="col-md-12 queryResponseBodyValue")[1]
      if domain_info:
         return domain_info.get_text()
      else:
         return "N/A"

   def get_ipv4_geolocation(self, ipv4):
      response = DbIpCity.get(ipv4, api_key='free')
      return response

   def get_ipv6_geolocation(self, ipv6):
      response = DbIpCity.get(ipv6, api_key='free')
      return response

   def get_client_ip(self):
      response = (requests.get("https://api.ipify.org/?format=json")).text
      response = json.loads(response)
      return response

   def get_cep(self, cep):
      response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
      return json.loads(response.text)

   def send_emails(self, from_email, from_password, message, target, repeat_number):
      for n in range(int(repeat_number)):
         with smtplib.SMTP('smtp.gmail.com', 587) as server:
               server.starttls()
               server.login(from_email, from_password)
               server.sendmail(from_email, target, message)
               print(f"Sent message number {n + 1}")
   
   def update_packages(self):
      subprocess.call(['pip', 'freeze', '>', 'requirements.txt'])
   
   def generate_dockerfile(self, image, version, run, path, port, build = ""):
      dockerfile_content = f"FROM {image}:{version}\nRUN {build}\nCMD {run}"
      with open(os.path.join(path, 'Dockerfile'), 'w') as dockerfile:
         dockerfile.write(dockerfile_content)

      docker_compose_content = f"version: '3'\nservices:\n  app:\n    build: .\n    ports:\n      - {port}:{port}"
      with open(os.path.join(path, 'docker-compose.yaml'), 'w') as docker_compose:
         docker_compose.write(docker_compose_content)

   def bhaskara_resolver(self, a, b, c):
      a = int(a)
      b = int(b)
      c = int(c)
      delta = b ** 2 - 4 * a * c
      if delta < 0: delta = delta * -1
      negative_b = b
      if b > 0:
         negative_b = b - (b * 2)

      variation_1 = (negative_b + (floor(sqrt(delta)))) / (2 * a)
      variation_2 = (negative_b - (floor(sqrt(delta)))) / (2 * a)

      result = f"{variation_1}; {variation_2}"
      if variation_1 > variation_2: result = f"{variation_2}; {variation_1}"
      return variation_1, variation_2, result

   def site_status(self, url):
      response = requests.get(url)
      response.raise_for_status()

      print("Site URL:", response.url)
      print("Status code:", response.status_code)
      print("Response headers:")
      for header, value in response.headers.items():
         print(f"{header}: {value}")

   def about_me(self):
      return "Eai, galera! Como não podemos nos conhecer pessoalmente, aqui vai um pouco sobre mim... Mexo com tecnologia há 2 anos, já desenvolvi muitas coisas entre muitas plataformas, um ambiente mais louco que o outro! Já desenvolvi desbloqueios para consoles, fiz aplicações desktop e webapps, quebrei a cabeça organizando um servidor Linux inteiro! Mas meu foco principal é desenvolvimento Full-Stack com PHP, ASP.NET Core MVC e Banco de Dados, Aplicações no Console e Desktop com .NET Framework/Core, e em muitos casos Aplicações Mobile."

   def network_scanner(self, ip):
      arp = ARP(pdst=ip)
      ether = Ether(dst="ff:ff:ff:ff:ff:ff")

      packet = ether/arp

      result = srp(packet, timeout=3)[0]

      clients = []

      for sent, received in result:
         clients.append({'ip': received.psrc, 'mac': received.hwsrc})
      
      print("Available devices in the network:")
      print("IP" + " "*18+"MAC")
      for client in clients:
         print("{:16}    {}".format(client['ip'], client['mac']))

