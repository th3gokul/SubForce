# SubForce
SubForce is a Python-based tool for performing subdomain bruteforce.

## Features

- Perform DNS checks on subdomains for specified domains
- Supports single domain or multiple domains from a file
- Uses a wordlist file to generate subdomains for brute-forcing
- Displays valid and invalid domains in the console
- Saves valid domains to an output file

## Usage

1. Clone the repository:
```shell
git clone https://github.com/th3gokul/SubForce.git
```
2. Change Directory
```shell
cd SubForce
```

3. Install the required packages:
```shell
pip install -r requirements.txt
```

4. Run the tool with the desired options:
```shell
python subdomain.py  -d example.com -w wordlists/subdomains.txt -o output.txt

```
Or
```shell
python subdomain.py  -l domains.txt -w wordlists/subdomains.txt -o output.txt
```

Available options:
- `-w`, `--wordlist`: Path to the wordlist file containing subdomains to check.
- `-d`, `--domain`: Single domain to check subdomains for.
- `-l`, `--domains_list`: File containing multiple domains to check subdomains for.
- `-o`, `--output_file`: Output file to save valid domains. (optional)


5. View the results in the console and the saved valid domains in the specified output file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


