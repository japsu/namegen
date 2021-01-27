# 5 minute name generator hack

This might actually produce something usable:

* `pattern_based.py`: Give it patterns like `KATAKAN` (tailored for the Kaamni people of the Kalnemaar RPG world)

These are failed experiments for inspiration at most:

* `lame_heuristic.py`: No more than 2 same characters and 3 characters of the same class in a row
* `sprinkle_consonants.py`: First pick the vowels, then sprinkle consonants among them

## Example

    $ python3 pattern_based.py
    Nuust Sumt
    Aan Niir
    Loor Kiter
    Teelfa Neef
    Tiilsu Seen
    Noor Fiin
    Ooku Kiluf
    Tiis Fumn
    Neek Soter
    Aafo Liis

    $ python3 lame_heuristic.py
    Nomuoa Ekettua
    Tkiuok Noteuu
    Asoiedsa Iunt
    Admaooloa Akio
    Miaeviuet Dotooltoiel
    Uiavuuokst Uuokoouks
    Audoeteid Oast
    Touko Naunussoloo
    Ooivnkumos Meoka
    Otete Iokuaa

    $ python3 sprinkle_consonants.py
    Naako Uotiikubu
    Akeevub Oukota
    Notonasaao Uokaakut
    Tokiutet Aibiko
    Kotaoiose Kanaki
    Ukatavu Aaauvitev
    Tekikov Teaba
    Abasuuatev Taauuvatob
    Uetutas Ousaav
    Keasov Vusisok
