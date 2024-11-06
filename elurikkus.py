from random import randint
import requests
import re
# Õpikust: https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/tkinteri-vidinad/
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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
              ('harilik palusammal (Pleurozium schreberi'),
              ('kähar sulgsammal (Ctenidium molluscum'),
              ('niidukäharik (Rhytidiadelphus squarrosus'),
              ('metsakäharik (Rhytidiadelphus triquetrus'),
              ('harilik lehviksammal (Ptilium crista-castrensis'),
              ('harilik teravtipp (Calliergonella cuspidata'),
              ('aasosi (Equisetum pratense'),
              ('konnaosi (Equisetum fluviatile'),
              ('metsosi (Equisetum sylvaticum'),
              ('põldosi (Equisietum arvense'),
              ('raudosi (Equisetum hyemale'),
              ('soo-osi (Equisetum palustre'),
              ('kilpjalg (Pteridium aquilinum'),
              ('maarja-sõnajalg (Dryopteris filix-mas'),
              ('ohtene sõnajalg (Dryopteris carthusiana'),
              ('harilik soosõnajalg (Thelypteris palustris'),
              ('naistesõnajalg (Athyrium filix-femina'),
              ('harilik kolmissõnajalg (Gymnocarpium dryopteris'),
              ('laanesõnajalg (Matteuccia struthiopteris'),
              ('kattekold (Lycopodium annotinum'),
              ('karukold (Lycopodium clavatum'),
              ('jugapuu (Taxus baccata'),
              ('siberi nulg (Abies sibirica'),
              ('harilik kuusk (Picea abies'),
              ('harilik mänd (Pinus sylvestris'),
              ('harilik kadakas (Juniperus communis'),
              ('harilik kukerpuu (Berberis vulgaris'),
              ('kollane käoking (Aconitum lycoctonum'),
              ('salu-siumari (Actaea spicata'),
              ('võsaülane (Anemone nemorosa'),
              ('kollane ülane (Anemone ranunculoides'),
              



              
              
              
              
              
              
              ]

# Õpikust: https://web.htk.tlu.ee/digitaru/tarkvara2/chapter/tkinteri-vidinad/
root = Tk()

# Allikas: ChatGPT
#root.state("zoomed")
#root.resizable(False, False)

# Õpikust, ChatGPT-st
pilt = Image.open("karu.jpg")
pildiobjekt = ImageTk.PhotoImage(pilt)
canvas = Canvas(root, width = pilt.width, height = pilt.width)
canvas.grid(row=0, column=1)
canvas.create_image(20, 20, anchor=NW, image=pildiobjekt)

ttk.Button(root, text="Vastus 1").grid(row=1, column=0, padx = 20, pady = 20)
ttk.Button(root, text="Vastus 2").grid(row=1, column=1, padx = 20, pady = 20)
ttk.Button(root, text="Vastus 3").grid(row=1, column=2, padx = 20, pady = 20 )


root.mainloop()