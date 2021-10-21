# mrz
Encode and Decode machine readable zones on passports, visas and other documents.

Written in Python, this project will be able to read the MRZ from an image or decode the MRZ from text and return all the data in an MRZ.

# Supported MRZ types:

## TD1 (OFFICIAL TRAVEL DOCUMENTS/ID CARDS):
I<UTOD231458907<<<<<<<<<<<<<<<
7408122F1204159UTO<<<<<<<<<<<6
ERIKSSON<<ANNA<MARIA<<<<<<<<<<

## TD2 (OFFICIAL TRAVEL DOCUMENTS/ID CARDS):
I<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<
D231458907UTO7408122F1204159<<<<<<<6

## TD3 (PASSPORTS):
P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<
L898902C<3UTO6908061F9406236ZE184226B<<<<<14

## MRV-A (VISAS):
V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<
L8988901C4XXX4009078F96121096ZE184226B<<<<<<

## MRV-B (VISAS):
V<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<
L8988901C4XXX4009078F9612109<<<<<<<<

Devlopment for this project started on: Oct/19/2021.
