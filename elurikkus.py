import random
import requests
import re
# Õpikust: https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/tkinteri-vidinad/
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
# Leheküljelt https://requests.readthedocs.io/en/latest/user/quickstart/
from io import BytesIO
# ChatGPT-st
import urllib.parse

# Taimenimed saadud: https://bio.edu.ee/taimed/general/indexnimek.html
taimenimed = [("pleurokokk", "Pleurococcus vulgaris"),
              ("vesijuus", "Ulothrix zonata"),
              ("põisadru", "Fucus vesiculosus"),
              ('harilik helvik','Marchantia polymorpha'),
              ('harilik karusammal','Polytrichum commune'),
              ('palu-karusammal','Polytrichum juniperinum'),
              ('raba-karusammal','Polytrichum strictum'),
              ('roossammal','Rhodobryum roseum'),
              ('lainjas lehiksammal','Plagiomnium undulatum'),
              ('soovildik','Aulacomnium palustre)'),
              ('soosammal','Paludella squarrosa'),
              ('lainjas kaksikhammas','Dicranum polysetum'),
              ('harilik tüviksammal','Climacium dendroides'),
              ('harilik loodehmik','Abietinella abietinum'),
              ('harilik lühikupar','Brachythecium rutabulum'),
              ('kähar salusammal','Eurhynchium angustirete'),
              ('harilik laanik','Hylocomium splendens'),
              ('harilik palusammal','Pleurozium schreberi'),
              ('kähar sulgsammal','Ctenidium molluscum'),
              ('niidukäharik','Rhytidiadelphus squarrosus'),
              ('metsakäharik','Rhytidiadelphus triquetrus'),
              ('harilik lehviksammal','Ptilium crista-castrensis'),
              ('harilik teravtipp','Calliergonella cuspidata'),
              ('aasosi','Equisetum pratense'),
              ('konnaosi','Equisetum fluviatile'),
              ('metsosi','Equisetum sylvaticum'),
              ('põldosi','Equisetum arvense'),
              ('raudosi','Equisetum hyemale'),
              ('soo-osi','Equisetum palustre'),
              ('kilpjalg','Pteridium aquilinum'),
              ('maarja-sõnajalg','Dryopteris filix-mas'),
              ('ohtene sõnajalg','Dryopteris carthusiana'),
              ('harilik soosõnajalg','Thelypteris palustris'),
              ('naistesõnajalg','Athyrium filix-femina'),
              ('harilik kolmissõnajalg','Gymnocarpium dryopteris'),
              ('laanesõnajalg','Matteuccia struthiopteris'),
              ('kattekold','Lycopodium annotinum'),
              ('karukold','Lycopodium clavatum'),
              ('jugapuu','Taxus baccata'),
              ('siberi nulg','Abies sibirica'),
              ('harilik kuusk','Picea abies'),
              ('harilik mänd','Pinus sylvestris'),
              ('harilik kadakas','Juniperus communis'),
              ('harilik kukerpuu','Berberis vulgaris'),
              ('kollane käoking','Aconitum lycoctonum'),
              ('salu-siumari','Actaea spicata'),
              ('võsaülane','Anemone nemorosa'),
              ('kollane ülane','Anemone ranunculoides'),
              ('metsülane','Anemone sylvestris'),
              ('varsakabi','Caltha palustris'),
              ('sinilill','Hepatica nobilis'),
              ('aas-karukell','Pulsatilla pratensis'),
              ('metstulikas','Ranunculus cassubicus'),
              ('kanakoole','Ranunculus ficaria'),
              ('roomav tulikas','Ranunculus repens'),
              ('kullerkupp','Trollius europaeus'),
              ('kollane vesikupp','Nuphar lutea'),
              ('väike vesiroos','Nymphaea candida'),
              ('metspipar','Asarum europaeum'),
              ('soopihl','Comarum palustre'),
              ('angervaks','Filipendula ulmaria'),
              ('metsmaasikas','Fragaria vesca'),
              ('muulukas','Fragaria viridis'),
              ('ojamõõl','Geum rivale'),
              ('maamõõl','Geum urbanum'),
              ('harilik toomingas','Prunus padus'),
              ('hanijalg','Potentilla anserina'),
              ('tedremaran','Potentilla erecta'),
              ('põõsasmaran','Potentilla fruticosa'),
              ('mesimurakas','Rubus arcticus'),
              ('põldmurakas','Rubus caesius'),
              ('rabamurakas','Rubus chamaemorus'),
              ('harilik vaarikas','Rubus idaeus'),
              ('lillakas','Rubus saxatilis'),
              ('harilik pihlakas','Sorbus aucuparia'),
              ('võsu-liivsibul','Jovibarba globifera'),
              ('harilik kukehari','Sedum acre'),
              ('valge kukehari','Sedum album'),
              ('lepiklilll','Chrysosplenium alternifolium'),
              ('ädalalill','Parnassia palustris'),
              ('mage sõstar','Ribes alpinum'),
              ('pikalehine huulhein','Drosera anglica'),
              ('ümaralehine huulhein','Drosera rotundifolia'),
              ('harilik koldrohi','Anthyllis vulneraria'),
              ('harilik koldrohi','Anthyllis vulneraria'),
              ('aas-seahernes','Lathyrus pratensis'),
              ('mets-seahernes','Lathyrus sylvestris'),
              ('kevadine seahernes','Lathyrus vernus'),
              ('sirplutsern','Medicago falcata'),
              ('humallutsern','Medicago lupulina'),
              ('harilik lutsern','Medicago sativa'),
              ('valge mesikas','Melilotus albus'),
              ('kollane mesikas','Melilotus officinalis'),
              ('kassiristik','Trifolium arvense'),
              ('kuldristik','Trifolium aureum'),
              ('keskmine ristik','Trifolium medium'),
              ('mägiristik','Trifolium montanum'),
              ('valge ristik','Trifolium repens'),
              ('harilik hiirehernes','Vicia cracca'),
              ('aed-hiirehernes','Vicia sepium'),
              ('mets-hiirehernes','Vicia sylvatica'),
              ('ahtalehine põdrakanep','Epilobium angustifolium'),
              ('mägi-pajulill','Epilobium montanum'),
              ('näsiniin','Daphne mezereum'),
              ('mõru vahulill','Polygala amarella'),
              ('harilik vaher','Acer platanoides'),
              ('harilik hobukastan','Aesculus hippocastanum'),
              ('paakspuu','Frangula alnus'),
              ('harilik türnpuu','Rhamnus cathartica'),
              ('luuderohi','Hedera helix'),
              ('verev kontpuu','Swida sanguinea'),
              ('naat','Aegopodium podagraria'),
              ('heinputk','Angelica sylvestris'),
              ('mets-harakputk','Anthriscus sylvestris'),
              ('mürkputk','Cicuta virosa'),
              ('täpiline surmaputk','Conium maculatum'),
              ('siberi karuputk','Heracleum sibiricum'),
              ('harilik moorputk','Pastinaca sativa subsp. sylvestris'),
              ('harilik näär','Pimpinella saxifraga'),
              ('roomav madar','Galium aparine'),
              ('värvmadar','Galium boreale'),
              ('pehme madar','Galium mollugo'),
              ('hobumadar','Galium verum'),
              ('äiatar','Knautia arvensis'),
              ('harilik kuslapuu','Lonicera xylosteum'),
              ('peetrileht','Succisa pratensis'),
              ('harilik lodjapuu','Viburnum opulus'),
              ('punane leeder','Sambucus racemosa'),
              ('palderjan','Valeriana officinalis'),
              ('harilik pärn','Tilia cordata'),
              ('harilik jänesekapsas','Oxalis acetosella'),
              ('kurekael','Erodium cicutarium'),
              ('soo-kurereha','Geranium palustre'),
              ('aas-kurereha','Geranium pratense'),
              ('mets-kurereha','Geranium sylvaticum')
      ]

