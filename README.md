LetterCompiler

Dieses Programm ist ein einfaches Python-Skript, das reguläre Ausdrücke (Regex) verwendet, um bestimmte Buchstaben in einem Text zu finden. Die Funktion LetterCompiler verwendet die re-Bibliothek, 
um alle Instanzen zu finden, bei denen die Buchstaben 'a', 'b', oder 'c' gefolgt von einem beliebigen Zeichen im übergebenen Text (txt) vorkommen.
Die Zeile result = re.findall(r'([a-c]).', txt) definiert ein Regex-Muster, das die genannten Buchstaben sucht, wobei jeder dieser Buchstaben 
von irgendeinem anderen Zeichen gefolgt sein muss (ausgedrückt durch den Punkt . im Regex). Die Klammern ([a-c]) bilden eine Erfassungsgruppe, die bedeutet, 
dass nur die Buchstaben 'a', 'b' oder 'c' zurückgegeben werden, nicht das Zeichen, das auf sie folgt.
Wenn das Skript ausgeführt wird, sucht es im vorgegebenen Text my_txt nach diesem Muster und gibt alle gefundenen Instanzen in einer Liste zurück. 
Im gegebenen Beispieltext würde die Ausgabe ['b', 'a'] sein, da "b" gefolgt von einem Leerzeichen und "a" gefolgt von einem "r" im Satz "The best preparation..." vorkommen.
