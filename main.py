#Write to st
st="5dnec|ngneeg|f6d5d6d5ne6c5c6c."

import sys

PROGRAM_FLAGS = {"--PRINT_MORE":False}

if len(sys.argv) > 0:
    for arg in sys.argv[1:]:
        if arg in list(PROGRAM_FLAGS.keys()):
            PROGRAM_FLAGS[arg] = not PROGRAM_FLAGS[arg]


keySignature = ["a","b","d","e","g"]

MODIFIER_CHARS = [">","<","n","|","/","-","=","1","2","3","4","5","6","@","(",")"]

def isModifierNote(note):
	return (note in MODIFIER_CHARS);

end = ""
chord = ""
ignre = False;
for p in st: #scans for chord notes
	if (ignre):
		if not (isModifierNote(p)):
			ignre = False;
		chord += p 
		continue;
	if (p=="="):
		#take the spot of the earlier note as it is meant to be...
		#... played simultaneously.
		chord = chord[:len(chord)-1]
		ignre = True
		continue;
	if (p=="."):
		chord += "."
		break;
	verr = False;
	try:
		int(p)
	except ValueError:
		verr = True;
	#octave signatures will be excluded
	if (isModifierNote(p)):
		if (verr and p != "n"):
			chord += p
		continue;
	chord += "0";

if (PROGRAM_FLAGS["--PRINT_MORE"]):
    print("Input string:",end="\n\t")
    print(st)
    print("Evaluated chords:",end="\n\t")
    print(chord)
    print()

accountrement = 0;
octave = 4; noteType = "quarter"; markedAsChord = False;
keySignChange = False;
for i in st:
    if i == ".":
        break;

    natural = False; modifier = isModifierNote(i);
    #| denotes measure, n denotes natural
    if i == "|" or i == "n" or markedAsChord: 
        accountrement+=1;
        if not (isModifierNote(i)):
            markedAsChord= False;
        continue;

    # i == ")" will be handled later
    if keySignChange and not modifier: 
        keySignature.append(i)
        continue;

    #over here, accountrement is one index behind.
    if (st[accountrement] == "n"): 
        natural = True;
    match i:
        case ">":
            modifier = True;
            noteType = "quarter"
        case "<":
            modifier = True;
            noteType = "eighth"
        case "/":
            modifier = True;
            noteType = "half"
        case "-":
            modifier = True;
            noteType = "sixteenth"
        case "=":
            modifier = True;
            markedAsChord = True;
        case "(":
            modifier = True;
            if (accountrement -1 >=0):
                if (st[accountrement-1] == "@"):
                    keySignChange = True;
                    keySignature = []
        case ")":
            modifier = True;
            keySignChange = False;
        case "1":
            octave = 1;
            modifier=True;
        case "2":
            octave = 2;
            modifier=True;
        case "3":
            octave = 3;
            modifier=True;
        case "4":
            octave = 4;
            modifier=True;
        case "5":
            octave = 5;
            modifier=True;
        case "6":
            octave = 6;
            modifier=True;
        case "a":
            if (natural or not (i in keySignature)):
                end+= f"a_{{{octave}}}"
            else:
                end += f"a_{{{octave}f}}"
        case "b":
            if (natural or not (i in keySignature)):
                end+= f"b_{{{octave}}}"
            else:
                end += f"b_{{{octave}f}}"
        case "c":
            end += f"c_{{{octave}}}"
        case "d" : 
            if (natural or not (i in keySignature)):
                end+= f"d_{{{octave}}}"
            else:
                end += f"d_{{{octave}f}}"
        case "e":
            if (natural or not (i in keySignature)):
                end+= f"e_{{{octave}}}"
            else:
                end += f"e_{{{octave}f}}"
        case "f":
            end+= f"f_{{{octave}}}"
        case "g":
            if (natural or not (i in keySignature)):
                end+= f"g_{{{octave}}}"
            else:
                end += f"g_{{{octave}f}}"
        case "0":
            end+="0"
    if not modifier:
        match (noteType):
            case "quarter":
                end += ",0,0,0,"
            case "eighth":
                end += ",0,"
            case "half":
                end += ","
                for _ in range(3):
                    match i:
                        case "a":
                            if (natural):
                                end+= f"a_{{{octave}}}"
                            else:
                                end += f"a_{{{octave}f}}"
                        case "b":
                            if (natural):
                                end+= f"b_{{{octave}}}"
                            else:
                                end += f"b_{{{octave}f}}"
                        case "c":
                            end+= f"c_{{{octave}}}"
                        case "d" : 
                            if (natural):
                                end+= f"d_{{{octave}}}"
                            else:
                                end += f"d_{{{octave}f}}"
                        case "e":
                            if (natural):
                                end+= f"e_{{{octave}}}"
                            else:
                                end += f"e_{{{octave}f}}"
                        case "f":
                            end += f"f_{{{octave}}}"
                        case "g":
                            if (natural):
                                end+= f"g_{{{octave}}}"
                            else:
                                end += f"g_{{{octave}f}}"
                        case _:
                            end+="0"
                    end += ","
                end += "0,0,0,"
            case _:
                end += ","
    if (accountrement < len(end)):
        if end[-1] == "," and st[accountrement+1] == ".":
            end = end[:len(end)-1]
    accountrement += 1;

