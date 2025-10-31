from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models.signals import post_save
from django.dispatch import receiver

KLIJENT = [
    ('fizicko lice', 'Fizičko lice'),
    ('agencija', 'Agencija'),
    ('investitor', 'Investitor'),
    ('banka', 'Banka'),
    ('drugo pravno lice', 'Drugo pravno lice'),
]

TIP_KUCE = [
    ('porodicna kuca', 'Porodična kuća'),
    ('kuce sa vise stanova', 'Kuće sa više stanova'),
    ('montazne kuce', 'Montažne kuće'),
    ('duplex kuca', 'Duplex kuće'),
]

TEREN = [
    ('blaga kosina', 'Blaga kosina'),
    ('kosina', 'Kosina'),
    ('ravno', 'Ravno'),
    ('terasasto zemljiste', 'Terasasto zemljište'),
    ('drugo', 'Drugo'),
]

VRSTA_KUCE = [
    ('klasicna kuca', 'Klasična kuća'),
    ('porodicna vila', 'Porodična kuća'),
    ('bungalov', 'Bungalov'),
    ('drvena kuca', 'Drvena kuća '),
    ('viseporodicna kuca', 'Višeporodična kuća'),
]

KANALIZACIJA = [
    ('javna kanalizacija', 'Javna kanalizacija'),
    ('septicka jama sa prelivnom jamom', 'Septička jama sa prelivnom jamom'),
    ('septicka jama bez prelivne jame', 'Septička jama bez prelivne jame'),
    ('bez odvodnog sistema', 'Bez odvodnog sistema'),

]


POD_KATEGORIJA = [
    ('garsonjera', 'Garsonjera'),
    ('jednosoban stan', 'Jednosoban stan'),
    ('dvosoban stan', 'Dvosoban stan'),
    ('trosoban stan', 'Trosoban stan'),
    ('cetvorosoban stan', 'Četvorosoban stan'),
    ('petosoban+ stan', 'Petosoban+ stan'),
    ('porodicna kuca', 'Porodična kuća'),
    ('kuce sa vise stanova', 'Kuće sa više stanova'),
    ('montazne kuce', 'Montažne kuće'),
    ('duplex kuce', 'Duplex kuće'),
    ('garaze i parking mesta', 'Garaže i parking mesta'),
    ('bastenska kucica / Zimovnik', 'Baštenska kućica / Zimovnik'),
    ('skladista / ostave', 'Skladišta/ Ostave'),
    ('prostorije za hobi', 'Prostorije za hobi'),
    ('vocnjak', 'Voćnjak'),
    ('livada, pašnjak', 'Livada, pašnjak'),
    ('obradiva zemlja', 'Obradiva zemlja'),
    ('sumsko zemljište', 'Šumsko zemljište'),
    ('pokretna kuca / bungalov', 'Pokretna kuća / bungalov'),
    ('brvnara', 'Brvnara'),
    ('vikendica, kuca za odmor', 'Vikendica, Kuća za odmor'),
    ('apartmani u hotelu', 'Apartmani u hotelu'),
    ('apartmani u kuci', 'Apartmani u kući'),
    ('apartmani u stambenoj zgradi', 'Apartmani u stambenoj zgradi'),
    ('kancelarije', 'Kancelarije'),
    ('poslovna zgrada', 'Poslovna zgrada'),
    ('komercijalni objekat / lokal', 'Komercijalni objekat / lokal'),
    ('magacin', 'Magacin'),
    ('ordinacija', 'Ordinacija'),
    ('restoran', 'Restoran'),
    ('hotel, prenoćište', 'Hotel, prenoćište'),
    ('kafici', 'Kafići'),
    ('spa centar', 'Spa centar'),
    ('sportski objekat', 'Sportski objekat'),
    ('poljoprivredni objekti', 'Poljoprivredni objekti'),
    ('proizvodni prostor', 'Proizvodni prostor'),
    ('radionice / servisi', 'Radionice / Servisi'),
]

