# (EXPERIMENTAL, AND EXTREMELY STUPID)
# Adding support for playing videos post download.
# Uses very stupid methods for using VLC for this.

from subprocess import run
import os

def PLAY(Path):
	# Determining the OS first.
	if os.name=='nt':
		os.startfile(Path)
	elif os.name=='posix':
		run('vlc '+Path,shell=True)