# country code

country_code = { "India" : "0091",
                 "Qatar" : "0974",
                 "Pakistan":"0092",
                 "USA":"001",
                 "Australia":"0061"}

print("The country code for india")
print(country_code.get("India","not found"))

print("The country code for Canada")
print(country_code.get("Canada","not found"))

print("The country code for qatar")
print(country_code.get("Qatar","not found"))

print("The country code for pakistan")
print(country_code.get("Pakistan","not found"))

print("The country code for USA")
print(country_code.get("USA","not found"))

print("The country code for australia")
print(country_code.get("Australia","not found"))