KATEGORIJA = [
    ('stanovi', 'Stanovi'),
    ('kuce', 'Kuće'),
    ('sobe', 'Sobe'),
    ('ostali tipovi prostora', 'Ostali tipovi prostora'),
    ('gradjevinska zemljista', 'Građevinska zemljišta'),
    ('poljoprivredna zemljista', 'Poljoprivredna zemljišta'),
    ('vikendice i brvnare', 'Vikendice i brvnare'),
    ('stan na dan', 'Stan na dan'),
    ('poslovni prostori', 'Poslovni prostori'),
    ('ugostiteljski objekti', 'Ugostiteljski objekti'),
    ('stan na dan', 'Stan na dan'),
    ('poslovni prostori', 'Poslovni prostori'),
    ('sportski objekti', 'Sportski objekti'),
    ('proizvodni objekti', 'Proizvodni objekti'),
]

DRZAVE = [
    ('srbija', 'Srbija'),
    ('bosna_i_hercegovina', 'Bosna i Hercegovina'),
    ('bugarska', 'Bugarska'),
    ('crna_gora', 'Crna Gora'),
    ('grcka', 'Grčka'),
    ('hrvatska', 'Hrvatska'),
]

GRADOVI = [
    ('aleksinac', 'Aleksinac'),
    ('alibunar', 'Alibunar'),
    ('arandjelovac', 'Aranđelovac'),
    ('asanja', 'Ašanja'),
    ('badanj', 'Badanj'),
    ('badovinci', 'Badovinci'),
    ('bajina_basta', 'Bajina Bašta'),
    ('baljevac', 'Baljevac'),
    ('banatski_karlovac', 'Banatski Karlovac'),
    ('banatski_sokolac', 'Banatski Sokolac'),
    ('banatsko_novo_selo', 'Banatsko Novo Selo'),
    ('banja_koviljaca', 'Banja Koviljača'),
    ('banja_vrujci', 'Banja Vrujci'),
    ('banjani', 'Banjani'),
    ('banostor', 'Banoštor'),
    ('baranda', 'Baranda'),
    ('baric', 'Barič'),
    ('batocina', 'Batočina'),
    ('bavaniste', 'Bavanište'),
    ('bac', 'Bač'),
    ('backa_palanka', 'Bačka Palanka'),
    ('backa_topola', 'Bačka Topola'),
    ('backi_gracac', 'Bački Gračac'),
    ('backi_jarak', 'Bački Jarak'),
    ('backi_petrovac', 'Bački Petrovac'),
    ('backo_gradiste', 'Bačko Gradište'),
    ('backo_petrovo_selo', 'Bačko Petrovo Selo'),
    ('begec', 'Begeč'),
    ('beograd', 'Beograd'),
    ('beocin', 'Beočin'),
    ('berkovac', 'Berkovac'),
    ('becej', 'Bečej'),
    ('becmen', 'Bečmen'),
    ('beska', 'Beška'),
    ('bogatic', 'Bogatić'),
    ('bojnik', 'Bojnik'),
    ('bolec', 'Boleč'),
    ('boljevac', 'Boljevac'),
    ('boljevci', 'Boljevci'),
    ('bor', 'Bor'),
    ('bosilegrad', 'Bosilegrad'),
    ('bosnjace', 'Bošnjace'),
    ('brajkovac', 'Brajkovac'),
    ('brzece', 'Brzeće'),
    ('bubanj', 'Bubanj'),
    ('bujanovac', 'Bujanovac'),
    ('bukovac', 'Bukovac'),
    ('budjanovci', 'Buđanovci'),
    ('carina', 'Carina'),
    ('crepaja', 'Crepaja'),
    ('crvenka', 'Crvenka'),
    ('cvetke', 'Cvetke'),
    ('deliblato', 'Deliblato'),
    ('despotovac', 'Despotovac'),
    ('dec', 'Deč'),
    ('divci', 'Divci'),
    ('divos', 'Divoš'),
    ('divcibare', 'Divčibare'),
    ('dici', 'Dići'),
    ('dobanovci', 'Dobanovci'),
    ('dobrica', 'Dobrica'),
    ('doljevac', 'Doljevac'),
    ('dolovo', 'Dolovo'),
    ('donja_satornja', 'Donja Šatornja'),
    ('donji_milanovac', 'Donji Milanovac'),
    ('draginje', 'Draginje'),
    ('drazevac', 'Draževac'),
    ('dubovac', 'Dubovac'),
    ('dudovica', 'Dudovica'),
    ('erdevik', 'Erdevik'),
    ('futog', 'Futog'),
    ('gadin_han', 'Gadžin Han'),
    ('gaj', 'Gaj'),
    ('gajdobra', 'Gajdobra'),
    ('glogonj', 'Glogonj'),
    ('glozan', 'Gložan'),
    ('golubac', 'Golubac'),
    ('gornji_milanovac', 'Gornji Milanovac'),
    ('gospodinci', 'Gospođinci'),
    ('gracac', 'Gračac'),
    ('grdica', 'Grdica'),
    ('grocka', 'Grocka'),
    ('guca_varosica', 'Guča (varošica)'),
    ('hrtkovci', 'Hrtkovci'),
    ('idvor', 'Idvor'),
    ('indjija', 'Inđija'),
    ('irig', 'Irig'),
    ('ivanjica', 'Ivanjica'),
    ('ivanovo', 'Ivanovo'),
    ('jabuka', 'Jabuka'),
    ('jabucje', 'Jabučje'),
    ('jagodina', 'Jagodina'),
    ('jajcic', 'Jajčić'),
    ('jakovo', 'Jakovo'),
    ('jarcujak', 'Jarčujak'),
    ('jasenak', 'Jasenak'),
    ('jelasnica', 'Jelašnica'),
    ('kanjiza', 'Kanjiža'),
    ('kaonik', 'Kaonik'),
    ('karlovcic', 'Karlovčić'),
    ('kac', 'Kać'),
    ('kacarevo', 'Kačarevo'),
    ('kikinda', 'Kikinda'),
    ('kisac', 'Kisač'),
    ('kladovo', 'Kladovo'),
    ('knic', 'Knić'),
    ('knjazevac', 'Knjaževac'),
    ('konarevo', 'Konarevo'),
    ('konatice', 'Konatice'),
    ('kopaonik', 'Kopaonik'),
    ('kostol', 'Kostol'),
    ('kovacica', 'Kovačica'),
    ('kovilj', 'Kovilj'),
    ('kovin', 'Kovin'),
    ('kragujevac', 'Kragujevac'),
    ('kraljevo', 'Kraljevo'),
    ('krivi_vir', 'Krivi Vir'),
    ('krusedol_selo', 'Krušedol Selo'),
    ('krusevac', 'Kruševac'),
    ('krusevac', 'Kruševac'),
    ('krcedin', 'Krčedin'),
    ('kula', 'Kula'),
    ('kupinovo', 'Kupinovo'),
    ('kursumlija', 'Kuršumlija'),
    ('lazarevac', 'Lazarevac'),
    ('lacarak', 'Laćarak'),
    ('lebane', 'Lebane'),
    ('ledinci', 'Ledinci'),
    ('leskovac', 'Leskovac'),
    ('lezimir', 'Ležimir'),
    ('lipolist', 'Lipolist'),
    ('lipovica', 'Lipovica'),
    ('ljig', 'Ljig'),
    ('ljubovija', 'Ljubovija'),
    ('loznica', 'Loznica'),
    ('majur', 'Majur'),
    ('mala_mostanica', 'Mala Moštanica'),
    ('mali_pozarevac', 'Mali Požarevac'),
    ('mali_zvornik', 'Mali Zvornik'),
    ('malo_crnice', 'Malo Crniće'),
    ('maradik', 'Maradik'),
    ('mataruska_banja', 'Mataruška Banja'),
    ('melenci', 'Melenci'),
    ('merosina', 'Merošina'),
    ('metikos', 'Metikoš'),
    ('metkovic', 'Metković'),
    ('milesevo', 'Mileševo'),
    ('miljkovica', 'Miljkovica'),
    ('mionica_selo', 'Mionica (selo)'),
    ('mionica_varosica', 'Mionica (varošica)'),
    ('mionica', 'Mionica'),
    ('mirasevac', 'Miraševac'),
    ('mislodin', 'Mislođin'),
    ('mladenovac_selo', 'Mladenovac (selo)'),
    ('mladenovac', 'Mladenovac'),
    ('mramor', 'Mramor'),
    ('mramorak', 'Mramorak'),
    ('mrcici', 'Mrčići'),
    ('nadrlje', 'Nadrlje'),
    ('nemenikuc', 'Nemenikuće'),
    ('nis', 'Niš'),
    ('niska_banja', 'Niška Banja'),
    ('nova_varos', 'Nova Varoš'),
    ('novi_becej', 'Novi Bečej'),
    ('novi_pazar', 'Novi Pazar'),
    ('novi_sad', 'Novi Sad'),
    ('novi_slankamen', 'Novi Slankamen'),
    ('obrenovac', 'Obrenovac'),
    ('obrovac', 'Obrovac'),
    ('odzaci', 'Odžaci'),
    ('omoljica', 'Omoljica'),
    ('oplanići', 'Oplanići'),
    ('opovo', 'Opovo'),
    ('orasac', 'Orašac'),
    ('ostrovo', 'Ostrovo'),
    ('ovcar_banja', 'Ovčar Banja'),
    ('ovca', 'Ovča'),
    ('padina', 'Padina'),
    ('palanka', 'Palanka'),
    ('palic', 'Palić'),
    ('palilula', 'Palilula'),
    ('pancevo', 'Pančevo'),
    ('paracin', 'Paraćin'),
    ('pasic', 'Pasić'),
    ('patizan', 'Partizan'),
    ('pecinci', 'Pećinci'),
    ('pec', 'Peć'),
    ('pecani', 'Pećani'),
    ('petka', 'Petka'),
    ('petkovica', 'Petkovica'),
    ('petrovaradin', 'Petrovaradin'),
    ('pinosava', 'Pinosava'),
    ('pirot', 'Pirot'),
    ('pirot', 'Pirot'),
    ('piscani', 'Piščani'),
    ('pivnica', 'Pivnica'),
    ('plac', 'Plac'),
    ('podgorica', 'Podgorica'),
    ('podrezak', 'Podrezak'),
    ('pojac', 'Pojac'),
    ('popovac', 'Popovac'),
    ('popovac', 'Popovac'),
    ('potpec', 'Potpeć'),
    ('pozega', 'Požega'),
    ('pozarevac', 'Požarevac'),
    ('prekovac', 'Prekovac'),
    ('presevo', 'Preševo'),
    ('priboj', 'Priboj'),
    ('pridvorica', 'Pridvorica'),
    ('prigrevica', 'Prigrevica'),
    ('prijepolje', 'Prijepolje'),
    ('prokuplje', 'Prokuplje'),
    ('raca', 'Rača'),
    ('racovnik', 'Racovnik'),
    ('rakovica', 'Rakovica'),
    ('rakovac', 'Rakovac'),
    ('ralja', 'Ralja'),
    ('rataje', 'Rataje'),
    ('ravan', 'Ravan'),
    ('ravnje', 'Ravnje'),
    ('ravanic', 'Ravanic'),
    ('redjina', 'Redjina'),
    ('renic', 'Renić'),
    ('rezek', 'Rezek'),
    ('rešica', 'Rešica'),
    ('riznic', 'Riznic'),
    ('rojkova', 'Rojkova'),
    ('rojkovac', 'Rojkovac'),
    ('rojkovići', 'Rojkovići'),
    ('rojkovic', 'Rojković'),
    ('ronic', 'Ronic'),
    ('roncovic', 'Roncović'),
    ('ronići', 'Ronići'),
    ('rovni', 'Rovni'),
    ('rudna_glava', 'Rudna Glava'),
    ('rudnik', 'Rudnik'),
    ('ruma', 'Ruma'),
    ('rusanj', 'Rusanj'),
    ('savinac', 'Savinac'),
    ('sekici', 'Sekići'),
    ('sekulići', 'Sekulići'),
    ('selace', 'Selače'),
    ('seonica', 'Seonica'),
    ('sikole', 'Sikole'),
    ('silovo', 'Silovo'),
    ('sivac', 'Sivac'),
    ('skela', 'Skela'),
    ('skobalj', 'Skobalj'),
    ('slatina', 'Slatina'),
    ('slepčević', 'Slepčević'),
    ('slijepčević', 'Slijepčević'),
    ('slovica', 'Slovica'),
    ('smederevo', 'Smederevo'),
    ('smederevska_palanka', 'Smederevska Palanka'),
    ('soko_banja', 'Soko Banja'),
    ('sokolac', 'Sokolac'),
    ('sombor', 'Sombor'),
    ('sopot', 'Sopot'),
    ('sopron', 'Sopron'),
    ('sovljak', 'Sovljak'),
    ('sracinec', 'Sračinec'),
    ('sremska_mitrovica', 'Sremska Mitrovica'),
    ('sremski_karlovci', 'Sremski Karlovci'),
    ('sremski_mihaljevci', 'Sremski Mihaljevci'),
    ('stara_pazova', 'Stara Pazova'),
    ('starcevo', 'Starčevo'),
    ('subotica', 'Subotica'),
    ('surcin', 'Surčin'),
    ('surdulica', 'Surdulica'),
    ('svetozarevo', 'Svetozarevo'),
    ('svrljig', 'Svrljig'),
    ('tajšić', 'Tajšić'),
    ('temerin', 'Temerin'),
    ('teskic', 'Teskić'),
    ('titov', 'Titov'),
    ('trstenik', 'Trstenik'),
    ('tumane', 'Tumane'),
    ('ulcinj', 'Ulcinj'),
    ('umberg', 'Umberg'),
    ('učiteljić', 'Učiteljić'),
    ('uzice', 'Užice'),
    ('valjevo', 'Valjevo'),
    ('veliki_idjos', 'Veliki Iđoš'),
    ('velika_plana', 'Velika Plana'),
    ('velika_hoča', 'Velika Hoča'),
    ('velika_jelica', 'Velika Jelica'),
    ('veliko_gradiste', 'Veliko Gradište'),
    ('vilovo', 'Vilovo'),
    ('vojka', 'Vojka'),
    ('vrbas', 'Vrbas'),
    ('vranje', 'Vranje'),
    ('vrbovac', 'Vrbovac'),
    ('vrnića', 'Vrnića'),
    ('vrnjacka_banja', 'Vrnjačka Banja'),
    ('vrnjci', 'Vrnjci'),
    ('vrcenovica', 'Vrćenovica'),
    ('vrcin', 'Vrčin'),
    ('vrsac', 'Vršac'),
    ('zajecar', 'Zaječar'),
    ('zaklopaca', 'Zaklopača'),
    ('zalug', 'Zalug'),
    ('zaovine', 'Zaovine'),
    ('zlatibor', 'Zlatibor'),
    ('zmajevo', 'Zmajevo'),
    ('zrenjanin', 'Zrenjanin'),
    ('zuce', 'Zuce'),
    ('zvecka', 'Zvečka'),
    ('cicevac', 'Ćićevac'),
    ('cuprija', 'Ćuprija'),
    ('cajetina', 'Čajetina'),
    ('cacak', 'Čačak'),
    ('cenej', 'Čenej'),
    ('centa', 'Čenta'),
    ('cerevic', 'Čerević'),
    ('cibukovac', 'Čibukovac'),
    ('cibutkovica', 'Čibutkovica'),
    ('coka', 'Čoka'),
    ('cortanovci', 'Čortanovci'),
    ('cukojevac', 'Čukojevac'),
    ('curug', 'Čurug'),
    ('djurinci', 'Đurinci'),
    ('sabac', 'Šabac'),
    ('sid', 'Šid'),
    ('simanovci', 'Šimanovci'),
    ('susnjar', 'Šušnjar'),
    ('zabalj', 'Žabalj'),
    ('zitiste', 'Žitište'),
    ('zica', 'Žiča'),
]

