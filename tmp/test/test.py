import nucleotide

c1 = nucleotide.catalog.Catalog()
c2 = nucleotide.catalog.Catalog()
c3 = nucleotide.catalog.Catalog()
c4 = nucleotide.catalog.Catalog()

print "----------"
print __file__ + ' - ' +str( c1 )
print __file__ + ' - ' +str( c2.get() )
print __file__ + ' - ' +str( c3.get()[0].get() )
print "----------"



opt = nucleotide.options.Options()

import json

#print __file__ + ' - get_this: ' +str( opt.get_this() )
print __file__ + ' - get_represents: ' +json.dumps( opt.get_represents(), indent=4 , sort_keys=True )
