# your code goes here!
import re


class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Replace commas with spaces, split on whitespace
        raw_addresses = self.addresses.replace(',', ' ').split()

        # Regex to match valid email addresses
        email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        # Filter only valid emails
        valid_emails = [
            email for email in raw_addresses if email_regex.match(email)]

        # Use set to remove duplicates, then sort alphabetically
        unique_sorted_addresses = sorted(set(valid_emails))
        return unique_sorted_addresses
