import dns.resolver
import dns.query
import dns.zone

def get_nameservers(domain):
    """Retrieve nameservers for the target domain."""
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        return [ns.to_text() for ns in answers]
    except dns.resolver.NoAnswer:
        print(f"[-] No nameservers found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"[-] Domain {domain} does not exist.")
    except Exception as e:
        print(f"[-] Error retrieving nameservers: {str(e)}")
    return []

def attempt_zone_transfer(domain, nameservers):
    """Attempt DNS Zone Transfer (AXFR) on each nameserver."""
    for ns in nameservers:
        print(f"[*] Trying Zone Transfer on {ns} for {domain}...")
        try:
            zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
            if zone:
                print(f"[+] Zone Transfer **SUCCESSFUL** on {ns} - Vulnerable!\n")
                for name, node in zone.nodes.items():
                    print(name.to_text(), node.to_text())
                return True
        except dns.query.TransferError:
            print(f"[-] Zone Transfer blocked on {ns} - Not vulnerable.")
        except Exception as e:
            print(f"[-] Unexpected error on {ns}: {str(e)}")
    return False

if __name__ == "__main__":
    # Define your target domains
    vulnerable_targets = ["google.com", "youtube.com", "xyseclabs.com", "tesla.com", "facebook.com"]
    
    for domain in vulnerable_targets:
        print(f"\n==== Checking {domain} ====")
        nameservers = get_nameservers(domain)
        
        if nameservers:
            success = attempt_zone_transfer(domain, nameservers)
            if not success:
                print(f"[+] {domain} appears to be secure against Zone Transfer.")