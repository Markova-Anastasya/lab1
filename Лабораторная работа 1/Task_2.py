# TODO Найдите количество книг, которое можно разместить на дискете

info_volume = 1.44
number_of_pages = 100
lines_per_page = 50
symbols_per_line = 25
one_symbol = 4

volume_per_book = one_symbol * symbols_per_line * lines_per_page * number_of_pages
number_of_books = info_volume * 1024 * 1024 // volume_per_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
