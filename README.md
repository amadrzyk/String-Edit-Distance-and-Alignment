# String Edit Distance and Alignment

This program computes the number of edits required to convert one string to another. This can be useful when comparing DNA sequences:
```
optimal alignment:

ACATACGATACAGACGATCGGCTAGAATCCACCAGCTACAGCTAGT--C--G-ATACA-G
|||||||||||||| |   | |||||||||||||||||||||||||  |  | ||  | |
ACATACGATACAGA-G---G-CTAGAATCCACCAGCTACAGCTAGTTACAAGGATCGATG

CACGAATCGCTAAACAG-CTCGATCGATCGCTAGCTGATCGATACTTACCACAGCTGATC
|||||| |  ||||||| || | |   ||||||||||||||||||||||||||||| |
CACGAA-C--TAAACAGACTAG-TTTCTCGCTAGCTGATCGATACTTACCACAGCTAAAA

GATGCTATT-TAGCTAGCTCGTAGT-A
||||||||| | |  ||||  |  | |
GATGCTATTATTG-GAGCTAATTTTTA

edit distance = 34
```

It can also be useful when comparing different languages, to extract similarities:
```
optimal alignment:

No puedo reco-rdar si llor--e Cuando lei acerca de su novia
  |    ||  ||     |      |  || |   |  |||     | | | ||   | |
Eu --nao --consigo lembrar se eu cho-rei ---Quando eu --li-

que dejaba viuda Pero -a---lgo me toco muy profundamente El
     | |  |||| || |  | |   ||||||| | |  | |||||||||||||||  |
-sobre a-- viuva dele Mas algo me comoveu- profundamente No

dia ---que la musica mur-io
||||   |||| |||||||||| |
dia em que -a musica morreu

edit distance = 70
```

# Usage
To run this program, simply run `python editDist.py file1.txt file2.txt` in the terminal. The program will still work if input is on several lines.