import whois
import re
import time


# Input text
list_of_potential_domains = """

"""

list_of_testing_names = """

"""

# Step 1: Regex to add quotes around each word, remove spaces, and add a comma at the end
result1 = re.sub(r'(?m)^\s*(\w+)\s*(\w+)', r"'\1\2',", list_of_testing_names)


# Step 2: Generate domain names by appending .com to each line
domain_names_with_dotcom = [item.strip(", '") + ".com" for item in result1.splitlines()]


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
            print(f" '{domain_name}' is already registered")
            return False
    except Exception:
        # WHOIS library raises an exception if the domain is not registered
        print(f"The domain '{domain_name}' is available!")
        return True

# keep the list to a maximum of 40 at a time
# Test the function
if __name__ == "__main__":
    for domain in domain_names_with_dotcom:
        check_domain_availability(domain)
        time.sleep(3) # Waits 3 seconds between lookups to stay within rate limit and not overwork Registrar servers
    print("Done")

