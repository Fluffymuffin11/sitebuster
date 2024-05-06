#!/usr/bin/env python3
import subprocess
import re
import dns.resolver

def resolve_domain(domain):
    """Resolve domain to IP address."""
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            return rdata.address
    except Exception as e:
        print(f"Error resolving domain: {e}")
        return None

def search_exploits(target):
    """Search for exploits using searchsploit."""
    try:
        result = subprocess.run(['searchsploit', '-w', target], capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Failed to search exploits: {e}"

def main():
    target = input("Enter the IP address or domain to search for exploits: ")
    
    # Validate if input is IP or domain
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", target):
        print(f"Searching for exploits for IP: {target}")
    else:
        print(f"Resolving domain: {target}")
        ip = resolve_domain(target)
        if ip:
            print(f"Resolved IP: {ip}")
            target = ip
        else:
            print("Failed to resolve IP.")
            return
    
    exploits = search_exploits(target)
    print("Found exploits:")
    print(exploits)

if __name__ == "__main__":
    main()
