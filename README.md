# MusicInterpreter
Python command line single-file notation interpreter. 

# Directions:
To use: Run the file. Command line flags include "--PRINT_MORE"... and that's it.
Not to use: Don't run the file.

# _________Guide_________:  #also attached in python
#	Note Types (persistent):
	    / : half
	    > : quarter
	    < : eighth
	    - : sixteenth
#	Key Signature Changes - Syntax:
	    @(\[individual notes here, no delimiter]), use before notes
#	Octave Changes - Persistent:
   		Digits 1-6 are for available octaves. May vary depending on the medium being exported to. Modify at your own discretion.
#	Non-persistent symbols:
	    = : mark a chord (use before a note)
	    n : natural (use before)
#	Special:
	    0 : non persistent REST (how would it even be persistent??)
	    . : end the music right there.
	    | : does nothing, just denotes line between bars
