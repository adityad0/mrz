#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from string import ascii_uppercase, digits
from typing import final

# document_type = input("Type: ").upper()
# issuing_country = input("Issuing country: ").upper()
# last_name = input("Last name: ").upper().replace(" ", "<")
# given_names = input("Given names: ").upper().replace(" ", "<")
# document_number = input("Doc number: ").upper()
# nationality = input("Nationality: ").upper()
# year_of_birth = input("Year of birth: ")
# month_of_birth = input("Month of birth: ")
# date_of_birth = input("Date: ")
# gender = input("Gender: ").upper()
# exp_year = input("Exp Year: ")
# exp_month = input("Exp month: ")
# exp_date = input("exp date: ")



document_type = "p".upper()
if len(document_type) > 1:
    print("Error, invalid document type.")
if document_type != "P":
    print("Error, invalid document type.")
issuing_country = "uto".upper()
last_name = "Eriksson".upper()
last_name = last_name.replace(" ", "<")
given_names = "anna maria".upper()
given_names = given_names.replace(" ", "<")
document_number = "L898902C".upper()
nationality = "uto".upper()
year_of_birth = "69"
month_of_birth = "08"
date_of_birth = "06"
gender = "f".upper()
exp_year = "94"
exp_month = "06"
exp_date = "23"
identification_number = "ZE184226B".upper().replace(" ", "<")

