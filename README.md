# MRZ (Machine Readable Zone)
An MRZ is the text at the bottom of documents such as national identity cards, passports, visas, residence permits or other documents which contain a specific set of characters which allow them to be easily read by a machine.

## Content of an MRZ
Passports usually contain the following data in the MRZ
1. Document Type (Sometimes 'P' is used to identify passports)
2. Type subtype (Sometimes used to differenciate between official/service or diplomatic passports)
3. Issuing country (USA for the United States, GBR for a British Citizen, FRA for French Citizens)
4. Name (Last name followed by given name/names)
5. Passport/Document number
6. Check Digit
7. Date of birth (YYMMDD)
8. Check digit
9. Sex (M, F or <)
10. Document expiration date (YYMMDD)
11. Check digit
12. Personal identification number
13. Check digit
14. Final check digit

Travel permits such as visas often implement an MRZ and usualy replace the Document type with V or I, A, C or something similar with a subtype such as T or < or another character. For example, a tourist visa from Hungary may start with VTHUN123456<

## About this project
This project was made for educational purposes to try and generate an MRZ or to decode an MRZ using the Python programming language.
This program currently supports only TD3 type passports.
Currently, this program cannot decode or find an MRZ from an image but the feature has been planned and may be implemented in a future version.

## MRZ types

### TD1 (OFFICIAL TRAVEL DOCUMENTS/ID CARDS):
I<UTOD231458907<<<<<<<<<<<<<<< <br />
7408122F1204159UTO<<<<<<<<<<<6 <br />
ERIKSSON<<ANNA<MARIA<<<<<<<<<< <br />

### TD2 (OFFICIAL TRAVEL DOCUMENTS/ID CARDS):
I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<< <br /> 
D231458907UTO7408122F1204159<<<<<<<6 <br />

### TD3 (PASSPORTS):
P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<< <br />
L898902C<3UTO6908061F9406236ZE184226B<<<<<14 <br />

### MRV-A (VISAS):
V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<< <br />
L8988901C4XXX4009078F96121096ZE184226B<<<<<< <br />

### MRV-B (VISAS):
V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<< <br />
L8988901C4XXX4009078F9612109<<<<<<<< <br />

 <br /> <br />
Devlopment for this project started on: Oct/19/2021.
