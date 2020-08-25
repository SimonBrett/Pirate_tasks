﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 25, 2020, at 11:31
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
expInfo = {'participant': '', 'session': '001'}
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
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "famIntro"
famIntroClock = core.Clock()
#Store images and initialise feedback display
imagePath = "stimuli/" 
imageVariable = None 


#Number of familiarisation trials
num_trial = 10 

# Setup blue/green win lose ratio
zero = [0] 
one = [1]
trial_list_s = zero*8+one*2 # Blue 80% Green 20%
trial_list_s1 = zero*2+one*8 # Blue 20% Green 80%


from numpy import random as rand #randomise lists
rand.shuffle(trial_list_s)
rand.shuffle(trial_list_s1)

#overall familiarisation probability (blue win 80%)
fam_prob_bg = trial_list_s 

#overall familiarisation probability (green win 80%)
fam_prob_gb = trial_list_s1

# reward variables
r_val = []
l_val = []

#create reward values
for t in range(0,num_trial):
    val = rand.randint(1,100)
    r_val.append(val)
    l_val.append(100-val)


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

# Initialize components for Routine "ratioCheck"
ratioCheckClock = core.Clock()

# Initialize components for Routine "Instruct2"
Instruct2Clock = core.Clock()

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
# Code in here is run at the very beginning of the experiment
# Put stuff here that you need to run once but doesn't change

imagePath = "stimuli/" # This establishes where the stimuli are stored
imageVariable = None # Need this to initialise the feedback image display
textFeedback = None # Need this to initialise the text feedback display
fdbck_winText = "Well done you chose correctly!"
fdbck_loseText = "Better luck next time!"
#soundFeedback = None # Need this to initialise the sound feedback display


num_trial = 120 # Number of trials in the experiment
zero = [0] #create lists 
one = [1]
trial_list_s = zero*45+one*15 # Blue 75% Green 25%
trial_list_vi = zero*16+one*4
trial_list_vii = zero*4+one*16

# used for pregenerating array of correct hint probabilities
#hint_list_s = zero*22+one*8 # p(hint = correct) first 30 trials = 0.73
#hint_list_vi = zero*8+one*2 # p(hint = correct) = 0.8
#hint_list_vii = zero*2+one*8 # p(hint = correct) = 0.2
#hint_list_si = zero*8+one*42 # p(hint = correct) last 50 = 0.16

# If using this method need to repeat for each set of trials (i.e. s, vi, vii)
# and then concatenate (as with bg_prob below)
#hint_prob = [(hint_list_s, hint_list_vii, hint_list_vi, hint_list_vii, hint_list_vi, hint_list_si)]


from numpy import random as rand #randomise lists
rand.shuffle(trial_list_s)
rand.shuffle(trial_list_vi)
rand.shuffle(trial_list_vii)
#overall task probability
prob_bg = trial_list_s + trial_list_vi + trial_list_vii + trial_list_vi



# set up "winning score"
#r_mult = prob_bg[t]
#l_mult = 1-prob_bg[t]
#r_tot = r_val*r_mult
#l_tot = l_val*l_mult


# Initialize components for Routine "studyTrial"
studyTrialClock = core.Clock()
r_val = []
l_val = []

