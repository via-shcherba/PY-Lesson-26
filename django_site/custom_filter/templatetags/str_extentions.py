from django import template

register = template.Library()

def capitalize(inputstr):
    return inputstr.capitalize()

def superoutput(inputstr):
    return ''.join([inputstr[i].upper() if i % 2 == 0 else inputstr[i] for i in range(len(inputstr))])

register.filter('capitalize', capitalize)
register.filter('sup', superoutput)