countries = {'AFG': 'Afghanistan', 'ALA': 'Aland Islands', 'ALB': 'Albania', 'DZA': 'Algeria', 'ASM': 'American Samoa', 'AND': 'Andorra', 'AGO': 'Angola', 'AIA': 'Anguilla', 'ATA': 'Antarctica', 'ATG': 'Antigua And Barbuda', 'ARG': 'Argentina', 'ARM': 'Armenia', 'ABW': 'Aruba', 'AUS': 'Australia', 'AUT': 'Austria', 'AZE': 'Azerbaijan', 'BHS': 'Bahamas', 'BHR': 'Bahrain', 'BGD': 'Bangladesh', 'BRB': 'Barbados', 'BLR': 'Belarus', 'BEL': 'Belgium', 'BLZ': 'Belize', 'BEN': 'Benin', 'BMU': 'Bermuda', 'BTN': 'Bhutan', 'BOL': 'Bolivia', 'BES': 'Bonaire, Sint Eustatius And Saba', 'BIH': 'Bosnia And Herzegovina', 'BWA': 'Botswana', 'BVT': 'Bouvet Island', 'BRA': 'Brazil', 'IOT': 'British Indian Ocean Territory', 'BRN': 'Brunei', 'BGR': 'Bulgaria', 'BFA': 'Burkina Faso', 'BDI': 'Burundi', 'CPV': 'Cabo Verde', 'KHM': 'Cambodia', 'CMR': 'Cameroon', 'CAN': 'Canada', 'CYM': 'Cayman Islands', 'CAF': 'Central African Republic', 'TCD': 'Chad', 'CHL': 'Chile', 'CHN': 'China', 'CXR': 'Christmas Island', 'CCK': 'Cocos Islands', 'COL': 'Colombia', 'COM': 'Comoros', 'COG': 'Congo', 'COD': 'Democratic Republic Of The Congo', 'COK': 'Cook Islands', 'CRI': 'Costa Rica', 'CIV': 'Ivory Coast', 'HRV': 'Croatia', 'CUB': 'Cuba', 'CUW': 'Curaçao', 'CYP': 'Cyprus', 'CZE': 'Czech Republic', 'DNK': 'Denmark', 'DJI': 'Djibouti', 'DMA': 'Dominica', 'DOM': 'Dominican Republic', 'ECU': 'Ecuador', 'EGY': 'Egypt', 'SLV': 'El Salvador', 'GNQ': 'Equatorial Guinea', 'ERI': 'Eritrea', 'EST': 'Estonia', 'ETH': 'Ethiopia', 'FLK': 'Falkland Islands', 'FRO': 'Faroe Islands', 'FJI': 'Fiji', 'FIN': 'Finland', 'FRA': 'France', 'GUF': 'French Guiana', 'PYF': 'French Polynesia', 'ATF': 'French Southern Territories', 'GAB': 'Gabon', 'GMB': 'Gambia', 'GEO': 'Georgia', 'D': 'Germany', 'GHA': 'Ghana', 'GIB': 'Gibraltar', 'GRC': 'Greece', 'GRL': 'Greenland', 'GRD': 'Grenada', 'GLP': 'Guadeloupe', 'GUM': 'Guam', 'GTM': 'Guatemala', 'GGY': 'Guernsey', 'GIN': 'Guinea', 'GNB': 'Guinea Bissau', 'GUY': 'Guyana', 'HTI': 'Haiti', 'HMD': 'Heard Island And Mcdonald Islands', 'VAT': 'Vatican City State', 'HND': 'Honduras', 'HKG': 'Hong Kong', 'HUN': 'Hungary', 'ISL': 'Iceland', 'IND': 'India', 'IDN': 'Indonesia', 'IRN': 'Iran', 'IRQ': 'Iraq', 'IRL': 'Ireland', 'IMN': 'Isle Of Man', 'ISR': 'Israel', 'ITA': 'Italy', 'JAM': 'Jamaica', 'JPN': 'Japan', 'JEY': 'Jersey', 'JOR': 'Jordan', 'KAZ': 'Kazakhstan', 'KEN': 'Kenya', 'KIR': 'Kiribati', 'RKS': 'Kosovo', 'PRK': 'North Korea', 'KOR': 'South Korea', 'KWT': 'Kuwait', 'KGZ': 'Kyrgyzstan', 'LAO': 'Lao Democratic Republic', 'LVA': 'Latvia', 'LBN': 'Lebanon', 'LSO': 'Lesotho', 'LBR': 'Liberia', 'LBY': 'Libya', 'LIE': 'Liechtenstein', 'LTU': 'Lithuania', 'LUX': 'Luxembourg', 'MAC': 'Macao', 'MKD': 'Macedonia', 'MDG': 'Madagascar', 'MWI': 'Malawi', 'MYS': 'Malaysia', 'MDV': 'Maldives', 'MLI': 'Mali', 'MLT': 'Malta', 'MHL': 'Marshall Islands', 'MTQ': 'Martinique', 'MRT': 'Mauritania', 'MUS': 'Mauritius', 'MYT': 'Mayotte', 'MEX': 'Mexico', 'FSM': 'Micronesia', 'MDA': 'Moldova', 'MCO': 'Monaco', 'MNG': 'Mongolia', 'MNE': 'Montenegro', 'MSR': 'Montserrat', 'MAR': 'Morocco', 'MOZ': 'Mozambique', 'MMR': 'Myanmar', 'NAM': 'Namibia', 'NRU': 'Nauru', 'NPL': 'Nepal', 'NLD': 'Netherlands', 'ANT': 'Netherlands Antilles', 'NTZ': 'Neutral Zone', 'NCL': 'New Caledonia', 'NZL': 'New Zealand', 'NIC': 'Nicaragua', 'NER': 'Niger', 'NGA': 'Nigeria', 'NIU': 'Niue', 'NFK': 'Norfolk Island', 'MNP': 'Northern Mariana Islands', 'NOR': 'Norway', 'OMN': 'Oman', 'PAK': 'Pakistan', 'PLW': 'Palau', 'PSE': 'Palestine', 'PAN': 'Panama', 'PNG': 'Papua New Guinea', 'PRY': 'Paraguay', 'PER': 'Peru', 'PHL': 'Philippines', 'PCN': 'Pitcairn', 'POL': 'Poland', 'PRT': 'Portugal', 'PRI': 'Puerto Rico', 'QAT': 'Qatar', 'REU': 'Reunion', 'ROU': 'Romania', 'RUS': 'Russia', 'RWA': 'Rwanda', 'BLM': 'Saint Barthelemy', 'SHN': 'Saint Helena, Ascension And Tristan Da Cunha', 'KNA': 'Saint Kitts And Nevis', 'LCA': 'Saint Lucia', 'MAF': 'Saint Martin', 'SPM': 'Saint Pierre And Miquelon', 'VCT': 'Saint Vincent And The Grenadines', 'WSM': 'Samoa', 'SMR': 'San Marino', 'STP': 'Sao Tome And Principe', 'SAU': 'Saudi Arabia', 'SEN': 'Senegal', 'SRB': 'Serbia', 'SYC': 'Seychelles', 'SLE': 'Sierra Leone', 'SGP': 'Singapore', 'SXM': 'Sint Maarten', 'SVK': 'Slovakia', 'SVN': 'Slovenia', 'SLB': 'Solomon Islands', 'SOM': 'Somalia', 'ZAF': 'South Africa', 'SGS': 'South Georgia And The South Sandwich Islands', 'SSD': 'South Sudan', 'ESP': 'Spain', 'LKA': 'Sri Lanka', 'SDN': 'Sudan', 'SUR': 'Suriname', 'SJM': 'Svalbard And Jan Mayen', 'SWZ': 'Swaziland', 'SWE': 'Sweden', 'CHE': 'Switzerland', 'SYR': 'Syria', 'TWN': 'Taiwan', 'TJK': 'Tajikistan', 'TZA': 'Tanzania', 'THA': 'Thailand', 'TLS': 'East Timor', 'TGO': 'Togo', 'TKL': 'Tokelau', 'TON': 'Tonga', 'TTO': 'Trinidad And Tobago', 'TUN': 'Tunisia', 'TUR': 'Turkey', 'TKM': 'Turkmenistan', 'TCA': 'Turks And Caicos Islands', 'TUV': 'Tuvalu', 'UGA': 'Uganda', 'UKR': 'Ukraine', 'ARE': 'Arab Emirates', 'GBR': 'United Kingdom of Great Britain and Northern Ireland Citizen', 'GBD': 'British Overseas Territories Citizen', 'GBN': 'British National Overseas', 'GBO': 'British Overseas Citizen', 'GBP': 'British Protected', 'GBS': 'British Subject', 'USA': 'United States', 'UMI': 'United States Minor Outlying Islands', 'URY': 'Uruguay', 'UTO': 'Utopia (Not a real country!)', 'UZB': 'Uzbekistan', 'VUT': 'Vanuatu', 'VEN': 'Venezuela', 'VNM': 'Vietnam', 'VGB': 'Virgin Islands', 'VIR': 'Virgin Islands Of The United States', 'WLF': 'Wallis And Futuna', 'ESH': 'Western Sahara', 'YEM': 'Yemen', 'ZMB': 'Zambia', 'ZWE': 'Zimbabwe', 'EUE': 'European Union', 'UNO': 'United Nations Organization', 'UNA': 'United Nations Agency', 'UNK': 'Kosovo UN', 'WSA': 'World Service Authority', 'XBA': 'African Development Bank', 'XIM': 'Afrexim', 'XCC': 'Caricom', 'XCO': 'Comesa', 'XEC': 'Ecowas', 'INP': 'Interpol', 'XPO': 'International Criminal Police Organization', 'XOM': 'Military Order Of Malta', 'XXA': 'Refugee A', 'XXB': 'Refugee B', 'XXC': 'Refugee C', 'XXX': 'Unknown'}

