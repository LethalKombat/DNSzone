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
        print(f"\n[*] Trying Zone Transfer on {ns} for {domain}...")
        try:
            zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
            if zone:
                print(f"\n[🚨] {domain} is **Vulnerable**! Zone Transfer **SUCCESSFUL** on {ns} 🚨")
                return True
        except dns.query.TransferError:
            print(f"[✔️] {domain} is **Not Vulnerable**. Zone Transfer blocked on {ns}.")
        except Exception as e:
            print(f"[-] Unexpected error on {ns}: {str(e)}")
    return False

if __name__ == "__main__":
    # 🚀 Ask the user for a domain input
    domain = input("Enter the domain to check for DNS Zone Transfer vulnerability: ").strip()

    print(f"\n==== Checking {domain} ====")
    nameservers = get_nameservers(domain)

    if nameservers:
        is_vulnerable = attempt_zone_transfer(domain, nameservers)

        if not is_vulnerable:
            print(f"\n✅ {domain} appears to be secure against Zone Transfer.")
