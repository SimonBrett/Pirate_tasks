#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on September 21, 2020, at 10:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'pirateTrial'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'condition': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Daniel\\Documents\\GitHub\\Pirate_tasks\\pirateTrial.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.INFO)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruct1"
Instruct1Clock = core.Clock()
#Store images and initialise feedback display
imagePath = "stimuli/" 
imageVariable = None 
textFeedback = None # Need this to initialise the text feedback display
fdbck_winText = "Well done you chose correctly!"
fdbck_loseText = "Better luck next time!"
fdbck_tooslowText = "Oops, you were too slow. Please respond quicker next time."
soundFeedback = None
zero = [0] 
one = [1]

from numpy import random as rand #randomise lists

# Set up selection positions
left_pos = (-0.52, -0.32)
right_pos = (0.52, -0.32)
Instruct_1_text = visual.TextStim(win=win, name='Instruct_1_text',
    text='In this game, there are two pirates, a green and a blue one, on different islands. Each pirate puts a flag up to tell you how many coins they have in their treasure chest.\n\n',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instruct_1_image = visual.ImageStim(
    win=win,
    name='instruct_1_image', units='norm', 
    image='stimuli/piratetask_instruct.bmp', mask=None,
    ori=0, pos=(0., -0.2), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_3 = keyboard.Keyboard()
counterbalancing = int(expInfo['condition'])

if counterbalancing == 1:
    
    # Green or blue weighting in fam trials (cond 1)
    trial_list_s = zero*8 + one*2
    
    # Correct hint chance for fam trials (cond 1)
    cb_hint_chance = 0.8
    
    # Hint chance for main trials
    cb_hint_chance_1 = 0.75
    cb_hint_chance_2 = 0.15
    
elif counterbalancing == 2:

    # Green or blue weighting in fam trials (cond 2)
    trial_list_s = zero*2 + one*8
    # Correct hint chance for fam trials (cond 1)
    cb_hint_chance = 0.8
    
    # Hint chance for main trials
    cb_hint_chance_1 = 0.75
    cb_hint_chance_2 = 0.15

elif counterbalancing == 3:
    
    # Green or blue weighting in fam trials (cond 1)
    trial_list_s = zero*8 + one*2
    cb_hint_chance = 0.8
    
    # Hint chance for main trials
    cb_hint_chance_1 = 0.25
    cb_hint_chance_2 = 0.85
    
elif counterbalancing == 4:
    # Green or blue weighting in fam trials (cond 2)
    trial_list_s = zero*2 + one*8
    cb_hint_chance = 0.8
    
    # Hint chance for main trials
    cb_hint_chance_1 = 0.25
    cb_hint_chance_2 = 0.85
elif counterbalancing == 5:
    # Green or blue weighting in fam trials (cond 1)
    trial_list_s = zero*8 + one*2
    # Correct hint chance for fam trials (cond 1)
    cb_hint_chance = 0.2
    cb_hint_chance_1 = 0.75
    cb_hint_chance_2 = 0.15

elif counterbalancing == 6:
    # Green or blue weighting in fam trials (cond 2)
    trial_list_s = zero*2 + one*8
    cb_hint_chance = 0.2
    cb_hint_chance_1 = 0.75
    cb_hint_chance_2 = 0.15

elif counterbalancing == 7:
    # Green or blue weighting in fam trials (cond 1)
    trial_list_s = zero*8 + one*2
    cb_hint_chance = 0.2
    cb_hint_chance_1 = 0.25
    cb_hint_chance_2 = 0.85
    
elif counterbalancing == 8:
    # Green or blue weighting in fam trials (cond 2)
    trial_list_s = zero*2 + one*8
    cb_hint_chance = 0.2
    cb_hint_chance_1 = 0.25
    cb_hint_chance_2 = 0.85
spacebar_text = visual.TextStim(win=win, name='spacebar_text',
    text='Press the Space Bar to Continue ',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Instruct2"
Instruct2Clock = core.Clock()
instruct_2_text = visual.TextStim(win=win, name='instruct_2_text',
    text='But only one of the pirates is telling the truth! The other pirate is trying to trick you, as they actually have nothing in their treasure chest. It could be the green or the blue pirate who is tricking you.\n\nTo help you along, the computer will give you a clue about where you can find the treasure; one of the treasure chests will glow.',
    font='Arial',
    units='norm', pos=(0, 0.6), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruct_2_image = visual.ImageStim(
    win=win,
    name='instruct_2_image', units='norm', 
    image='stimuli/hint_instruct.bmp', mask=None,
    ori=0, pos=(0, -0.3), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_4 = keyboard.Keyboard()
spacebar_text_2 = visual.TextStim(win=win, name='spacebar_text_2',
    text='Press the Space Bar to Continue ',
    font='Arial',
    units='norm', pos=(0, -0.9), height=0.08, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Instruct3"
Instruct3Clock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='You need to decide whether the clue - the glowing treasure chest - is helpful or unhelpful\n\nThe pirate who is telling the truth will open their chest to show you their coins. Here are examples of both pirates showing their coins.\n\n',
    font='Arial',
    units='norm', pos=(0, 0.4), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruct_image_3 = visual.ImageStim(
    win=win,
    name='instruct_image_3', units='norm', 
    image='stimuli/bluewin_instruct.bmp', mask=None,
    ori=0, pos=(-0.4, -0.3), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instruct_image_4 = visual.ImageStim(
    win=win,
    name='instruct_image_4', units='norm', 
    image='stimuli/greenwin_instruct.bmp', mask=None,
    ori=0, pos=(0.4, -0.3), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_5 = keyboard.Keyboard()
spacebar_text_3 = visual.TextStim(win=win, name='spacebar_text_3',
    text='Press the Space Bar to Continue ',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.08, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Instruct4"
Instruct4Clock = core.Clock()
Instruct_text_4 = visual.TextStim(win=win, name='Instruct_text_4',
    text="But the pirate who is tricking you *might* not always be the same. It *could* change throughout the game.\n\nLet's watch the pirates now. Let's see who has treasure in their chest and who has an empty chest, and if the clue is helpful or unhelpful.",
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
spacebar_text_4 = visual.TextStim(win=win, name='spacebar_text_4',
    text='Press the space bar to begin',
    font='Arial',
    units='norm', pos=(0, -0.8), height=0.08, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "famIntro"
famIntroClock = core.Clock()

# Initialize components for Routine "famTrial"
famTrialClock = core.Clock()
famBackground = visual.ImageStim(
    win=win,
    name='famBackground', 
    image='stimuli/piratetask.bmp', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
famHint = visual.ImageStim(
    win=win,
    name='famHint', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
famR_text = visual.TextStim(win=win, name='famR_text',
    text='default text',
    font='Arial',
    pos=(0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
famL_text = visual.TextStim(win=win, name='famL_text',
    text='default text',
    font='Arial',
    pos=(-0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
famSelect_pos = visual.Rect(
    win=win, name='famSelect_pos',
    width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
    ori=0, pos=[0,0],
    lineWidth=8, lineColor='yellow', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
famFixation = visual.TextStim(win=win, name='famFixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "famFeedback"
famFeedbackClock = core.Clock()
famImage = visual.ImageStim(
    win=win,
    name='famImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fam_Rtext_2 = visual.TextStim(win=win, name='fam_Rtext_2',
    text='default text',
    font='Arial',
    pos=(0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fam_Ltext_2 = visual.TextStim(win=win, name='fam_Ltext_2',
    text='default text',
    font='Arial',
    pos=(-0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
famfdbck_text = visual.TextStim(win=win, name='famfdbck_text',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ratioCheck"
ratioCheckClock = core.Clock()
TreasureLocation = visual.RatingScale(win=win, name='TreasureLocation', marker='slider', size=1.0, pos=[0.0, -0.4], low=0, high=10, labels=['All green', ' All blue'], scale='Was the treasure more often in the green pirate’s chest or the blue pirate’s chest? ', markerStart='5')
HelpfulHint = visual.RatingScale(win=win, name='HelpfulHint', marker='slider', size=1.0, pos=[0.0, 0.2], low=0, high=10, labels=['Always unhelpful', ' Always helpful'], scale='Was the clue more often helpful or unhelpful to find the treasure? ')
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Instruct5"
Instruct5Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You’re going to see the pirates and their chests again now. This time you have to GUESS where the treasure is each time using the clues and your knowledge of the pirates as you go. It might not be the same as you’ve just seen and it might change during the game. If you guess correctly, you will win the coins in the chest. \n\nRemember, just because a pirate says he’s got a lot of coins in his chest, it doesn’t mean he is telling the truth. also, remember, the clues may be helpful or unhelpful and might change during the game too. \n\nWhen you have won a certain amount of coins you get to move on up to the next level. \n\nIf you think the green pirate is telling the truth and has the treasure, press this button . If you think the blue pirate is telling the truth and has the treasure, press this button.\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Intro"
IntroClock = core.Clock()

# Initialize components for Routine "studyTrial"
studyTrialClock = core.Clock()
background = visual.ImageStim(
    win=win,
    name='background', 
    image='stimuli/piratetask.bmp', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
hint = visual.ImageStim(
    win=win,
    name='hint', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
R_text = visual.TextStim(win=win, name='R_text',
    text='default text',
    font='Arial',
    pos=(0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
L_text = visual.TextStim(win=win, name='L_text',
    text='default text',
    font='Arial',
    pos=(-0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "selection"
selectionClock = core.Clock()
background2 = visual.ImageStim(
    win=win,
    name='background2', 
    image='stimuli/piratetask.bmp', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
r_text = visual.TextStim(win=win, name='r_text',
    text='default text',
    font='Arial',
    pos=(0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
l_text = visual.TextStim(win=win, name='l_text',
    text='default text',
    font='Arial',
    pos=(-0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
select_frame = visual.Rect(
    win=win, name='select_frame',
    width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
    ori=0, pos=[0,0],
    lineWidth=8, lineColor='yellow', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
R_text_2 = visual.TextStim(win=win, name='R_text_2',
    text='default text',
    font='Arial',
    pos=(0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
L_text_2 = visual.TextStim(win=win, name='L_text_2',
    text='default text',
    font='Arial',
    pos=(-0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
fdbck_text = visual.TextStim(win=win, name='fdbck_text',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
feedbackFrame = visual.Rect(
    win=win, name='feedbackFrame',
    width=(0.4, 0.6)[0], height=(0.4, 0.6)[1],
    ori=0, pos=(0, -0.15),
    lineWidth=1, lineColor=[1.000,1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
feedbackFill = visual.Rect(
    win=win, name='feedbackFill',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
player_score = 0
pirate_level = 0
level_limit = 460
level_up = False

# The maximum height of the bar
# (should correspond to the height value in the feedbackFrame)
max_height = 0.6

# Proportion of the bar's height that corresponds to a single point
height_for_one_point = max_height/level_limit

# Set initial values for bar
height = player_score * height_for_one_point
width = 0.4

# This should start as the lower bound of the feedbackFrame
# i.e. if feedbackFrame height = 0.2 and y position = 0 then
# y_pos = -0.1 (y position - height/2)
y_pos = -0.45
x_pos = 0

# Timings for bar 
rect_start = 0
move_start = 2
rect_dur = 5
end_idle = 1
move_dur = rect_dur - (move_start + end_idle)

# Two options for final version:
# 1. Set duration, in which case the RoCs will be scaled by the score (variable speed/fixed duration)
# 2. Set rate of change, in which case the duration will be scaled by score (variable duration/ fixed speed)

# Currently set up as 1.

# Put variables into lists
rect_dims = [width, height]
rect_pos = [x_pos, y_pos]


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruct1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instruct1Components = [Instruct_1_text, instruct_1_image, key_resp_3, spacebar_text]
for thisComponent in Instruct1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruct1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruct1"-------
while continueRoutine:
    # get current time
    t = Instruct1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruct1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct_1_text* updates
    if Instruct_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct_1_text.frameNStart = frameN  # exact frame index
        Instruct_1_text.tStart = t  # local t and not account for scr refresh
        Instruct_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct_1_text, 'tStartRefresh')  # time at next scr refresh
        Instruct_1_text.setAutoDraw(True)
    
    # *instruct_1_image* updates
    if instruct_1_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_1_image.frameNStart = frameN  # exact frame index
        instruct_1_image.tStart = t  # local t and not account for scr refresh
        instruct_1_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_1_image, 'tStartRefresh')  # time at next scr refresh
        instruct_1_image.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spacebar_text* updates
    if spacebar_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spacebar_text.frameNStart = frameN  # exact frame index
        spacebar_text.tStart = t  # local t and not account for scr refresh
        spacebar_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spacebar_text, 'tStartRefresh')  # time at next scr refresh
        spacebar_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct1"-------
for thisComponent in Instruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct_1_text.started', Instruct_1_text.tStartRefresh)
thisExp.addData('Instruct_1_text.stopped', Instruct_1_text.tStopRefresh)
thisExp.addData('instruct_1_image.started', instruct_1_image.tStartRefresh)
thisExp.addData('instruct_1_image.stopped', instruct_1_image.tStopRefresh)
thisExp.addData('spacebar_text.started', spacebar_text.tStartRefresh)
thisExp.addData('spacebar_text.stopped', spacebar_text.tStopRefresh)
# the Routine "Instruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruct2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Instruct2Components = [instruct_2_text, instruct_2_image, key_resp_4, spacebar_text_2]
for thisComponent in Instruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruct2"-------
while continueRoutine:
    # get current time
    t = Instruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_2_text* updates
    if instruct_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_2_text.frameNStart = frameN  # exact frame index
        instruct_2_text.tStart = t  # local t and not account for scr refresh
        instruct_2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_2_text, 'tStartRefresh')  # time at next scr refresh
        instruct_2_text.setAutoDraw(True)
    
    # *instruct_2_image* updates
    if instruct_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_2_image.frameNStart = frameN  # exact frame index
        instruct_2_image.tStart = t  # local t and not account for scr refresh
        instruct_2_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_2_image, 'tStartRefresh')  # time at next scr refresh
        instruct_2_image.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spacebar_text_2* updates
    if spacebar_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spacebar_text_2.frameNStart = frameN  # exact frame index
        spacebar_text_2.tStart = t  # local t and not account for scr refresh
        spacebar_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spacebar_text_2, 'tStartRefresh')  # time at next scr refresh
        spacebar_text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct2"-------
for thisComponent in Instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct_2_text.started', instruct_2_text.tStartRefresh)
thisExp.addData('instruct_2_text.stopped', instruct_2_text.tStopRefresh)
thisExp.addData('instruct_2_image.started', instruct_2_image.tStartRefresh)
thisExp.addData('instruct_2_image.stopped', instruct_2_image.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('spacebar_text_2.started', spacebar_text_2.tStartRefresh)
thisExp.addData('spacebar_text_2.stopped', spacebar_text_2.tStopRefresh)
# the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruct3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Instruct3Components = [instruct_text_3, instruct_image_3, instruct_image_4, key_resp_5, spacebar_text_3]
for thisComponent in Instruct3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruct3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruct3"-------
while continueRoutine:
    # get current time
    t = Instruct3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruct3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text_3* updates
    if instruct_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_3.frameNStart = frameN  # exact frame index
        instruct_text_3.tStart = t  # local t and not account for scr refresh
        instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
        instruct_text_3.setAutoDraw(True)
    
    # *instruct_image_3* updates
    if instruct_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_image_3.frameNStart = frameN  # exact frame index
        instruct_image_3.tStart = t  # local t and not account for scr refresh
        instruct_image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_image_3, 'tStartRefresh')  # time at next scr refresh
        instruct_image_3.setAutoDraw(True)
    
    # *instruct_image_4* updates
    if instruct_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_image_4.frameNStart = frameN  # exact frame index
        instruct_image_4.tStart = t  # local t and not account for scr refresh
        instruct_image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_image_4, 'tStartRefresh')  # time at next scr refresh
        instruct_image_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spacebar_text_3* updates
    if spacebar_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spacebar_text_3.frameNStart = frameN  # exact frame index
        spacebar_text_3.tStart = t  # local t and not account for scr refresh
        spacebar_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spacebar_text_3, 'tStartRefresh')  # time at next scr refresh
        spacebar_text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct3"-------
for thisComponent in Instruct3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct_text_3.started', instruct_text_3.tStartRefresh)
thisExp.addData('instruct_text_3.stopped', instruct_text_3.tStopRefresh)
thisExp.addData('instruct_image_3.started', instruct_image_3.tStartRefresh)
thisExp.addData('instruct_image_3.stopped', instruct_image_3.tStopRefresh)
thisExp.addData('instruct_image_4.started', instruct_image_4.tStartRefresh)
thisExp.addData('instruct_image_4.stopped', instruct_image_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('spacebar_text_3.started', spacebar_text_3.tStartRefresh)
thisExp.addData('spacebar_text_3.stopped', spacebar_text_3.tStopRefresh)
# the Routine "Instruct3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruct4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Instruct4Components = [Instruct_text_4, key_resp_6, spacebar_text_4]
for thisComponent in Instruct4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruct4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruct4"-------
while continueRoutine:
    # get current time
    t = Instruct4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruct4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct_text_4* updates
    if Instruct_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct_text_4.frameNStart = frameN  # exact frame index
        Instruct_text_4.tStart = t  # local t and not account for scr refresh
        Instruct_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct_text_4, 'tStartRefresh')  # time at next scr refresh
        Instruct_text_4.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spacebar_text_4* updates
    if spacebar_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spacebar_text_4.frameNStart = frameN  # exact frame index
        spacebar_text_4.tStart = t  # local t and not account for scr refresh
        spacebar_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spacebar_text_4, 'tStartRefresh')  # time at next scr refresh
        spacebar_text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct4"-------
for thisComponent in Instruct4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct_text_4.started', Instruct_text_4.tStartRefresh)
thisExp.addData('Instruct_text_4.stopped', Instruct_text_4.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('spacebar_text_4.started', spacebar_text_4.tStartRefresh)
thisExp.addData('spacebar_text_4.stopped', spacebar_text_4.tStopRefresh)
# the Routine "Instruct4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fam_repeat = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='fam_repeat')
thisExp.addLoop(fam_repeat)  # add the loop to the experiment
thisFam_repeat = fam_repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFam_repeat.rgb)
if thisFam_repeat != None:
    for paramName in thisFam_repeat:
        exec('{} = thisFam_repeat[paramName]'.format(paramName))

for thisFam_repeat in fam_repeat:
    currentLoop = fam_repeat
    # abbreviate parameter names if possible (e.g. rgb = thisFam_repeat.rgb)
    if thisFam_repeat != None:
        for paramName in thisFam_repeat:
            exec('{} = thisFam_repeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "famIntro"-------
    continueRoutine = True
    # update component parameters for each repeat
    rand.shuffle(trial_list_s)
    
    #overall familiarisation probability (blue win 80%)
    fam_prob_bg = trial_list_s 
    
    num_trial = len(fam_prob_bg)
    
    # reward variables
    r_val = []
    l_val = []
    
    #create reward values
    for t in range(0,num_trial):
        val = rand.randint(1,100)
        r_val.append(val)
        l_val.append(100-val)
    # keep track of which components have finished
    famIntroComponents = []
    for thisComponent in famIntroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    famIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "famIntro"-------
    while continueRoutine:
        # get current time
        t = famIntroClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=famIntroClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in famIntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "famIntro"-------
    for thisComponent in famIntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "famIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    fam_trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('famtrialList.xlsx', selection='1'),
        seed=None, name='fam_trials')
    thisExp.addLoop(fam_trials)  # add the loop to the experiment
    thisFam_trial = fam_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFam_trial.rgb)
    if thisFam_trial != None:
        for paramName in thisFam_trial:
            exec('{} = thisFam_trial[paramName]'.format(paramName))
    
    for thisFam_trial in fam_trials:
        currentLoop = fam_trials
        # abbreviate parameter names if possible (e.g. rgb = thisFam_trial.rgb)
        if thisFam_trial != None:
            for paramName in thisFam_trial:
                exec('{} = thisFam_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "famTrial"-------
        continueRoutine = True
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        trial_r_val = r_val[ currentLoop.thisN ]
        trial_l_val = l_val[ currentLoop.thisN ]
        
        # Generate uniformly distributed random number between 0 and 1
        hint_prob = rand.uniform(size = 1)
        select_prob = rand.uniform(size = 1)
        
        # Generate start times for selection window
        select_start = rand.uniform(3, 7)
        famHint_dur = 1 + select_start
        famRLtext_dur = 2 + select_start
        
        # Multiple ifs way of changing hint correct probability
        if currentLoop.thisN < 10:
            corr_hint_chance = 0.8
            
        
        corr_select_chance = 0.8
        
        # statement to define correct image for trial
        if fam_prob_bg[ currentLoop.thisN ]:
            # Determine whether the hint will be show on correct or incorrect side
            if hint_prob <= corr_hint_chance:
                imageVariable = imagePath + "Lgreenhint.bmp"
                correct_hint = 1
            else:
                imageVariable = imagePath + "Rbluehint.bmp"
                correct_hint = 0
            
            # Determine whether the selection will be correct or incorrect
            if select_prob <= corr_select_chance:
                select_pos = left_pos
                imageFeedback = imagePath + "Lgreenwin.bmp" #  then display the treasure
                textFeedback = fdbck_winText # Display positive feedback text
                soundFeedback = "stimuli/coins-drop-1.wav"
            else:
                select_pos = right_pos
                imageFeedback = imagePath + "Rbluelose.bmp"# Otherwise show the empty chest
                textFeedback = fdbck_loseText
                soundFeedback = None
        else:
            if hint_prob <= corr_hint_chance:
                imageVariable = imagePath + "Rbluehint.bmp"
                correct_hint = 1
            else:
                imageVariable = imagePath + "Lgreenhint.bmp"
                correct_hint = 0
            
            if select_prob <= corr_select_chance:
                select_pos = right_pos
                imageFeedback = imagePath + "Rbluewin.bmp" # The predefined image path is added to the file name
                textFeedback = fdbck_winText # Display positive feedback text
                soundFeedback = "stimuli/coins-drop-1.wav"
            else:
                select_pos = left_pos
                imageFeedback = imagePath + "Lgreenlose.bmp"
                textFeedback = fdbck_loseText
                soundFeedback = None 
        
        famHint.setImage(imageVariable)
        famR_text.setText(trial_r_val)
        famL_text.setText(trial_l_val)
        famSelect_pos.setPos(select_pos)
        # keep track of which components have finished
        famTrialComponents = [famBackground, famHint, famR_text, famL_text, famSelect_pos, famFixation]
        for thisComponent in famTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        famTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "famTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = famTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=famTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *famBackground* updates
            if famBackground.status == NOT_STARTED and tThisFlip >= 0.-frameTolerance:
                # keep track of start time/frame for later
                famBackground.frameNStart = frameN  # exact frame index
                famBackground.tStart = t  # local t and not account for scr refresh
                famBackground.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famBackground, 'tStartRefresh')  # time at next scr refresh
                famBackground.setAutoDraw(True)
            if famBackground.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famBackground.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    famBackground.tStop = t  # not accounting for scr refresh
                    famBackground.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famBackground, 'tStopRefresh')  # time at next scr refresh
                    famBackground.setAutoDraw(False)
            
            # *famHint* updates
            if famHint.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                famHint.frameNStart = frameN  # exact frame index
                famHint.tStart = t  # local t and not account for scr refresh
                famHint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famHint, 'tStartRefresh')  # time at next scr refresh
                famHint.setAutoDraw(True)
            if famHint.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famHint.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    famHint.tStop = t  # not accounting for scr refresh
                    famHint.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famHint, 'tStopRefresh')  # time at next scr refresh
                    famHint.setAutoDraw(False)
            
            # *famR_text* updates
            if famR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                famR_text.frameNStart = frameN  # exact frame index
                famR_text.tStart = t  # local t and not account for scr refresh
                famR_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famR_text, 'tStartRefresh')  # time at next scr refresh
                famR_text.setAutoDraw(True)
            if famR_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famR_text.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    famR_text.tStop = t  # not accounting for scr refresh
                    famR_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famR_text, 'tStopRefresh')  # time at next scr refresh
                    famR_text.setAutoDraw(False)
            
            # *famL_text* updates
            if famL_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                famL_text.frameNStart = frameN  # exact frame index
                famL_text.tStart = t  # local t and not account for scr refresh
                famL_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famL_text, 'tStartRefresh')  # time at next scr refresh
                famL_text.setAutoDraw(True)
            if famL_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famL_text.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    famL_text.tStop = t  # not accounting for scr refresh
                    famL_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famL_text, 'tStopRefresh')  # time at next scr refresh
                    famL_text.setAutoDraw(False)
            
            # *famSelect_pos* updates
            if famSelect_pos.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                famSelect_pos.frameNStart = frameN  # exact frame index
                famSelect_pos.tStart = t  # local t and not account for scr refresh
                famSelect_pos.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famSelect_pos, 'tStartRefresh')  # time at next scr refresh
                famSelect_pos.setAutoDraw(True)
            if famSelect_pos.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famSelect_pos.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    famSelect_pos.tStop = t  # not accounting for scr refresh
                    famSelect_pos.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famSelect_pos, 'tStopRefresh')  # time at next scr refresh
                    famSelect_pos.setAutoDraw(False)
            
            # *famFixation* updates
            if famFixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                famFixation.frameNStart = frameN  # exact frame index
                famFixation.tStart = t  # local t and not account for scr refresh
                famFixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famFixation, 'tStartRefresh')  # time at next scr refresh
                famFixation.setAutoDraw(True)
            if famFixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famFixation.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    famFixation.tStop = t  # not accounting for scr refresh
                    famFixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famFixation, 'tStopRefresh')  # time at next scr refresh
                    famFixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in famTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "famTrial"-------
        for thisComponent in famTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fam_trials.addData('famBackground.started', famBackground.tStartRefresh)
        fam_trials.addData('famBackground.stopped', famBackground.tStopRefresh)
        fam_trials.addData('famHint.started', famHint.tStartRefresh)
        fam_trials.addData('famHint.stopped', famHint.tStopRefresh)
        fam_trials.addData('famR_text.started', famR_text.tStartRefresh)
        fam_trials.addData('famR_text.stopped', famR_text.tStopRefresh)
        fam_trials.addData('famL_text.started', famL_text.tStartRefresh)
        fam_trials.addData('famL_text.stopped', famL_text.tStopRefresh)
        fam_trials.addData('famSelect_pos.started', famSelect_pos.tStartRefresh)
        fam_trials.addData('famSelect_pos.stopped', famSelect_pos.tStopRefresh)
        fam_trials.addData('famFixation.started', famFixation.tStartRefresh)
        fam_trials.addData('famFixation.stopped', famFixation.tStopRefresh)
        
        # ------Prepare to start Routine "famFeedback"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        famImage.setImage(imageFeedback)
        fam_Rtext_2.setText(trial_r_val)
        fam_Ltext_2.setText(trial_l_val)
        famfdbck_text.setText(textFeedback)
        # keep track of which components have finished
        famFeedbackComponents = [famImage, fam_Rtext_2, fam_Ltext_2, famfdbck_text]
        for thisComponent in famFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        famFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "famFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = famFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=famFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *famImage* updates
            if famImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                famImage.frameNStart = frameN  # exact frame index
                famImage.tStart = t  # local t and not account for scr refresh
                famImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famImage, 'tStartRefresh')  # time at next scr refresh
                famImage.setAutoDraw(True)
            if famImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famImage.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    famImage.tStop = t  # not accounting for scr refresh
                    famImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famImage, 'tStopRefresh')  # time at next scr refresh
                    famImage.setAutoDraw(False)
            
            # *fam_Rtext_2* updates
            if fam_Rtext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fam_Rtext_2.frameNStart = frameN  # exact frame index
                fam_Rtext_2.tStart = t  # local t and not account for scr refresh
                fam_Rtext_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fam_Rtext_2, 'tStartRefresh')  # time at next scr refresh
                fam_Rtext_2.setAutoDraw(True)
            if fam_Rtext_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fam_Rtext_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fam_Rtext_2.tStop = t  # not accounting for scr refresh
                    fam_Rtext_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fam_Rtext_2, 'tStopRefresh')  # time at next scr refresh
                    fam_Rtext_2.setAutoDraw(False)
            
            # *fam_Ltext_2* updates
            if fam_Ltext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fam_Ltext_2.frameNStart = frameN  # exact frame index
                fam_Ltext_2.tStart = t  # local t and not account for scr refresh
                fam_Ltext_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fam_Ltext_2, 'tStartRefresh')  # time at next scr refresh
                fam_Ltext_2.setAutoDraw(True)
            if fam_Ltext_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fam_Ltext_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fam_Ltext_2.tStop = t  # not accounting for scr refresh
                    fam_Ltext_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fam_Ltext_2, 'tStopRefresh')  # time at next scr refresh
                    fam_Ltext_2.setAutoDraw(False)
            
            # *famfdbck_text* updates
            if famfdbck_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                famfdbck_text.frameNStart = frameN  # exact frame index
                famfdbck_text.tStart = t  # local t and not account for scr refresh
                famfdbck_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(famfdbck_text, 'tStartRefresh')  # time at next scr refresh
                famfdbck_text.setAutoDraw(True)
            if famfdbck_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > famfdbck_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    famfdbck_text.tStop = t  # not accounting for scr refresh
                    famfdbck_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(famfdbck_text, 'tStopRefresh')  # time at next scr refresh
                    famfdbck_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in famFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "famFeedback"-------
        for thisComponent in famFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fam_trials.addData('famImage.started', famImage.tStartRefresh)
        fam_trials.addData('famImage.stopped', famImage.tStopRefresh)
        fam_trials.addData('fam_Rtext_2.started', fam_Rtext_2.tStartRefresh)
        fam_trials.addData('fam_Rtext_2.stopped', fam_Rtext_2.tStopRefresh)
        fam_trials.addData('fam_Ltext_2.started', fam_Ltext_2.tStartRefresh)
        fam_trials.addData('fam_Ltext_2.stopped', fam_Ltext_2.tStopRefresh)
        fam_trials.addData('famfdbck_text.started', famfdbck_text.tStartRefresh)
        fam_trials.addData('famfdbck_text.stopped', famfdbck_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'fam_trials'
    
    
    # ------Prepare to start Routine "ratioCheck"-------
    continueRoutine = True
    # update component parameters for each repeat
    TreasureLocation.reset()
    HelpfulHint.reset()
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    ratioCheckComponents = [TreasureLocation, HelpfulHint, key_resp_2]
    for thisComponent in ratioCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ratioCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ratioCheck"-------
    while continueRoutine:
        # get current time
        t = ratioCheckClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ratioCheckClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *TreasureLocation* updates
        if TreasureLocation.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            TreasureLocation.frameNStart = frameN  # exact frame index
            TreasureLocation.tStart = t  # local t and not account for scr refresh
            TreasureLocation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TreasureLocation, 'tStartRefresh')  # time at next scr refresh
            TreasureLocation.setAutoDraw(True)
        # *HelpfulHint* updates
        if HelpfulHint.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HelpfulHint.frameNStart = frameN  # exact frame index
            HelpfulHint.tStart = t  # local t and not account for scr refresh
            HelpfulHint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HelpfulHint, 'tStartRefresh')  # time at next scr refresh
            HelpfulHint.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratioCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ratioCheck"-------
    for thisComponent in ratioCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if counterbalancing < 5 and counterbalancing % 2:
        
        if TreasureLocation.getRating() > 5 and HelpfulHint.getRating() > 5:
            fam_repeat.finished = 1
            
    elif counterbalancing > 5 and counterbalancing % 2:
        
        if TreasureLocation.getRating() > 5 and HelpfulHint.getRating() > 5:
            fam_repeat.finished = 1
            
    elif counterbalancing < 5 and not counterbalancing % 2:
        
        if TreasureLocation.getRating() > 5 and HelpfulHint.getRating() > 5:
            fam_repeat.finished = 1
            
    elif counterbalancing > 5 and not counterbalancing % 2:
        
        if TreasureLocation.getRating() > 5 and HelpfulHint.getRating() > 5:
            fam_repeat.finished = 1
    # store data for fam_repeat (TrialHandler)
    fam_repeat.addData('TreasureLocation.response', TreasureLocation.getRating())
    fam_repeat.addData('TreasureLocation.rt', TreasureLocation.getRT())
    fam_repeat.addData('TreasureLocation.started', TreasureLocation.tStart)
    fam_repeat.addData('TreasureLocation.stopped', TreasureLocation.tStop)
    # store data for fam_repeat (TrialHandler)
    fam_repeat.addData('HelpfulHint.response', HelpfulHint.getRating())
    fam_repeat.addData('HelpfulHint.rt', HelpfulHint.getRT())
    fam_repeat.addData('HelpfulHint.started', HelpfulHint.tStart)
    fam_repeat.addData('HelpfulHint.stopped', HelpfulHint.tStop)
    # the Routine "ratioCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'fam_repeat'


# ------Prepare to start Routine "Instruct5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
Instruct5Components = [text, key_resp_7]
for thisComponent in Instruct5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruct5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruct5"-------
while continueRoutine:
    # get current time
    t = Instruct5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruct5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct5"-------
for thisComponent in Instruct5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruct5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
trial_list_s = zero*45+one*15 # Blue 75% Green 25%
trial_list_vi = zero*16+one*4
trial_list_vii = zero*4+one*16

rand.shuffle(trial_list_s)
rand.shuffle(trial_list_vi)
rand.shuffle(trial_list_vii)
#overall task probability
prob_bg = trial_list_s + trial_list_vi + trial_list_vii + trial_list_vi

num_trial = len(prob_bg)

r_val = []
l_val = []

#create reward values
for t in range(0,num_trial):
    val = rand.randint(1,100)
    r_val.append(val)
    l_val.append(100-val)

#counterbalancing = int(expInfo['condition'])

#if counterbalancing % 2:
#    trial_list_s = zero*8 + one*2
#    cb_hint_chance = 0.8

#if counterbalancing //4:
#    trial_list_s = zero*2 + one*8
#    cb_hint_chance = 0.8




#if counterbalancing // 4:
#    cb_hint_chance_1 = 0.75
#    cb_hint_chance_2 = 0.15
#else:
#    cb_hint_chance_1 = 0.25
#    cb_hint_chance_2 = 0.85


#if (condition_value % 4) // 2:
# keep track of which components have finished
IntroComponents = []
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialList.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "studyTrial"-------
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    #Assuming you have a r_val and and l_val list:
    
    trial_r_val = r_val[ currentLoop.thisN ]
    trial_l_val = l_val[ currentLoop.thisN ]
    
    # Generate uniformly distributed random number between 0 and 1
    hint_prob = rand.uniform(size = 1)
    
    # Generate start times for hint and response window
    hint_start = rand.uniform(3, 7)
    resp_start = hint_start + rand.uniform(3, 7)
    
    # Set up selection positions
    left_pos = (-0.52, -0.32)
    right_pos = (0.52, -0.32)
    
    # Pre-generated array way of changing hint correct probability
    #corr_hint_chance = hint_prob[ currentLoop.thisN ]
    
    # Multiple ifs way of changing hint correct probability
    if currentLoop.thisN < 30:
           corr_hint_chance = cb_hint_chance_1
    elif currentLoop.thisN < 40:
            corr_hint_chance = 0.2
    elif currentLoop.thisN < 50:
            corr_hint_chance = 0.8
    elif currentLoop.thisN < 60:
            corr_hint_chance = 0.2
    elif currentLoop.thisN < 70:
            corr_hint_chance = 0.8
    elif currentLoop.thisN < 120:
            corr_hint_chance = cb_hint_chance_2
    
    
    # statement to define correct keys for trial
    if prob_bg[ currentLoop.thisN ]:
        correct_key = 'left'
        # Determine whether the hint will be show on correct or incorrect side
        if hint_prob <= corr_hint_chance:
           imageVariable = imagePath + "Lgreenhint.bmp"
           correct_hint = 1
        else:
            imageVariable = imagePath + "Rbluehint.bmp"
            correct_hint = 0
    else:
        correct_key = 'right'
        if hint_prob <= corr_hint_chance:
            imageVariable = imagePath + "Rbluehint.bmp"
            correct_hint = 1
        else:
            imageVariable = imagePath + "Lgreenhint.bmp"
            correct_hint = 0
    hint.setImage(imageVariable)
    R_text.setText(trial_r_val)
    L_text.setText(trial_l_val)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    studyTrialComponents = [background, hint, R_text, L_text, key_resp, fixation]
    for thisComponent in studyTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    studyTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "studyTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = studyTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=studyTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background* updates
        if background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background.frameNStart = frameN  # exact frame index
            background.tStart = t  # local t and not account for scr refresh
            background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
            background.setAutoDraw(True)
        if background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                background.tStop = t  # not accounting for scr refresh
                background.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background, 'tStopRefresh')  # time at next scr refresh
                background.setAutoDraw(False)
        
        # *hint* updates
        if hint.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            hint.frameNStart = frameN  # exact frame index
            hint.tStart = t  # local t and not account for scr refresh
            hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hint, 'tStartRefresh')  # time at next scr refresh
            hint.setAutoDraw(True)
        if hint.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hint.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                hint.tStop = t  # not accounting for scr refresh
                hint.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hint, 'tStopRefresh')  # time at next scr refresh
                hint.setAutoDraw(False)
        
        # *R_text* updates
        if R_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_text.frameNStart = frameN  # exact frame index
            R_text.tStart = t  # local t and not account for scr refresh
            R_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_text, 'tStartRefresh')  # time at next scr refresh
            R_text.setAutoDraw(True)
        if R_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R_text.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                R_text.tStop = t  # not accounting for scr refresh
                R_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(R_text, 'tStopRefresh')  # time at next scr refresh
                R_text.setAutoDraw(False)
        
        # *L_text* updates
        if L_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_text.frameNStart = frameN  # exact frame index
            L_text.tStart = t  # local t and not account for scr refresh
            L_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_text, 'tStartRefresh')  # time at next scr refresh
            L_text.setAutoDraw(True)
        if L_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_text.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                L_text.tStop = t  # not accounting for scr refresh
                L_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_text, 'tStopRefresh')  # time at next scr refresh
                L_text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(correct_key)) or (key_resp.keys == correct_key):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in studyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "studyTrial"-------
    for thisComponent in studyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # This code will run at the end of the routine in which it is placed
    # Useful for making adjustments to the following routine based on responses in the current routine
    
    # Ensure that the object you are accessing ('key_resp') is the named exactly the same here as in the builder
    if key_resp.keys == 'left': # Start by checking which key was pressed
        select_pos = left_pos
        if key_resp.corr: # Then see if the response was correct
            imageVariable = imagePath + "Lgreenwin.bmp" # If yes then display the treasure
            score_update = trial_l_val # Add the value displayed to the players score
            textFeedback = fdbck_winText # Display positive feedback text
            soundFeedback = "stimuli/coins-drop-1.wav"
        else:
            imageVariable = imagePath + "Lgreenlose.bmp"# Otherwise show the empty chest
            score_update = 0
            textFeedback = fdbck_loseText
            soundFeedback = None
    elif key_resp.keys == 'right':# Same as above but on the other side 
        select_pos = right_pos
        if key_resp.corr:
            imageVariable = imagePath + "Rbluewin.bmp" # The predefined image path is added to the file name
            score_update = trial_r_val # Add the value displayed to the players score
            textFeedback = fdbck_winText # Display positive feedback text
            soundFeedback = "stimuli/coins-drop-1.wav"
        else:
            imageVariable = imagePath + "Rbluelose.bmp"
            score_update = 0
            textFeedback = fdbck_loseText
            soundFeedback = None
    # If response is too slow
    #else:
    #    pass select_pos 
    #    imageVariable = imagePath + "piratetask.bmp"
    #    score_update = 0
    #    textFeedback = fdbck_tooslowText
    
    old_player_score = player_score
    new_player_score = player_score + score_update
    
    # You might not need this here if you implement the resetting bar in the feedback routine
    # But you will want to transplant some of this code to it
    # (e.g. increasing the player level, subtracting the level limit)
    if player_score > level_limit:
        pirate_level += 1
        leveled_up = True
        
        player_score -= level_limit
    
    # Add data to the output
    trials.addData('trial_r_val', trial_r_val)
    trials.addData('trial_l_val', trial_l_val)
    trials.addData('correct_hint', correct_hint) 
    trials.addData('prob_bg', prob_bg[ currentLoop.thisN ])
    
    
    # Use this to set the image in the following routine
    # Again be sure that the object called is named the same thing as the object in the builder
    image.setImage(imageVariable)
    
    trials.addData('hint.started', hint.tStartRefresh)
    trials.addData('hint.stopped', hint.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    
    # ------Prepare to start Routine "selection"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    r_text.setText(trial_r_val)
    l_text.setText(trial_l_val)
    select_frame.setPos(select_pos)
    # keep track of which components have finished
    selectionComponents = [background2, r_text, l_text, select_frame]
    for thisComponent in selectionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    selectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "selection"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = selectionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=selectionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *background2* updates
        if background2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            background2.frameNStart = frameN  # exact frame index
            background2.tStart = t  # local t and not account for scr refresh
            background2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background2, 'tStartRefresh')  # time at next scr refresh
            background2.setAutoDraw(True)
        if background2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                background2.tStop = t  # not accounting for scr refresh
                background2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(background2, 'tStopRefresh')  # time at next scr refresh
                background2.setAutoDraw(False)
        
        # *r_text* updates
        if r_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            r_text.frameNStart = frameN  # exact frame index
            r_text.tStart = t  # local t and not account for scr refresh
            r_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_text, 'tStartRefresh')  # time at next scr refresh
            r_text.setAutoDraw(True)
        if r_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > r_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                r_text.tStop = t  # not accounting for scr refresh
                r_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(r_text, 'tStopRefresh')  # time at next scr refresh
                r_text.setAutoDraw(False)
        
        # *l_text* updates
        if l_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            l_text.frameNStart = frameN  # exact frame index
            l_text.tStart = t  # local t and not account for scr refresh
            l_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_text, 'tStartRefresh')  # time at next scr refresh
            l_text.setAutoDraw(True)
        if l_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                l_text.tStop = t  # not accounting for scr refresh
                l_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(l_text, 'tStopRefresh')  # time at next scr refresh
                l_text.setAutoDraw(False)
        
        # *select_frame* updates
        if select_frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            select_frame.frameNStart = frameN  # exact frame index
            select_frame.tStart = t  # local t and not account for scr refresh
            select_frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(select_frame, 'tStartRefresh')  # time at next scr refresh
            select_frame.setAutoDraw(True)
        if select_frame.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > select_frame.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                select_frame.tStop = t  # not accounting for scr refresh
                select_frame.frameNStop = frameN  # exact frame index
                win.timeOnFlip(select_frame, 'tStopRefresh')  # time at next scr refresh
                select_frame.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "selection"-------
    for thisComponent in selectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(imageVariable)
    R_text_2.setText(trial_r_val)
    L_text_2.setText(trial_l_val)
    fdbck_text.setText(textFeedback)
    
    # Calculate the initial and final height based on the score variables
    initial_height = old_player_score * height_for_one_point
    final_height = new_player_score * height_for_one_point
    
    # Calculate the amount of movement
    total_amount_to_move = final_height - initial_height
    
    frame_duration = move_dur * 60
    
    height_RoC = total_amount_to_move/frame_duration
    yPos_RoC = height_RoC/2
    
    
    
    # You might not need this here if you implement the resetting bar in the feedback routine
    # But you will want to transplant some of this code to it
    # (e.g. increasing the player level, subtracting the level limit)
    if player_score > level_limit:
        pirate_level += 1
        leveled_up = True
        
        player_score -= level_limit
    # keep track of which components have finished
    feedbackComponents = [image, R_text_2, L_text_2, fdbck_text, feedbackFrame, feedbackFill]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *R_text_2* updates
        if R_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_text_2.frameNStart = frameN  # exact frame index
            R_text_2.tStart = t  # local t and not account for scr refresh
            R_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_text_2, 'tStartRefresh')  # time at next scr refresh
            R_text_2.setAutoDraw(True)
        if R_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R_text_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                R_text_2.tStop = t  # not accounting for scr refresh
                R_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(R_text_2, 'tStopRefresh')  # time at next scr refresh
                R_text_2.setAutoDraw(False)
        
        # *L_text_2* updates
        if L_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_text_2.frameNStart = frameN  # exact frame index
            L_text_2.tStart = t  # local t and not account for scr refresh
            L_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_text_2, 'tStartRefresh')  # time at next scr refresh
            L_text_2.setAutoDraw(True)
        if L_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_text_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                L_text_2.tStop = t  # not accounting for scr refresh
                L_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_text_2, 'tStopRefresh')  # time at next scr refresh
                L_text_2.setAutoDraw(False)
        
        # *fdbck_text* updates
        if fdbck_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fdbck_text.frameNStart = frameN  # exact frame index
            fdbck_text.tStart = t  # local t and not account for scr refresh
            fdbck_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fdbck_text, 'tStartRefresh')  # time at next scr refresh
            fdbck_text.setAutoDraw(True)
        if fdbck_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fdbck_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                fdbck_text.tStop = t  # not accounting for scr refresh
                fdbck_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fdbck_text, 'tStopRefresh')  # time at next scr refresh
                fdbck_text.setAutoDraw(False)
        
        # *feedbackFrame* updates
        if feedbackFrame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackFrame.frameNStart = frameN  # exact frame index
            feedbackFrame.tStart = t  # local t and not account for scr refresh
            feedbackFrame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackFrame, 'tStartRefresh')  # time at next scr refresh
            feedbackFrame.setAutoDraw(True)
        if feedbackFrame.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackFrame.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackFrame.tStop = t  # not accounting for scr refresh
                feedbackFrame.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackFrame, 'tStopRefresh')  # time at next scr refresh
                feedbackFrame.setAutoDraw(False)
        
        # *feedbackFill* updates
        if feedbackFill.status == NOT_STARTED and tThisFlip >= rect_start-frameTolerance:
            # keep track of start time/frame for later
            feedbackFill.frameNStart = frameN  # exact frame index
            feedbackFill.tStart = t  # local t and not account for scr refresh
            feedbackFill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackFill, 'tStartRefresh')  # time at next scr refresh
            feedbackFill.setAutoDraw(True)
        if feedbackFill.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackFill.tStartRefresh + rect_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedbackFill.tStop = t  # not accounting for scr refresh
                feedbackFill.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackFill, 'tStopRefresh')  # time at next scr refresh
                feedbackFill.setAutoDraw(False)
        if feedbackFill.status == STARTED:  # only update if drawing
            feedbackFill.setPos(rect_pos, log=False)
            feedbackFill.setSize(rect_dims, log=False)
        # Only change once the bars have appreared 
        if feedbackFill.status == STARTED and t > move_start and t < (rect_dur - end_idle):
            # Only update the height/y properties (index 1 for both)
            rect_dims[1] += height_RoC
            rect_pos[1] += yPos_RoC
        
            # This calculates where the top of the bar is:
            # Position of bar + half the height (as position is always measured from middle)
            bar_top = rect_pos[1] + rect_dims[1]/2
        
            # If bar goes beyond upper limit of frame then reset it
            if bar_top > 0.15:
                rect_dims[1] = height
                rect_pos[1] = y_pos
               
                pirate_level += 1
                player_score -= level_limit
                
                level_up = True
                
                #fdbck_text.setText("Congratulations, you are now level %d" % pirate_level)
        
        if fdbck_text.status == STARTED and t > (rect_dur - end_idle) and level_up:
            fdbck_text.setText("Congratulations, you are now a level %d pirate" % pirate_level)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    level_up = False
    
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
