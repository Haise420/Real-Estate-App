Real Estate Project Documentation
Choices for Models
KLIJENT
Fizičko lice

Agencija

Investitor

Banka

Drugo pravno lice

TIP_KUCE
Porodična kuća

Kuće sa više stanova

Montažne kuće

Duplex kuća

TEREN
Blaga kosina

Kosina

Ravno

Terasasto zemljište

Drugo

VRSTA_KUCE
Klasična kuća

Porodična vila

Bungalov

Drvena kuća

Višeporodična kuća

KANALIZACIJA
Javna kanalizacija

Septička jama sa prelivnom jamom

Septička jama bez prelivne jame

Bez odvodnog sistema

POD_KATEGORIJA
Garsonjera

Jednosoban stan

Dvosoban stan

Trosoban stan

Četvorosoban stan

Petosoban+ stan

Porodična kuća

Kuće sa više stanova

Montažne kuće

Duplex kuće

Garaže i parking mesta

Baštenska kućica / Zimovnik

Skladišta/ Ostave

Prostorije za hobi

Voćnjak

Livada, pašnjak

Obradiva zemlja

Šumsko zemljište

Pokretna kuća / bungalov

Brvnara

Vikendica, Kuća za odmor

Apartmani u hotelu

Apartmani u kući

Apartmani u stambenoj zgradi

Kancelarije

Poslovna zgrada

Komercijalni objekat / lokal

Magacin

Ordinacija

Restoran

Hotel, prenoćište

Kafići

Spa centar

Sportski objekat

Poljoprivredni objekti

Proizvodni prostor

Radionice / Servisi

KATEGORIJA
Stanovi

Kuće

Sobe

Ostali tipovi prostora

Građevinska zemljišta

Poljoprivredna zemljišta

Vikendice i brvnare

Stan na dan

Poslovni prostori

Ugostiteljski objekti

Sportski objekti

Proizvodni objekti

DRZAVE
Srbija

Bosna i Hercegovina

Bugarska

Crna Gora

Grčka

Hrvatska

GRADOVI
Aleksinac

Alibunar

Aranđelovac

Ašanja

Beograd

Novi Sad

Niš

1. Client Model
first_name: Client's first name

last_name: Client's last name

cell_phone: Client's cell phone

number email: Client's email address

post_office_box: Client's PO box

address: Client's address (optional)

city: Client's city (choices: GRADOVI)

postal_code: Postal code (numeric only)

client_type: Client type (choices: KLIJENT)

2. PropertyBase Model (Abstract)
category: Property category (KATEGORIJA)

sub_category: Property sub-category (POD_KATEGORIJA)

title: Property title

last_updated: Last updated timestamp

posted: Initial post timestamp

price: Property price

description: Property description

variety: Property variety

location: Property location

city: City (choices: GRADOVI)

address: Full address (optional)

listing_type: Listing type (choices: RENT_CHOICES)

registered: Is the property registered?

owner: Is the owner selling directly?

area: Property area in square meters

rooms: Number of rooms

heating: Heating type

floor: Floor number

furnishing: Type of furnishing

additional_furnishing: Additional furnishing (optional)

total_number_of_rooms: Total rooms (optional)

3. Apartment Model (Inherits PropertyBase)
structure: Structure type (STRUKTURA_CHOICES)

located: Position (POZICIJA)

property_condition: Condition (STANJE_NEKRETNINE)

aparment_type: Type (VRSTA_STANA)

floor_level: Floor level (SPRATNOST)

heating_type: Heating type (GREJANJE)

additional_equipment: Additional equipment (DODATNA_OPREMLJENOST)

hot_water: Hot water type (TOPLA_VODA)

4. House Model (Inherits PropertyBase)
house_type: House type (TIP_KUCE)

land_area_in_ares: Land area in ares

terrain: Terrain type (TEREN)

house_category: House category (VRSTA_KUCE)

sewage_system: Sewage system (KANALIZACIJA)

yard_area: Yard area (optional)

5. Agencie Model
title: Agency name

city: City (choices: GRADOVI)

country: Country (choices: DRZAVE)

postal_code: Postal code

summary: Short summary

description: Detailed description

broker_registration_number: Registration number

business_phone: Business phone number

cell_phone: Contact cell phone

website: Agency website

logo: Agency logo

6. Investor Model
title: Investor name

city: City (choices: GRADOVI)

country: Country (choices: DRZAVE)

postal_code: Postal code

summary: Short summary

description: Detailed description

broker_registration_number: Registration number

business_phone: Business phone number

cell_phone: Contact cell phone

website: Investor website

logo: Investor logo

7. Bank Model
title: Bank name

city: City (choices: GRADOVI)

country: Country (choices: DRZAVE)

postal_code: Postal code

summary: Short summary

description: Detailed description

broker_registration_number: Registration number

business_phone: Business phone number

cell_phone: Contact cell phone

website: Bank website

logo: Bank logo
