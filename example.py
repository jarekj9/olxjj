from olxjj import OLXJJ

url = "https://www.olx.pl/nieruchomosci/mieszkania/bydgoszcz/?search%5Bfilter_float_price%3Afrom%5D=250000&search%5Bfilter_float_price%3Ato%5D=330000&search%5Bfilter_enum_floor_select%5D%5B0%5D=floor_1&search%5Bfilter_enum_floor_select%5D%5B1%5D=floor_2&search%5Bfilter_enum_floor_select%5D%5B2%5D=floor_3&search%5Bfilter_enum_floor_select%5D%5B3%5D=floor_4&search%5Bfilter_enum_floor_select%5D%5B4%5D=floor_5&search%5Bfilter_enum_floor_select%5D%5B5%5D=floor_6&search%5Bfilter_enum_floor_select%5D%5B6%5D=floor_7&search%5Bfilter_enum_floor_select%5D%5B7%5D=floor_8&search%5Bfilter_enum_floor_select%5D%5B8%5D=floor_9&search%5Bfilter_enum_floor_select%5D%5B9%5D=floor_10&search%5Bfilter_enum_floor_select%5D%5B10%5D=floor_11&search%5Bfilter_enum_builttype%5D%5B0%5D=blok&search%5Bfilter_enum_builttype%5D%5B1%5D=apartamentowiec&search%5Bfilter_float_m%3Afrom%5D=45&search%5Bfilter_float_m%3Ato%5D=60&search%5Bfilter_enum_rooms%5D%5B0%5D=three"	
words=['loggia','logia','winda']
olx=OLXJJ(url)

#print(olx.get_links_with_word("and",words))
print(olx.get_links_with_word("or",words))

	
