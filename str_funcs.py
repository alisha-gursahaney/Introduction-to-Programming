# Ben Tyeryar and Alisha Gursahaney (bat8hgp and amg9zd)
def ellipsis(s):
    e = s[0:2]+'...'+s[len(s)-2:len(s)]
    return e


def eighteen(s):
    e = s[0:1]+str((len(s)-2))+s[len(s)-1:len(s)]
    return e


def allit(s, t):
    s = s.lower()
    t = t.lower()
    a = s[0:1] == t[0:1]
    return a


def between(s, t):
    if s.find(t) == -1:
        return '""'
    else:
        i = s.find(t)
    #  m = s[i+len(t)-1:len(s)]
        j = s.find(t, i, len(s))
        s = s[len(t)-1:j+1]
        return s
# we did our best, might come back to it if we have time


def rbetween(s, t):
    return


def rand_between(s, t):
    return


def temperature(s):
    t = s.find('lrg">')
    u = s.find('&deg')
    m = s[t+5:u]
    return m


def unhide(s):
    s = s.lower()
    s = s.replace(' at ', '@')
    s = s.replace(' (at) ', '@')
    s = s.replace(' dot ', '.')
    s = s.replace(' (dot) ', '.')
    return s


def vowel_confusion(s):
    s = s.replace('i', 'ÃŸ')
    s = s.replace('e', 'i')
    s = s.replace('ÃŸ', 'e')
    s = s.replace('I', 'Î±')
    s = s.replace('E', 'I')
    s = s.replace('Î±', 'E')
    return s


print(ellipsis('computer'))
print(eighteen('internationalization'))
print(allit('hi', 'hello'))
print(between("peripatetics", "p"))
print(temperature('<p class="myforecast-current">Fair</p>n<p class="myforecast-current-lrg">103&deg;F</p><p class="myforecast-current-sm">28&deg;C</p>'))
print(unhide('mst3k (at) virginia (dot) edu'))
print(vowel_confusion("I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, 'How long have you been singing, Mademoiselle?'"))
