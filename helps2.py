# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 04:29:46 2022

@author: jrmfi
"""

texto_a = '''
Props
Required
onPress
Handler to be called when the user taps the button.

TYPE
({ nativeEvent: PressEvent })
Requiredtitle
Text to display inside the button. On Android the given title will be converted to the uppercased form.

TYPE
string
accessibilityLabel
Text to display for blindness accessibility features.

TYPE
string
accessibilityLanguage iOS
A value indicating which language should be used by the screen reader when the user interacts with the element. It should follow the BCP 47 specification.

See the iOS accessibilityLanguage doc for more information.

TYPE
string
accessibilityActions
Accessibility actions allow an assistive technology to programmatically invoke the actions of a component. The accessibilityActions property should contain a list of action objects. Each action object should contain the field name and label.

See the Accessibility guide for more information.

TYPE	REQUIRED
array	No
onAccessibilityAction
Invoked when the user performs the accessibility actions. The only argument to this function is an event containing the name of the action to perform.

See the Accessibility guide for more information.

TYPE	REQUIRED
function	No
color
Color of the text (iOS), or background color of the button (Android).

TYPE	DEFAULT
color	`'#2196F3'` Android
'#007AFF' iOS
disabled
If true, disable all interactions for this component.

TYPE	DEFAULT
bool	false
hasTVPreferredFocus TV
TV preferred focus.

TYPE	DEFAULT
bool	false
nextFocusDown AndroidTV
Designates the next view to receive focus when the user navigates down. See the Android documentation.

TYPE
number
nextFocusForward AndroidTV
Designates the next view to receive focus when the user navigates forward. See the Android documentation.

TYPE
number
nextFocusLeft AndroidTV
Designates the next view to receive focus when the user navigates left. See the Android documentation.

TYPE
number
nextFocusRight AndroidTV
Designates the next view to receive focus when the user navigates right. See the Android documentation.

TYPE
number
nextFocusUp AndroidTV
Designates the next view to receive focus when the user navigates up. See the Android documentation.

TYPE
number
testID
Used to locate this view in end-to-end tests.

TYPE
string
touchSoundDisabled Android
If true, doesn't play system sound on touch.

TYPE	DEFAULT
boolean	false
'''
props = '''
onPress
title
accessibilityLabel
accessibilityLanguage
accessibilityActions
onAccessibilityAction
color
disabled
hasTVPreferredFocus
nextFocusDown
nextFocusForward
nextFocusLeft
nextFocusRight
nextFocusUp
testID
touchSoundDisabled
'''
componentes = '''
ActivityIndicator
Button
FlatList
Image
ImageBackground
KeyboardAvoidingView
Modal
Pressable
RefreshControl
ScrollView
SectionList
StatusBar
Switch
Text
TextInput
TouchableHighlight
TouchableOpacity
TouchableWithoutFeedback
View
VirtualizedList
DrawerLayoutAndroid
TouchableNativeFeedback
InputAccessoryView
SafeAreaView
'''
def separador(texto):
    '''retirar palavras que não estão entre virgulas'''
    nome = ''
    ficha = False
    lista = []
    for s in texto:
        if s == "'" and ficha:
            ficha = False
            if not nome in ', ':
                lista.append(nome)
            nome =''
        if ficha:
            nome += s
        if s == "'" and not ficha:
            ficha = True
    return lista

palavra = ''
cont = 0
chave = False
argumentos = []
props_box = []
componentes_box = []
tratamento = []
prop = ''
arg = ''
arg_ = ''
cont1 = 0
chave2 = False

for s in componentes:
    if s.isspace():
        cont += 1
        componentes_box.append(prop)
        frase = '"'+prop+'":' + "{},"
        # print(frase)
        prop = ''
    else:
        prop += s
        
        
for s in props:
    if s.isspace():
        cont += 1
        props_box.append(prop)
        frase = f'const {prop} = []'
        # print(frase)
        prop = ''
    else:
        prop += s
props_box.append('tintColor')

for p in texto_a:
    if p.isspace():
        cont += 1
        # print(cont, palavra)
        if 'TYPE' in palavra:
            # print('Começando')
            chave = True
        if palavra in props_box and chave:
            cont1 += 1
            arg = arg.replace('TYPE','')
            arg = arg.replace(palavra,'')
            arg = arg.replace('REQUIRED','')
            arg = arg.replace('DEFAULT','')
            arg = arg.replace('functionNo',"'function'")
            arg = arg.replace('arrayNo',"'array'")
            arg = arg.replace('false','')
            arg = arg.replace('bool',"'bool'")
            arg = arg.replace(')','')
            arg = arg.replace(',',', ')
            arg = arg.replace('number',"'number'")
            arg = arg.replace('string',"'string'")
            argumentos.append(arg)
            tratamento = []
            chave = False
            arg = arg.strip()
            lista = separador(arg)
            frase = f'{palavra} {arg}'
            print(frase)
            arg = ''
        if chave:
            arg += palavra
        palavra = ''
    else:
        palavra += p
        
# for p in texto_a:
#     if p.isspace():
#         cont += 1
#         # print(cont, palavra)
#         if 'TYPE' in palavra:
#             # print('Começando')
#             chave = True
#         if palavra in props_box and chave:
#             cont1 += 1
#             arg = arg.replace('TYPE','')
#             arg = arg.replace(palavra,'')
#             arg = arg.replace('Required','')
#             arg = arg.replace('No','')
#             arg = arg.replace(')','')
#             arg = arg.replace(',',', ')
#             arg = arg.replace('number',"'number'")
#             arg = arg.replace('string',"'string'")
#             argumentos.append(arg)
#             tratamento = []
#             chave = False
#             arg = arg.strip()
#             lista = separador(arg)
#             frase = f'const {props_box[cont1]} = {lista}'
#             # print(frase)
#             arg = ''
#         if chave:
#             arg += palavra
#         palavra = ''
#     else:
#         palavra += p
        