# Régénère www/index.html à partir de la page publiée (a-table.html).
import sys
src=sys.argv[1] if len(sys.argv)>1 else 'a-table.html'
s=open(src,encoding='utf8').read()
head='<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="theme-color" content="#1B6B55">\n'
i=s.index('</style>')+len('</style>')
j=i-len('</style>')
out=head+s[:j]+'\n.shell{padding-top:calc(14px + env(safe-area-inset-top,0px))}\n</style>\n</head>\n<body>'+s[i:]+'\n</body>\n</html>\n'
open('www/index.html','w',encoding='utf8').write(out)