if identification_number == "":
    identification_number = "<<<<<<<<<<"

dob = year_of_birth + month_of_birth + date_of_birth
exp = exp_year + exp_month + exp_date

# Validate the document number:
if len(document_number) > 9 or len(document_number) < 4:
    print("Error, invalid document number!")
    quit()

def generate_check(value: str) -> str:
    printable = digits + ascii_uppercase
    value = value.upper().replace("<", "0")
    weight = [7, 3, 1]
    summation = 0
    for i in range(len(value)):
        c = value[i]
        if c not in printable:
            raise ValueError("%s contains invalid characters" % value, c)
        summation += printable.index(c) * weight[i % 3]
    return str(summation % 10)

def encode():
    doc_no_checkDigit = generate_check(document_number)
    dob_checkDigit = generate_check(dob)
    exp_checkDigit = generate_check(exp)

    doc_num_len = len(document_number)
    mrz_f_line = document_type + "<" + issuing_country + last_name + "<<" + given_names
    f_line_len = len(mrz_f_line)

    if f_line_len < 44:
        mrz_f_line += "<" * (44 - f_line_len)

    display_doc_no = document_number
    if len(document_number) < 9:
        display_doc_no = document_number + "<" * (9 - len(document_number)) + doc_no_checkDigit
    else:
        display_doc_no = document_number + doc_no_checkDigit

    mrz_s_line = display_doc_no + nationality + dob + dob_checkDigit + gender + exp + exp_checkDigit + identification_number
    if len(mrz_s_line) < 44:
        mrz_s_line += "<" * (44 - len(mrz_s_line))

    char_43 = generate_check(identification_number)
    # if str(char_43) == "0":
    #     char_43 = "<"
    # Change the 43rd character of the second line with the check digit for the identification_number
    mrz_s_line = mrz_s_line[:-2]
    mrz_s_line += char_43 + "<"

    # Get chars 1-10, 14-20, 22-43 and find the check digit of it
    validate_for_char_44 = mrz_s_line[0:10] + mrz_s_line[13:20] + mrz_s_line[21:42]
    char_44 = generate_check(validate_for_char_44)

    # Replace the last char of line 2 with the check digit
    mrz_s_line = mrz_s_line[:-1]
    mrz_s_line += char_44

    print(mrz_f_line)
    print(mrz_s_line)

