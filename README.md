# SubForce

Subforce is a subdomain bruteforcing tool written in Python. It helps you discover valid subdomains for a given domain by leveraging a wordlist-based approach and DNS queries.

## Features

- Perform DNS checks on subdomains for specified domains
- Supports single domain or multiple domains from a file
- Uses a wordlist file to generate subdomains for brute-forcing
- Displays the valid subdomains found during the scan.
- Provides an option to show invalid subdomains.
- Saves valid domains to an output file

## Installation

1. Clone the repository
```shell
git clone https://github.com/th3gokul/SubForce.git
```
2. Navigate to the SubForce directory
```shell
cd SubForce
```
3. Install the required dependencies by running the following command:
```shell
pip install -r requirements.txt
```

## Usage

```shell
python SubForce.py -l <domains_list_file> -w <wordlist_file> [-o <output_file>] [-i]
python SubForce.py -d <example.com> -w <wordlist_file> [-o <output_file>]
```
1. Perform subdomain brute-forcing for a single domain:
```shell
python SubForce.py  -d example.com -w wordlists/subdomains.txt -o output.txt

```
2. Perform subdomain brute-forcing using a domains list file:
```shell
python SubForce.py  -l domains.txt -w wordlists/subdomains.txt -o output.txt
```
3. To perform subdomain brute-forcing using a domains list file/Single Domain, specify a wordlist, save the results to a file, and display invalid domains while running, you can use the following command:
```shell
python SubForce.py -l domains.txt -w wordlist.txt -o results.txt -i
```

Available options:
- `-l, --domains_list`: Specify the file containing multiple domain inputs.
- `-d, --domain`: Specify the single domain to check subdomains for.
- `-w, --wordlist`: Specify the path to the subdomains wordlist file.
- `-o, --output_file`: Specify the output file to save valid domains (default: subforce_results.txt).
- `-i, --show_invalid`: Show invalid domains while running.



3. View the results in the console and the saved valid domains in the specified output file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


