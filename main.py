import whois
import re
import time


# Input text
list_of_names = """
"""

# Regex to remove spaces, input quotation marks around and finish the word of with a comma for
# every string in the array
result1 = re.sub(r'(?m)^(\w+)\s+(\w+)', r"'\1\2',", list_of_names)

# Regex with prefix(here "AI", to remove space between two words, input quotation marks around and finish the word of with a comma for
# on everything coming after the prefix "AI"
result2 = re.sub(r'(?m)^AI\s+(\w+)(\w*)', r"'AI\1\2',", list_of_names)

#print(result1)


# Generate domain names from the formatted result adding the .com suffix
domain_names_with_dotcom = [item.strip("' ,") + ".com" for item in result1.splitlines()]

# Print the formatted result
print(domain_names_with_dotcom)

def check_domain_availability(domain_name):
    """
    Check if a domain name is available.

    :param domain_name: The domain name to check (e.g., example.com).
    :return: True if available, False if registered.
    """
    try:
        # Perform a WHOIS lookup
        domain_info = whois.whois(domain_name)
        # If the WHOIS response contains information, it's registered
        if domain_info.status is not None:
            print(f" '{domain_name}'is already registered")
            return False
    except Exception:
        # WHOIS library raises an exception if the domain is not registered
        print(f"The domain '{domain_name}' is available!")
        return True

# keep the list to a maximum of 75 at a time
# Test the function
if __name__ == "__main__":
    for domain in domain_names_with_dotcom:
        check_domain_availability(domain)
        time.sleep(3) # Waits 3 seconds between lookups to stay within rate limit and not overwork Registrar servers
    print("done")