TOPLA_VODA = [
    ('toplana', 'Toplana'),
    ('bojler', 'Bojler'),
    ('kotao na gas', 'Kotao Na Gas'),
    ('kotao na struju', 'Kotao Na Struju'),
    ('grejanje na cvrsto gorivo', 'Grejanje Na Cvrsto Gorivo'),

]

DODATNA_OPREMLJENOST = [
    ('garaza', 'Garaža'),
    ('lift', 'Lift'),
    ('vrt', 'Vrt'),
    ('garazno_mesto', 'Garažno mesto'),
    ('pristup_bez_barijera', 'Pristup bez barijera'),
    ('toplotna_izolacija', 'Toplotna izolacija'),
    ('spoljno_parking_mesto', 'Spoljno parking mesto'),
    ('terasa', 'Terasa'),
    ('bazen', 'Bazen'),
    ('sigurnosni_uredjaji', 'Sigurnosni uređaji'),
    ('javni_parking', 'Javni parking'),
    ('balkon', 'Balkon'),
    ('sauna', 'Sauna'),
    ('lodja', 'Lođa'),
    ('obezbedjenje', 'Obezbeđenje'),
    ('garderoberi', 'Garderoberi'),
    ('teretana', 'Teretana'),
    ('staklena_basta', 'Staklena bašta'),
    ('vesernica', 'Vešernica'),
    ('recepcija', 'Recepcija'),
    ('ostava', 'Ostava'),
    ('kamin', 'Kamin'),
    ('igraliste', 'Igralište'),
    ('podrum', 'Podrum'),
]


