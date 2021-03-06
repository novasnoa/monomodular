
"""
Base_Map.py

Created by amounra on 2013-07-18.
"""


"""This variable determines whether or not the script automatically arms an instruments track for recording when it is selected"""
AUTO_ARM_SELECTED = True

"""This variable determines whether the octave shift for the note offset controls work as momentary or toggle"""
OFFSET_SHIFT_IS_MOMENTARY = False

"""The following variables contain color values for different operational mode indicators"""
"""[blackkey, whitekey]"""
KEYCOLORS = [45, 37, 53, 5]
DRUMCOLORS = [45, 37, 53, 5]

CHAN_SELECT = 7

OFFSET = 6
SHIFT_OFFSET = 13
VERTOFFSET = 7
MIDIMODE = 14
USERMODE = 13
SCALEOFFSET = 5
SPLITMODE = 1
OVERDUB = 5
RECORD = 6
NEW = 2
LENGTH = 3

"""[non-banked, banked]"""
SESSION_NAV = [127, 3]
DEVICE_NAV = 5
BANK_NAV = 4
CHAIN_NAV = 11
DEVICE_LAYER = 12


TRACK_MUTE = 2
TRACK_ARM = 5
TRACK_SOLO = 3
TRACK_STOP = 127

STOP_CLIP = 127
CLIP_TRG_PLAY = 13
CLIP_TRG_REC = 11
CLIP_STOP = 1
CLIP_STARTED = 6
CLIP_RECORDING = 5
ZOOM_STOPPED = 127
ZOOM_PLAYING = 6
ZOOM_SELECTED = 8


"""The scale modes and drumpads use the following note maps"""

