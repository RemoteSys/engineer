
mm = {'Côte':"Cote D'Ivoire","Republic Of Korea":'Korea Dem' ,'Micronesia':'Micronesia',\
     'Northern Mariana Islands':'Northern Mariana Islands', 'Saint Martin':'Saint Martin',\
     'Sint Maarten':'Sint Maarten', 'United Kingdom':'United Kingdom',\
      'Wallis And Futuna':'Wallis And Futuna','Palestine':'other','Other':'other',\
     'Macao Sar':'other','Guernsey':'other','Hong Kong':'other',\
      'Channel Islands':'other','Pitcairn Islands':'other','Palestinian':'other',\
     'Jersey':'other','Taiwan':'other','Kosovo':'other','Western Sahara':'other'}



for country in dif:
    for k,v in mm.items():
        #if re.search(fr'{k}',fr'{country}'):
        if re.search(k,country):
            #print()
            print(f'{country}:\t{k}\t{v}')
            idx = cov.Country == country
            cov.loc[idx,'Country'] = v
            
            idx = pop.Country == country
            pop.loc[idx,'Country'] = v
