#Левченко Варвара, группа 3, вариант 6
import random
   
def open_files():
    f = open('text.txt', 'r')
    text = f.readlines()
    return text

def massiv(num):
    a = open_files()[num].split()
    return a

def verb():
    return random.choice(massiv(1))
    
def pron():
    return random.choice(massiv(0))

def lang():
    return random.choice(massiv(4))

def sp_verb():
    return random.choice(massiv(2))
def noun():
    return random.choice(massiv(5))
def imper():
    return random.choice(massiv(3))
def name():
    return random.choice(massiv(6))
def verb_cond():
    return random.choice(massiv(7))

def verb_form_ques(pron, verb):
    if verb == 'parler':
        if pron == 'je':
            verb = 'parle-je'
        if pron == 'tu': 
            verb = 'parles-tu'
        if pron == 'elle':
            verb = 'parle-t-elle'
        if pron == 'il':
            verb = 'parle-t-il'
        if pron == 'nous':
            verb = 'parlons-nous'
        if pron == 'vous':
            verb = 'parlez-vous'
        if pron == 'ils':
            verb = 'parlent-ils'
        if pron == 'elles':
            verb = 'parlent-elles'
    if verb == 'apprendre':
        if pron == 'je': 
            verb = 'apprends-je'
        if pron == 'tu':
            verb = 'apprends-tu'
        if pron == 'il':
            verb = 'apprend-il'
        if pron == 'elle':
            verb = 'apprend-elle'
        if pron == 'nous':
            verb = 'apprenons-nous'
        if pron == 'vous':
            verb = 'apprenez-vous'
        if pron == 'ils':
            verb = 'apprennent-ils'
        if pron == 'elles':
            verb = 'apprennent-elles'
    return verb


def question():
    pron1 = pron()
    sentence = pron1 + ', ' + verb_form_ques(pron1, sp_verb()) + ' ' + lang() + '?'
    sentence = sentence.capitalize()
    return sentence

def verb_forms(verb, pron):
    if verb == 'lire':
        if (pron == 'je') or (pron == 'tu'):
            verb = 'lis'
        elif (pron == 'il') or (pron == 'elle'):
            verb = 'lit'
        elif pron == 'nous':
            verb = 'lisons'
        elif pron == 'vous':
            verb = 'lisez'
        elif pron == 'ils' or pron == 'elles':
            verb = 'lisent'
    if verb == 'dire':
        if pron == 'je' or pron == 'tu':
            verb = 'dis'
        elif pron == 'il' or pron == 'elle':
            verb = 'dit'
        elif pron == 'nous':
            verb = 'disons'
        elif pron == 'vous':
            verb = 'disez'
        elif pron == 'ils' or pron == 'elles':
            verb = 'disent'
    if verb == 'apprendre':
        if pron == 'je': 
            verb = 'apprends'
        elif pron == 'tu':
            verb = 'apprends'
        elif pron == 'il' or pron == 'elle':
            verb = 'apprend'
        elif pron == 'nous':
            verb = 'apprenons'
        elif pron == 'vous':
            verb = 'apprenez'
        elif pron == 'ils' or pron == 'elles':
            verb = 'apprennent'
    pron_verb = verb
    return pron_verb

def ce_noun(noun):
    if noun == 'livre':
        sent = 'ce' + ' ' + noun
    elif noun == 'soir':
        sent = 'cette' + ' ' + noun
    elif noun == 'lecon':
        sent = 'ce' + ' ' + noun
    elif noun == 'copine':
        sent = 'ce' + ' ' + noun
    elif noun == 'revue':
        sent = 'ce' + ' ' + noun
    elif noun == 'faculte':
        sent = 'ce' + ' ' + noun
    return sent

def positive():
    pron4 = pron()
    sentence = (pron4 + ' '+ verb_forms(verb(), pron4) + ' ' + ce_noun(noun()) + '.') 
    sentence = sentence.capitalize()
    return sentence
def verb_names(pron):
    if pron == 'je':
        verb = 'm' + "'" +'appelle'
    elif pron == 'tu':
        verb = 't'+"'"+'appelles'
    elif pron == 'il':
        verb = 's'+"'"+'appelle'
    elif pron == 'elle':
        verb = 's'+"'"+'appelle'
    elif pron == 'nous':
        verb = 'nous appelons'
    elif pron == 'vous':
        verb = 'vous appelez'
    elif pron == 'ils':
        verb = 's'+"'"+'appellent'
    elif pron == 'elles':
        verb = 's'+"'"+'appellent'
    return verb

def negative():
    pron2 = pron()
    sent = pron2 + ' ne ' + verb_names(pron2) + ' pas ' + name().title() + '.'
    sent = sent.capitalize()
    return sent
def imperative():
    sent = imper()+ ' ' + ce_noun(noun()) + '!'
    sent = sent.capitalize()
    return sent

def pron_verb_cond(pron, verb):
    if verb == 'etre':
        if pron == 'je':
            verb = 'j' + "'" + 'etais'
        elif pron == 'tu':
            verb = 'etais'
        elif pron == 'il' or pron == 'elle':
            verb = 'etait'
        elif pron == 'nous':
            verb = 'etions'
        elif pron == 'vous':
            verb = 'etiez'
        elif pron == 'ils' or pron == 'elles':
            verb = 'etaient'
    if verb == 'parler':
        if pron == 'je' or pron == 'tu':
            verb = 'parlais'
        elif pron == 'il' or pron == 'elle':
            verb = 'parlait'
        elif pron == 'nous':
            verb = 'parlions'
        elif pron == 'vous':
            verb = 'parliez'
        elif pron == 'ils' or pron == 'elles':
            verb = 'parlaient'
    if verb == 'finir':
        if pron == 'je' or pron == 'tu':
            verb = 'finissais'
        elif pron == 'il' or pron == 'elle':
            verb = 'finissait'
        elif pron == 'nous':
            verb = 'finissins'
        elif pron == 'vous':
            verb = 'finissiez'
        elif pron == 'ils' or pron == 'elles':
            verb = 'finissaient'
    return (verb)

def conditional():
    pron3 = pron()
    sent = (pron3 + ' le ' + verb_forms(verb(), pron3) + ', si ' + pron3 + ' ' + pron_verb_cond(pron3, verb_cond()) + ' ' + ce_noun(noun()) + '.')
    sent = sent.capitalize()
    return sent

def shuffled(array):
    indices = list(range(len(array)))
    random.shuffle(indices)
    for i in indices:
        yield array[i]

def printing():
    spisok = [conditional(), positive(), negative(), question(), imperative()]
    for item in shuffled(spisok):
        print (item)

printing()
