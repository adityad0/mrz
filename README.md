# mrz
Encode and Decode machine readable zones on passports, visas and other documents.
Currently supporting only TD3 type passports

Written in Python, this project will be able to read the MRZ from an image or decode the MRZ from text and return all the data in an MRZ.

# Supported MRZ types:

## TD1 (OFFICIAL TRAVEL DOCUMENTS/ID CARDS):
I<UTOD231458907<<<<<<<<<<<<<<< <br />
7408122F1204159UTO<<<<<<<<<<<6 <br />
ERIKSSON<<ANNA<MARIA<<<<<<<<<< <br />

## TD2 (OFFICIAL TRAVEL DOCUMENTS/ID CARDS):
I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<< <br /> 
D231458907UTO7408122F1204159<<<<<<<6 <br />

## TD3 (PASSPORTS):
P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<< <br />
L898902C<3UTO6908061F9406236ZE184226B<<<<<14 <br />

## MRV-A (VISAS):
V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<< <br />
L8988901C4XXX4009078F96121096ZE184226B<<<<<< <br />

## MRV-B (VISAS):
V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<< <br />
L8988901C4XXX4009078F9612109<<<<<<<< <br />
 <br /> <br />
Devlopment for this project started on: Oct/19/2021.
