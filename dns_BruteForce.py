import dns.resolver
import sys

res = dns.resolver.Resolver()

try:
    domain = sys.argv[1]
    try:
        file = open("subdomains-top1mil-20000.txt", "r")
        wordList = file.read().splitlines()
        for word in wordList:
            try:
                subdomain = word + "." + domain
                answer = res.resolve(subdomain, "A")
                for ip in answer:
                    print("Subdomain: {} ---> ip: {}".format(subdomain,ip))
            except: pass
    except:
        print("Word List not found...")
except:
    print("Usage:python3 dns_BruteForce.py domain")
    print("example:python3 dns_BruteForce.py google.com")