resolvedST = end[:] #p
end = ""
keySignature = ["a","b","d","e","g"]

#Chord note interpreter
accountrement = 0;
octave = 4; noteType = "quarter"; markedAsChord = False;
for i in chord:
    if i == ".":
        break;

    natural = False; modifier = isModifierNote(i);
    #| denotes measure, n denotes natural
    if i == "|" or i == "n" or markedAsChord: 
        accountrement+=1;
        if not (isModifierNote(i)):
            markedAsChord= False;
        continue;

    # i == ")" will be handled later
    if keySignChange and not modifier: 
        keySignature.append(i)
        continue;

    #over here, accountrement is one index behind.
    if (chord[accountrement] == "n"): 
        natural = True;
    match i:
        case ">":
            modifier = True;
            noteType = "quarter"
        case "<":
            modifier = True;
            noteType = "eighth"
        case "/":
            modifier = True;
            noteType = "half"
        case "-":
            modifier = True;
            noteType = "sixteenth"
        case "=":
            modifier = True;
            markedAsChord = True;
        case "(":
            modifier = True;
            if (accountrement - 1 >=0):
                if (chord[accountrement-1] == "@"):
                    keySignChange = True;
                    keySignature = []
        case ")":
            modifier = True;
            keySignChange = False;
        case "1":
            octave = 1;
            modifier=True;
        case "2":
            octave = 2;
            modifier=True;
        case "3":
            octave = 3;
            modifier=True;
        case "4":
            octave = 4;
            modifier=True;
        case "5":
            octave = 5;
            modifier=True;
        case "6":
            octave = 6;
            modifier=True;
        case "a":
            if (natural or not (i in keySignature)):
                end+= f"a_{{{octave}}}"
            else:
                end += f"a_{{{octave}f}}"
        case "b":
            if (natural or not (i in keySignature)):
                end+= f"b_{{{octave}}}"
            else:
                end += f"b_{{{octave}f}}"
        case "c":
            end += f"c_{{{octave}}}" #h
        case "d" : 
            if (natural or not (i in keySignature)):
                end+= f"d_{{{octave}}}"
            else:
                end += f"d_{{{octave}f}}"
        case "e":
            if (natural or not (i in keySignature)):
                end+= f"e_{{{octave}}}"
            else:
                end += f"e_{{{octave}f}}"
        case "f":
            end+= f"f_{{{octave}}}"
        case "g":
            if (natural or not (i in keySignature)):
                end+= f"g_{{{octave}}}"
            else:
                end += f"g_{{{octave}f}}"
        case "0":
            end+="0"
    if not modifier:
        match (noteType):
            case "quarter":
                end += ",0,0,0,"
            case "eighth":
                end += ",0,"
            case "half":
                end += ","
                for _ in range(3):
                    match i:
                        case "a":
                            if (natural):
                                end+= f"a_{{{octave}}}"
                            else:
                                end += f"a_{{{octave}f}}"
                        case "b":
                            if (natural):
                                end+= f"b_{{{octave}}}"
                            else:
                                end += f"b_{{{octave}f}}"
                        case "c":
                            end+= f"c_{{{octave}}}"
                        case "d" : # o
                            if (natural):
                                end+= f"d_{{{octave}}}"
                            else:
                                end += f"d_{{{octave}f}}"
                        case "e":
                            if (natural):
                                end+= f"e_{{{octave}}}"
                            else:
                                end += f"e_{{{octave}f}}"
                        case "f":
                            end += f"f_{{{octave}}}"
                        case "g":
                            if (natural):
                                end+= f"g_{{{octave}}}"
                            else:
                                end += f"g_{{{octave}f}}"
                        case _:
                            end+="0"
                    end += ","# t
                end += "0,0,0,"
            case _:
                end += ","
    if (accountrement < len(end)):
        if end[-1] == "," and chord[accountrement+1] == ".":
            end = end[:len(end)-1]
    accountrement += 1;# o

print("__________________\n Main Part: \n__________________\n")
print(resolvedST)
print("\n__________________\n Chord Part: \n__________________\n")
print(end) #n