# Õpikust: https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/tkinteri-vidinad/
root = Tk()

# Allikas: ChatGPT
#root.state("zoomed")
#root.resizable(False, False)

# Õpikust, ChatGPT-st
#pilt = Image.open("karu.jpg")
#pildiobjekt = ImageTk.PhotoImage(pilt)
#canvas = Canvas(root, width = 4000, height = 4000)
#canvas.grid(row=0, column=1)
#pilt = None
#pildiobjekt = None
#canvas.create_image(20, 20, anchor=NW, image=pildiobjekt)

variandid = [ttk.Button(root, text="Vastus 1", command = lambda: vali_vastus(0)),
             ttk.Button(root, text="Vastus 2", command = lambda: vali_vastus(1)),
             ttk.Button(root, text="Vastus 3", command = lambda: vali_vastus(2))]
variandid[0].grid(row=2, column=0, padx = 20, pady = 20)
variandid[1].grid(row=2, column=1, padx = 20, pady = 20)
variandid[2].grid(row=2, column=2, padx = 20, pady = 20)
# Miskipärast nõuab tkinter tekstile oma eraldi muutujat
tulemus_tekst = StringVar()
ttk.Label(root, textvariable=tulemus_tekst).grid(row=0, column=1)

headers = {'user-agent': 'elurikkus/0.0.1'}
# Õige variant peab olema ka funktsioonist väljaspoolt kättesaadav (kõik on globalid, sest ma enam ei viitsi)
õige_variant = -1
vastus = ()
def uuenda():
    # Allikas: https://requests.readthedocs.io/en/latest/user/quickstart/
    # API info: https://www.mediawiki.org/wiki/API:REST_API
    
    # https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
    global õige_variant
    global vastus
    
    vastused = random.sample(taimenimed, k=4)
    vastus = vastused[0]
    valed_vastused = vastused[1:3]
    print(vastus)
    print(valed_vastused)
    
    tulemused = requests.get(f"https://commons.wikimedia.org/w/rest.php/v1/search/page?q={vastus[1]}&type=image&filemime=jpeg&haslicense=unrestricted", headers=headers)
    json_tulemused = tulemused.json()
    
    # ChatGPT-lt
    jpeg_pildid = [image for image in json_tulemused['pages'] if image['title'].lower().endswith(('.jpg', '.jpeg'))]
    
    # Andmestruktuur: "pages" -> tulemuste järjend (valib suvalise) -> "key" (viib URL-ini)
    pildi_id = random.choice(jpeg_pildid)["key"]
    print(pildi_id)
    
    # URL-il on kindlad nõudmised
    pildi_id.replace(" ", "_")
    
    # Leiab pildi lingi Commonsist
    pildi_link = requests.get(f"https://commons.wikimedia.org/wiki/{pildi_id}", headers=headers)
    
    # URL-il on kindlad nõudmised (käsk saadud ChatGPT-st)
    failinimi = urllib.parse.quote(pildi_id.replace("File:", ""))
    
    # Regulaaravaldis saadud regex101.com abiga (leiab HTML-ist pildi URL-i)
    url = re.findall(r"upload\.wikimedia\.org\/wikipedia\/commons\/[^t]\/.{2}\/", pildi_link.text)[0]
    
    # Lõpuks leiame pildi ning muudame selle PIL mooduliga Pythonile sobivaks
    print(f"Image URL: https://{url}{failinimi}")
    pilt_raw = requests.get(f"https://{url}{failinimi}", headers=headers)
    print(pilt_raw.content)
    pilt = Image.open(BytesIO(pilt_raw.content)) # Saadud https://requests.readthedocs.io/en/latest/user/quickstart/
    print(f"Kõrgus: {pilt.height}")
    vähendustegur = 500 / pilt.height
    pilt = pilt.resize((round(pilt.width * vähendustegur), round(pilt.height * vähendustegur)))
    pildiobjekt = ImageTk.PhotoImage(pilt)
    # ChatGPT
    canvas.config(width = pilt.width, height = pilt.height)
    canvas.grid(row=1, column=1)
    canvas.create_image(0, 0, anchor="nw", image=pildiobjekt)
    canvas.image = pildiobjekt
    
    # Muudab nuppude tekstid
    õige_variant = random.randint(0, 2)
    print(f"õige variant: {õige_variant}")
    valed_variandid = [0, 1, 2]
    valed_variandid.remove(õige_variant)
    variandid[õige_variant].config(text=vastus[0])
    variandid[valed_variandid[0]].config(text=valed_vastused[0][0])
    variandid[valed_variandid[1]].config(text=valed_vastused[1][0])
    
canvas = Canvas(root)
#canvas.pack(fill="both", expand=True)
uuenda()

def vali_vastus(valik):
    print(f"Valitud {valik}, õige on {õige_variant}")
    if valik == õige_variant:
        tulemus_tekst.set("Õige vastus! Laen järgmise pildi...")
    else:
        tulemus_tekst.set(f"Vale vastus! Taim oli {vastus[0]}.")
    # ChatGPT-lt: värskendab kasutajaliidest
    root.update_idletasks()
    
    uuenda()
    tulemus_tekst.set("")
    

#canvas.create_image(0, 0, anchor=NW, image=pildiobjekt)

root.mainloop()