GREJANJE = [
    ('centralno grejanje', 'Centralno Grejanje'),
    ('ta pec', 'TA Peć'),
    ('klima uredjaj', 'Klima Uredjaj'),
    ('etazno grejanje na struju', 'Etažno Grejanje Na Struju'),
    ('etazno grejanje na cvrsto gorivo', 'Etažno Grejanje Na Čvrsto Gorivo'),
    ('etazno grejanje na gas', 'Etažno Grejanje Na Gas'),
    ('podno grejanje', 'Podno Grejanje'),
    
]

TEHNICKA_OPREMLJENOST = [
    ('telefon', 'Telefon'),
    ('internet', 'Internet'),
    ('kablovska_tv', 'Kablovska TV'),
    ('opticka_mreza', 'Optička mreža'),
    ('video_nadzor', 'Video Nadzor'),
    ('interfon', 'Interfon'),
    ('alarmni_sistem', 'Alarmni Sistem'),
    ('protivpozarni_sistem', 'Protivpožarni Sistem'),
]

SPRATNOST = [
    ('suteren', 'Suteren'),
    ('prizemlje', 'Prizemlje'),
    ('visoko prizemlje', 'Visoko Prizemlje'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
]

VRSTA_STANA = [
    ('duplex', 'Duplex'),
    ('stan u kuci', 'Stan U Kući'),
    ('dvorisni stan', 'Dvorišni Stan'),
    ('penthaus', 'Penthaus'),
    ('salonski stan', 'Salonski Stan'),
    ('stan u zgradi', 'Stan U Zgradi'),
    
]

STANJE_NEKRETNINE = [
    ('izvorno stanje', 'Izvorno Stanje'),
    ('standardna gradnja', 'Standardna Gradnja'),
    ('novogradnja', 'Novogradnja'),
    ('u pripremi', 'U Pripremi'),
    ('u izgradnji', 'U Izgradnji'),
    ('zavrsena izgradnja', 'Završena Izgradnja'),
    ('delimicna rekonstrukcija', 'Delimična Rekonstrukcija'),
]

STRUKTURA_CHOICES = [
    ('garsonjera', 'Garsonjera'),
    ('jednosoban stan', 'Jednosoban Stan'),
    ('dvosoban stan', 'Dvosoban stan'),
    ('trosoban stan', 'Trosoban stan'),
    ('cetvrosoban stan', 'Cetvorosoban stan'),
    ('petosoban+ stan', 'Petosoban+ stan'),
]

RENT_CHOICES = [
    ('iznajmljivanje', 'Iznajmljivanje'),
    ('prodaja', 'Prodaja')
]

POZICIJA = [
    ('centar', 'Centar'),
    ('vikend naselje', 'Vikend Naselje'),
    ('periferija', 'Periferija'),
    ('strogi centar grada', 'Strogi Centar Grada'),
    ('zaseok', 'Zaseok'),
    ('stambeno naselje', 'Stambeno Naselje'),
    ('mirna lokacija', 'Mirna Lokacija'),
]


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    post_office_box = models.CharField(max_length=55)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=32, choices=GRADOVI, blank=True)
    postal_code = models.CharField(max_length=10, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')], blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile', null=True, blank=True)
    client_type = models.CharField(max_length=32, choices=KLIJENT, blank=True)
    
    image = models.ImageField(upload_to='clients/profiles/', blank=True)
    