#create reward values
for t in range(0,num_trial):
    val = rand.randint(1,100)
    r_val.append(val)
    l_val.append(100-val)

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
resp = visual.TextStim(win=win, name='resp',
    text='?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

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
# keep track of which components have finished
Instruct1Components = []
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
# the Routine "Instruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "famIntro"-------
continueRoutine = True
# update component parameters for each repeat
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
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('famtrialList.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "famTrial"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    trial_r_val = r_val[ currentLoop.thisN ]
    trial_l_val = l_val[ currentLoop.thisN ]
    
    # Generate uniformly distributed random number between 0 and 1
    hint_prob = rand.uniform(size = 1)
    select_prob = rand.uniform(size = 1)
    
    # Set up selection positions
    left_pos = (-0.52, -0.32)
    right_pos = (0.52, -0.32)
    
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
            imageFeedback = imagePath + "Lgreenlose.bmp"# Otherwise show the empty chest
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
            imagefeedback = imagePath + "Rbluewin.bmp" # The predefined image path is added to the file name
            textFeedback = fdbck_winText # Display positive feedback text
            soundFeedback = "stimuli/coins-drop-1.wav"
        else:
            select_pos = left_pos
            imageFeedback = imagePath + "Rbluelose.bmp"
            textFeedback = fdbck_loseText
            soundFeedback = None 
    
    
    if fam_prob_bg[ currentLoop.thisN ]: # Start by checking if blue or green is the winner
        if correct_pos:
            imageVariable = imagePath + "Lgreenwin.bmp" #  then display the treasure
            textFeedback = fdbck_winText # Display positive feedback text
            soundFeedback = "stimuli/coins-drop-1.wav"
        else:
            imageVariable = imagePath + "Lgreenlose.bmp"# Otherwise show the empty chest
            textFeedback = fdbck_loseText
            soundFeedback = None
    elif fam_prob_bg[ currentLoop.thisN ]: # Same as above but on the other side 
        if correct_pos:
            imageVariable = imagePath + "Rbluewin.bmp" # The predefined image path is added to the file name
            textFeedback = fdbck_winText # Display positive feedback text
            soundFeedback = "stimuli/coins-drop-1.wav"
        else:
            imageVariable = imagePath + "Rbluelose.bmp"
            textFeedback = fdbck_loseText
            soundFeedback = None 
    famHint.setImage(imageVariable)
    famR_text.setText(trial_r_val)
    famL_text.setText(trial_l_val)
    famSelect_pos.setPos(select_pos)
    # keep track of which components have finished
    famTrialComponents = [famBackground, famHint, famR_text, famL_text, famSelect_pos]
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
        if famBackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if tThisFlipGlobal > famHint.tStartRefresh + 2.0-frameTolerance:
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
            if tThisFlipGlobal > famR_text.tStartRefresh + 3.0-frameTolerance:
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
            if tThisFlipGlobal > famL_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                famL_text.tStop = t  # not accounting for scr refresh
                famL_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(famL_text, 'tStopRefresh')  # time at next scr refresh
                famL_text.setAutoDraw(False)
        
        # *famSelect_pos* updates
        if famSelect_pos.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
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
    trials_2.addData('famBackground.started', famBackground.tStartRefresh)
    trials_2.addData('famBackground.stopped', famBackground.tStopRefresh)
    trials_2.addData('famHint.started', famHint.tStartRefresh)
    trials_2.addData('famHint.stopped', famHint.tStopRefresh)
    trials_2.addData('famR_text.started', famR_text.tStartRefresh)
    trials_2.addData('famR_text.stopped', famR_text.tStopRefresh)
    trials_2.addData('famL_text.started', famL_text.tStartRefresh)
    trials_2.addData('famL_text.stopped', famL_text.tStopRefresh)
    trials_2.addData('famSelect_pos.started', famSelect_pos.tStartRefresh)
    trials_2.addData('famSelect_pos.stopped', famSelect_pos.tStopRefresh)
    
    # ------Prepare to start Routine "famFeedback"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    famImage.setImage(imageFeedback)
    # keep track of which components have finished
    famFeedbackComponents = [famImage]
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
            if tThisFlipGlobal > famImage.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                famImage.tStop = t  # not accounting for scr refresh
                famImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(famImage, 'tStopRefresh')  # time at next scr refresh
                famImage.setAutoDraw(False)
        
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
    trials_2.addData('famImage.started', famImage.tStartRefresh)
    trials_2.addData('famImage.stopped', famImage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "ratioCheck"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ratioCheckComponents = []
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
# the Routine "ratioCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruct2"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Instruct2Components = []
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
# the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
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
           corr_hint_chance = 0.75
    elif currentLoop.thisN < 40:
            corr_hint_chance = 0.2
    elif currentLoop.thisN < 50:
            corr_hint_chance = 0.8
    elif currentLoop.thisN < 60:
            corr_hint_chance = 0.2
    elif currentLoop.thisN < 70:
            corr_hint_chance = 0.8
    elif currentLoop.thisN < 120:
            corr_hint_chance = 0.15
    
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
    studyTrialComponents = [background, hint, R_text, L_text, key_resp, resp, fixation]
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
    while continueRoutine:
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
        
        # *hint* updates
        if hint.status == NOT_STARTED and tThisFlip >= hint_start-frameTolerance:
            # keep track of start time/frame for later
            hint.frameNStart = frameN  # exact frame index
            hint.tStart = t  # local t and not account for scr refresh
            hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hint, 'tStartRefresh')  # time at next scr refresh
            hint.setAutoDraw(True)
        
        # *R_text* updates
        if R_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_text.frameNStart = frameN  # exact frame index
            R_text.tStart = t  # local t and not account for scr refresh
            R_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_text, 'tStartRefresh')  # time at next scr refresh
            R_text.setAutoDraw(True)
        
        # *L_text* updates
        if L_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_text.frameNStart = frameN  # exact frame index
            L_text.tStart = t  # local t and not account for scr refresh
            L_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_text, 'tStartRefresh')  # time at next scr refresh
            L_text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= resp_start-frameTolerance:
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
        
        # *resp* updates
        if resp.status == NOT_STARTED and tThisFlip >= resp_start-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.setAutoDraw(True)
        
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
            if tThisFlipGlobal > fixation.tStartRefresh + resp_start-frameTolerance:
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
    # the Routine "studyTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "selection"-------
    continueRoutine = True
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
    while continueRoutine:
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
            if tThisFlipGlobal > background2.tStartRefresh + hint_start-frameTolerance:
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
            if tThisFlipGlobal > r_text.tStartRefresh + hint_start-frameTolerance:
                # keep track of stop time/frame for later
                r_text.tStop = t  # not accounting for scr refresh
                r_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(r_text, 'tStopRefresh')  # time at next scr refresh
                r_text.setAutoDraw(False)
        
        # *l_text* updates
        if l_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l_text.frameNStart = frameN  # exact frame index
            l_text.tStart = t  # local t and not account for scr refresh
            l_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_text, 'tStartRefresh')  # time at next scr refresh
            l_text.setAutoDraw(True)
        if l_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_text.tStartRefresh + hint_start-frameTolerance:
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
            if tThisFlipGlobal > select_frame.tStartRefresh + hint_start-frameTolerance:
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
    # the Routine "selection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
