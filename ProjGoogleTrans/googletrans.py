#import googletrans

#print(googletrans.LANGUAGES)

from googletrans import Translator
translator = Translator()

translate_channel = translator.translate('जारी रखना', dest='ja')

#translate_channel = translator.translate('Canal La Tele Perú', src='es', dest='en').group()
#translate_channel2 = translator.translate('La defensa y las acciones ofensivas de Alex Dujshebaev dan a Españasu cuarto bronce en unos Juegos tras los de Atlanta 1996, Sydney 2000 y Pekín 2008.', src='es', dest='en')
#print(translate_channel)
#print(translate_channel2) 