NOTES = [24, 25, 26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
#DRUMNOTES = [48, 49, 50, 51, 64, 65, 66, 67, 44, 45, 46, 47, 60, 61, 62, 63, 40, 41, 42, 43, 56, 57, 58, 59, 36, 37, 38, 39, 52, 53, 54, 55]
DRUMNOTES = [44, 45, 46, 47, 60, 61, 62, 63, 40, 41, 42, 43, 56, 57, 58, 59, 36, 37, 38, 39, 52, 53, 54, 55, 32, 33, 34, 35, 48, 49, 50, 51, 12, 13, 14, 15, 28, 29, 30, 31, 8, 9, 10, 11, 24, 25, 26, 27, 4, 5, 6, 7, 20, 21, 22, 23, 0, 1, 2, 3, 16, 17, 18, 19]
DRUMNOTES = [28, 29, 30, 31, 60, 61, 62, 63, 24, 25, 26, 27, 56, 57, 58, 59, 20, 21, 22, 23, 52, 53, 54, 55, 16, 17, 18, 19, 48, 49, 50, 51, 12, 13, 14, 15, 44, 45, 46, 47, 8, 9, 10, 11, 40, 41, 42, 43, 4, 5, 6, 7, 36, 37, 38, 39, 0, 1, 2, 3, 32, 33, 34, 35]

SCALENOTES = [36, 38, 40, 41, 43, 45, 47, 48, 24, 26, 28, 29, 31, 33, 35, 36, 12, 14, 16, 17, 19, 21, 23, 24, 0, 2, 4, 5, 7, 9, 11, 12]
WHITEKEYS = [0, 2, 4, 5, 7, 9, 11, 12]

"""These are the scales we have available.  You can freely add your own scales to this """
SCALES = 	{'Mod':[0,1,2,3,4,5,6,7,8,9,10,11],
			'Session':[0,1,2,3,4,5,6,7,8,9,10,11],
			'Auto':[0,1,2,3,4,5,6,7,8,9,10,11],
			'Chromatic':[0,1,2,3,4,5,6,7,8,9,10,11],
			'DrumPad':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
			'Major':[0,2,4,5,7,9,11],
			'Minor':[0,2,3,5,7,8,10],
			'Dorian':[0,2,3,5,7,9,10],
			'Mixolydian':[0,2,4,5,7,9,10],
			'Lydian':[0,2,4,6,7,9,11],
			'Phrygian':[0,1,3,5,7,8,10],
			'Locrian':[0,1,3,4,7,8,10],
			'Diminished':[0,1,3,4,6,7,9,10],
			'Whole-half':[0,2,3,5,6,8,9,11],
			'Whole Tone':[0,2,4,6,8,10],
			'Minor Blues':[0,3,5,6,7,10],
			'Minor Pentatonic':[0,3,5,7,10],
			'Major Pentatonic':[0,2,4,7,9],
			'Harmonic Minor':[0,2,3,5,7,8,11],
			'Melodic Minor':[0,2,3,5,7,9,11],
			'Dominant Sus':[0,2,5,7,9,10],
			'Super Locrian':[0,1,3,4,6,8,10],
			'Neopolitan Minor':[0,1,3,5,7,8,11],
			'Neopolitan Major':[0,1,3,5,7,9,11],
			'Enigmatic Minor':[0,1,3,6,7,10,11],
			'Enigmatic':[0,1,4,6,8,10,11],
			'Composite':[0,1,4,6,7,8,11],
			'Bebop Locrian':[0,2,3,5,6,8,10,11],
			'Bebop Dominant':[0,2,4,5,7,9,10,11],
			'Bebop Major':[0,2,4,5,7,8,9,11],
			'Bhairav':[0,1,4,5,7,8,11],
			'Hungarian Minor':[0,2,3,6,7,8,11],
			'Minor Gypsy':[0,1,4,5,7,8,10],
			'Persian':[0,1,4,5,6,8,11],
			'Hirojoshi':[0,2,3,7,8],
			'In-Sen':[0,1,5,7,10],
			'Iwato':[0,1,5,6,10],
			'Kumoi':[0,2,3,7,9],
			'Pelog':[0,1,3,4,7,8],
			'Spanish':[0,1,3,4,5,6,8,10]
			}

SCALEABBREVS = {'Mod':'E3', 'Session':'-S','Auto':'-A','Chromatic':'12','DrumPad':'-D','Major':'M-','Minor':'m-','Dorian':'II','Mixolydian':'V',
			'Lydian':'IV','Phrygian':'IH','Locrian':'VH','Diminished':'d-','Whole-half':'Wh','Whole Tone':'WT','Minor Blues':'mB',
			'Minor Pentatonic':'mP','Major Pentatonic':'MP','Harmonic Minor':'mH','Melodic Minor':'mM','Dominant Sus':'D+','Super Locrian':'SL',
			'Neopolitan Minor':'mN','Neopolitan Major':'MN','Enigmatic Minor':'mE','Enigmatic':'ME','Composite':'Cp','Bebop Locrian':'lB',
			'Bebop Dominant':'DB','Bebop Major':'MB','Bhairav':'Bv','Hungarian Minor':'mH','Minor Gypsy':'mG','Persian':'Pr',
			'Hirojoshi':'Hr','In-Sen':'IS','Iwato':'Iw','Kumoi':'Km','Pelog':'Pg','Spanish':'Sp'}


"""Any scale names in this array will automatically use SplitMode when chosen, regardless of the SplitSwitch for the individual MIDI Channel"""
SPLIT_SCALES = []

"""It is possible to create a custom list of scales to be used by the script.  For instance, the list below would include major, minor, auto, drumpad, and chromatic scales, in that order."""
#SCALENAMES = ['Major', 'Minor', 'Auto', 'DrumPad', 'Chromatic']

"""This is the default scale used by Auto when something other than a drumrack is detected for the selected track"""
DEFAULT_AUTO_SCALE = 'Major'

"""This is the default Vertical Offset for any scale other than DrumPad """
DEFAULT_VERTOFFSET = 4

"""This is the default NoteOffset, aka RootNote, used for scales other than DrumPad"""
DEFAULT_OFFSET = 48

"""This is the default NoteOffset, aka RootNote, used for the DrumPad scale;  it is a multiple of 4, so an offset of 4 is actually a RootNote of 16"""
DEFAULT_DRUMOFFSET = 9

"""This is the default Scale used for all MIDI Channels"""
DEFAULT_SCALE = 'Auto'

"""This is the default SplitMode used for all MIDI Channels"""
DEFAULT_SPLIT = False