@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    if hasattr(instance, 'client_profile'):
        instance.client_profile.save()
        
        

class Conversation(models.Model):
    participants = models.ManyToManyField(
        User,
        related_name='conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {', '.join([u.username for u in self.participants.all()])}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class PropertyBase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    technical_equipment = models.CharField(max_length=32, choices=TEHNICKA_OPREMLJENOST, blank=True)
    category = models.CharField(max_length=32, choices=KATEGORIJA, null=True)
    sub_category = models.CharField(max_length=32, choices=POD_KATEGORIJA, null=True)

    title = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    posted = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    variety = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=32, choices=GRADOVI, blank=True)
    address = models.CharField(max_length=255, blank=True)
    listing_type = models.CharField(
        max_length=20, 
        choices=RENT_CHOICES
    )
    registered = models.BooleanField(default=False)
    owner = models.BooleanField(default=True)
    area = models.DecimalField(max_digits=7, decimal_places=2)
    rooms = models.IntegerField()
    heating_type = models.CharField(max_length=32, choices=GREJANJE, blank=True)
    floor = models.IntegerField()
    furnishing = models.CharField(max_length=50)
    additional_furnishing = models.TextField(blank=True, null=True)
    total_number_of_rooms = models.IntegerField(blank=True, null=True)
    
    is_feautured = models.BooleanField(default=False)
    
    images = GenericRelation('PropertyImage', related_query_name='properties')

    class Meta:
        abstract = True
        
class PropertyImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    property = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField(upload_to='properties/%Y/%m/%d/')
    is_main = models.BooleanField(default=False)
    is_thumbnail = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Apartment(PropertyBase):
    structure = models.CharField(max_length=23, choices=STRUKTURA_CHOICES, blank=True)
    located = models.CharField(max_length=25, choices=POZICIJA, blank=True)
    property_condition = models.CharField(max_length=25, choices=STANJE_NEKRETNINE, blank=True)
    aparment_type = models.CharField(max_length=25, choices=VRSTA_STANA, blank=True)
    floor_level = models.CharField(max_length=25, choices=SPRATNOST, blank=True)
    heating_type = models.CharField(max_length=32, choices=GREJANJE, blank=True)
    additional_equipment = models.CharField(max_length=25, choices=DODATNA_OPREMLJENOST, blank=True)
    hot_water = models.CharField(max_length=25, choices=TOPLA_VODA, blank=True)
    pass

class House(PropertyBase):
    house_type = models.CharField(max_length=23, choices=TIP_KUCE, blank=True)
    land_area_in_ares = models.IntegerField(default=0, blank=True)
    terrain = models.CharField(max_length=23, choices=TEREN, blank=True)
    house_category = models.CharField(max_length=23, choices=VRSTA_KUCE, blank=True)
    sewage_system = models.CharField(max_length=32, choices=KANALIZACIJA, blank=True)

    yard_area = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    pass

class Agency(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=32, choices=GRADOVI)
    country = models.CharField(max_length=32, choices=DRZAVE)
    postal_code = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')])
    
    summary = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=755, blank=True)

    broker_registration_number = models.IntegerField()
    business_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='agencies/logos/', blank=True)


class Investor(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=32, choices=GRADOVI, blank=True)
    country = models.CharField(max_length=32, choices=DRZAVE)
    postal_code = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')])

    summary = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=755, blank=True)

    business_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='investors/logos/', blank=True)
    

class Bank(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=32, choices=GRADOVI, blank=True)
    country = models.CharField(max_length=32, choices=DRZAVE, blank=True)
    postal_code = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')])

    summary = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=755, blank=True)

    business_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='banks/logos/', blank=True)