def decode(mrz_f_line, mrz_s_line):
    mrz_f_line = mrz_f_line.upper()
    mrz_s_line = mrz_s_line.upper()
    # Validate the lengths
    if len(mrz_f_line) == 44:
        valid_len = True
    else:
        print('Invalid lenght for first MRZ line')
    if len(mrz_s_line) == 44:
        valid_len = True
    else:
        print('Invalid lenght for second MRZ line')
    
    # Get data from first line:
    document_type = mrz_f_line[0]
    if document_type == "P":
        print("Document Type: Passport (P)")
    else:
        print("Document Type: Unknown")

    document_sub_type = mrz_f_line[1]
    if document_sub_type == "<":
        print("Document sub-type: None")
    else:
        print("Document sub-type: " + document_sub_type)

    issuing_country = mrz_f_line[2 : 5]
    print("Issuing country: " + issuing_country)

    last_name = mrz_f_line.split("<<")
    last_name = str(last_name[0])
    last_name = last_name[5:]
    print("Last Name: " + str(last_name))

    given_names = ""
    last_name_len = len(last_name)
    before_given_names_len = 5 + last_name_len
    after_given_names_len = 44 - before_given_names_len
    given_names = mrz_f_line[before_given_names_len + 2:].replace("<", " ")
    print("Given Names: "+ given_names)

    # Get data from second line
    document_number = mrz_s_line[:10]
    document_number_check = document_number[-1]
    document_number = document_number[:-1].replace("<", "")
    print("Document Number: " + document_number)
    # print("Document Number Checksum: " + document_number_check)
    if generate_check(document_number) == document_number_check:
        check_matched = True
    else:
        print("WARNING: DOCUMENT NUMBER CHECK DID NOT MATCH!!")

    nationality = mrz_s_line[10 : 13]
    nationality_country_name = countries[nationality]

    print("Nationality: " + nationality_country_name + " (" + nationality + ")")

    date_of_birth = mrz_s_line[13 : 19]
    date_of_birth_check = mrz_s_line[19]
    print("Date of birth: " + date_of_birth)
    # print("Date of birth Checksum: " + date_of_birth_check)

    gender = mrz_s_line[20]
    print("Gender: " + gender)

    exp_date = mrz_s_line[21 : 27]
    exp_date_check = mrz_s_line[27]
    print("Document Expiry Date: " + exp_date)
    # print("Document Expiry Date Checksum: " + exp_date_check)

    identification_number = mrz_s_line[28 : 42].replace("<", "")
    if identification_number == "":
        print("Identification Number: None")
    else:
        print("Identification Number: " + identification_number)

    identification_number_check = mrz_s_line[42]
    # print("Identification Number Checksum: " + identification_number_check)

    final_check = mrz_s_line[-1]
    # print("Final Check Digit: " + final_check)

line_1 = input("Enter MRZ line 1: ")
line_2 = input("Enter MRZ line 2: ")
print()
print("= = = = DECODED DETAILS = = = =")
# decode("P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<", "L898902C<3UTO6908061F9406236ZE184226B<<<<<14")
print()
decode(line_1, line_2)
# P<USASCHNEIDER<<WILLIAM<CHARLES<<<<<<<<<<<<<
# 0368202241USA4302089M0901141<<<<<<<<<<<<<<<6