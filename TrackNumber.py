#!/usr/bin/python

import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def track_phone_number():
    phone_number = input("masukkan nomor target (Ex: +6281xxxxxxxxx): ")

    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "en")
        is_valid = phonenumbers.is_valid_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        time_zones = timezone.time_zones_for_number(parsed_number)

        print("\n--- informasi nomor yang di dapat ---")
        print(f"Location          : {location}")
        print(f"Region Code       : {region_code}")
        print(f"Operator          : {provider}")
        print(f"Valid Number      : {is_valid}")
        print(f"Formatted Number  : {formatted_number}")
        print(f"Time Zones        : {', '.join(time_zones)}")

    except phonenumbers.phonenumberutil.NumberParseException:
        print("nomor tidak diketahui. periksa dan pastikan kode negara benar")

if __name__ == "__main__":
    track_phone_number()
