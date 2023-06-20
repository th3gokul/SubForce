#Gokul
import argparse
import socket
import dns.resolver
import concurrent.futures
from colorama import init, Fore, Style

init()


def check_subdomain(subdomain, domain):
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        return None
    
    def query_dns():
        try:
            answers = dns.resolver.query(subdomain + '.' + domain, 'A')
            if len(answers) > 0:
                return f"{subdomain}.{domain}"
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.Timeout:
            pass
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(query_dns)
        try:
            result = future.result(timeout=5)  
            return result
        except concurrent.futures.TimeoutError:
            return None

parser = argparse.ArgumentParser(description='Subdomain Bruteforce.')
parser.add_argument('-l', '--domains_list', help='The file containing multiple domain inputs.')
parser.add_argument('-d', '--domain', help='The single domain to check subdomains for.')
parser.add_argument('-w', '--wordlist', required=True, help='The path to the subdomains wordlist file.')
parser.add_argument('-o', '--output_file', help='The output file to save valid domains.')
parser.add_argument('-i', '--show_invalid', action='store_true', help='Show invalid domains while running.')

args = parser.parse_args()

if args.domains_list and args.domain:
    parser.error('Please provide either a domains list file or a single domain.')
elif not args.domains_list and not args.domain:
    parser.error('Please provide either a domains list file or a single domain.')
elif args.domains_list:
    domains_list_file = args.domains_list
    with open(domains_list_file, 'r') as file:
        domains = file.read().splitlines()
else:
    domains = [args.domain]

wordlist_file = args.wordlist
with open(wordlist_file, 'r') as file:
    subdomains = file.read().splitlines()

red_color = Fore.RED
cyan_color = Fore.CYAN
yellow_color = Fore.LIGHTYELLOW_EX
white_color = Fore.WHITE

banner = r'''
███████╗██╗   ██╗██████╗ ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
███████╗██║   ██║██████╔╝█████╗  ██║   ██║██████╔╝██║     █████╗  
╚════██║██║   ██║██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
███████║╚██████╔╝██████╔╝██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                        Name        : Gokul
                                        Username    : Th3Gokul
                                        Tool        : SubForce
                                        Description : Subdomain Bruteforce
'''

valid_domains = []
invalid_domains = []

print(f"{red_color}{banner}{Style.RESET_ALL}")
print(f"{yellow_color}[+] Subforce is running...{Style.RESET_ALL}")

try:
    for domain in domains:
        for subdomain in subdomains:
            result = check_subdomain(subdomain, domain)
            if result:
                print(f"{cyan_color}[+] Valid domain: {Style.RESET_ALL}{result}")
                valid_domains.append(result)
            elif args.show_invalid:
                print(f"{red_color}[-] Invalid domain: {Style.RESET_ALL}{subdomain}.{domain}")
                invalid_domains.append(f"{subdomain}.{domain}")
except KeyboardInterrupt:
    print(f"\n{red_color}[-] Script terminated by user.{Style.RESET_ALL}")

filename = args.output_file if args.output_file else 'subforce_results.txt'
with open(filename, 'w') as file:
    for domain in valid_domains:
        file.write(domain + '\n')

if valid_domains:
    print(f"\n{yellow_color}[+] Valid domains saved to {Style.RESET_ALL}{white_color}'{filename}'{Style.RESET_ALL}")
    print(f"{yellow_color}[+] Number of valid domains found: {len(valid_domains)}{Style.RESET_ALL}")
else:
    with open(filename, 'w') as file:
        file.write("No valid domains found.\n")
    print(f"\n{red_color}[-] No valid domains found. Message saved to {Style.RESET_ALL}{white_color}'{filename}'{Style.RESET_ALL}")
