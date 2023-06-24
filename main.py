from art import text2art
from colorama import Fore
import os
import tools

configFile = "./impulse.txt"
def configuration_file_exists():
    if os.path.exists(configFile):
        return True
    else:
        return False
    
def create_configuration_file(platform):
    with open(configFile, 'w') as file:
        file.write(platform) 

def get_platform():
    with open(configFile, 'r') as file:
        lines = file.readlines()
        return lines[0]

def open_platform_selection_screen(): 
    if not configuration_file_exists():
        print(Fore.BLUE + "1. Windows")
        print(Fore.BLUE + "2. Linux")
        print(Fore.BLUE + "3. Mac OS")
        platform = int(input(Fore.BLUE + "Please, enter your platform -> "))
        if platform == 1: platform = "windows"
        if platform == 2: platform = "linux"
        if platform == 3: platform = "macos"
        create_configuration_file(platform)
    else: 
        platform = get_platform()

def title(): 
    print(Fore.BLUE + text2art("impulse"))
    print("                         developed by mx")

def clear_terminal():
    if get_platform() == "windows": 
        os.system("cls") 
    else: 
        os.system("clear")
    title()

def dashboard():
    clear_terminal()
    print(Fore.GREEN)
    print("1. Who is domain -> Domain search")
    print("2. IPv4 tracer -> IPv4 Geolocation")
    print("3. IPv6 tracer -> IPv6 Geolocation")
    print("4. What's my IP? -> Get your IP")
    print("5. Search CEP -> Get informations from a CEP")
    print("6. E-mail spam -> Send e-mails for a target")
    print("7. Docker generate -> Generate Dockefile")
    print("8. Bhaskara resolver -> Resolves a bhaskara question")
    print("9. Network scanner -> Scan an IP")
    print("10. Site status -> Get results for a site request")
    print("11. Update Impulse dependencies")
    print("12. About me")
    print("13. Exit")
    print()
    return int(input(Fore.RED + "What I can do for you  --> "))

def get_choise(choise):
    tools_class = tools.Tools()
    clear_terminal()
    print()
    print(Fore.RED)

    match choise:
        case 1:
            domain = input(Fore.CYAN + "What is the domain? -> ")
            result = tools_class.get_domain_information(domain)
            lines = result.splitlines()
            filtered_lines = [line for line in lines if not line.startswith("%")]
            capitalized_lines = [line.capitalize() for line in filtered_lines]
            print(Fore.GREEN + "\n".join(capitalized_lines))
        case 2:
            ipv4 = input("What is the IPv4? -> ")
            result = tools_class.get_ipv4_geolocation(ipv4)
            print(Fore.GREEN)
            print(f"IP Address: {result.ip_address}")
            print(f"City: {result.city}")
            print(f"Region/State: {result.region}")
            print(f"Country: {result.country}")
            print(f"Latitude: {result.latitude}")
            print(f"Longitude: {result.longitude}")
            print(f"Coordinates: {result.latitude}, {result.longitude}")
        case 3:
            ipv6 = input("What is the IPv6? -> ")
            result = tools_class.get_ipv6_geolocation(ipv6)
            print(Fore.GREEN)
            print(f"IP Address: {result.ip_address}")
            print(f"City: {result.city}")
            print(f"Region/State: {result.region}")
            print(f"Country: {result.country}")
            print(f"Latitude: {result.latitude}")
            print(f"Longitude: {result.longitude}")
            print(f"Coordinates: {result.latitude}, {result.longitude}")
        case 4:
            result = tools_class.get_client_ip()
            print(Fore.GREEN + f"Your IPv4 is {result['ip']}")
        case 5:
            cep = input("What is the CEP (xxxxx-xxx) ? -> ")
            result = tools_class.get_cep(cep)
            print(Fore.GREEN)
            print(f"CEP: {result['cep']}")
            print(f"Street: {result['logradouro']}")
            print(f"Extra: {result['complemento']}")
            print(f"Neighborhood: {result['bairro']}")
            print(f"Locality/City: {result['localidade']}")
            print(f"Country: Brasil")
            print(f"UF: {result['uf']}")
            print(f"DDD: {result['ddd']}")
        case 6:
            from_email = input("What's your gmail's email? -> ")
            from_password = input("What's your gmail's password? -> ")
            message = input("What's the message (email's body)? -> ")
            target = input("What's the email target? -> ")
            repeat_number = input("And how many times will the email be sent? -> ")
            print(Fore.GREEN)
            tools_class.send_emails(from_email, from_password, message, target, repeat_number)
            
        case 7:
            image = input("What's the docker image? -> ")
            version = input("What's the docker image version? -> ")
            run_command = input("What's the run command? -> ")
            build_command = input("What's the build command (optional)? -> ")
            path = input("What's the generatio's path? -> ")
            port = input("What's the application ports? -> ")
            tools_class.generate_dockerfile(image, version, run_command, path, port, build_command)
            print(Fore.GREEN)
            print("Dockerfile and docker-compose.yaml generated")
        case 8:
            print(Fore.CYAN + "Please, enter the variables:")
            print(Fore.RED)
            a = input("a -> ")
            b= input("b -> ")
            c = input("c -> ")
            x1, x2, solution = tools_class.bhaskara_resolver(a, b, c)
            print(Fore.GREEN)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print("S = { " + solution + " }")
        case 9:
            ip = input("What's the IP and port (127.0.0.1/24, for example)? -> ")
            print(Fore.GREEN)
            tools_class.network_scanner(ip)
        case 10:
            domain = input("What's domain? -> ")
            print(Fore.GREEN)
            tools_class.site_status(domain)
        case 11:
            tools_class.update_packages()
        case 12:
            print(Fore.GREEN + tools_class.about_me())
        case 13:
            exit()

open_platform_selection_screen()
option = dashboard()
print("Ok! I will do my best.")
get_choise(option)