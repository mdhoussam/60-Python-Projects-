
import phonenumbers
from phonenumbers import geocoder

first_num = phonenumbers.parse("Enter the phone number")
print(geocoder.description_for_number(first_num, "en"))