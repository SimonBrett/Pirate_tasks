#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 07, 2020, at 17:38
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
    originPath='C:\\Users\\tobiiuser\\Documents\\GitHub\\Pirate_tasks\\pirateTrial_lastrun.py',
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

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
# Code in here is run at the very beginning of the experiment
# Put stuff here that you need to run once but doesn't change

imagePath = "stimuli/" # This establishes where the stimuli are stored
imageVariable = None # Need this to initialise the feedback image display
textFeedback = None # Need this to initialise the text feedback display
fdbck_winText = "Well done you chose correctly!"
fdbck_loseText = "better luck next time!"

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
prob_bg = [(trial_list_s, trial_list_vi, trial_list_vii, trial_list_vi)]



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
    val = rand.randint(1,101)
    r_val.append(val)
    l_val.append(100-val)

player_score = 0
pirate_level = 0
level_limit = 460
leveled_up = False

background = visual.ImageStim(
    win=win,
    name='background', 
    image='stimuli/piratetask.bmp', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
R_text = visual.TextStim(win=win, name='R_text',
    text='default text',
    font='Arial',
    pos=(0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
L_text = visual.TextStim(win=win, name='L_text',
    text='default text',
    font='Arial',
    pos=(-0.43, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0, pos=[0,0],
    lineWidth=8, lineColor=[1.000,1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
key_resp = keyboard.Keyboard()

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
    width=(0.35, 0.55)[0], height=(0.35, 0.55)[1],
    ori=0, pos=(0, -0.2),
    lineWidth=1, lineColor=[1.000,1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
feedbackFill = visual.Rect(
    win=win, name='feedbackFill',
    width=(0.35, 0.55)[0], height=(0.35, 0.55)[1],
    ori=0, pos=(0, -0.2),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[1.000,1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # Set up hint positions
    left_pos = (0.5, -0.3)
    right_pos = (-0.5, -0.3)
    
    # Pre-generated array way of changing hint correct probability
    corr_hint_chance = hint_prob[ currentLoop.thisN ]
    
    # Multiple ifs way of changing hint correct probability
    #if currentLoop.thisN < 80:
    #    corr_hint_chance = 0.75
    #elif currentLoop.thisN < 160:
    #    corr_hint_chance = 0.15
    #...
    
    # statement to define correct keys for trial
    if prob_bg[ currentLoop.thisN ]:
        correct_key = 'left'
        # Determine whether the hint will be show on correct or incorrect side
        if hint_prob <= corr_hint_chance:
            hint_pos = left_pos
        else:
            hint_pos = right_pos
    else:
        correct_key = 'right'
        if hint_prob <= corr_hint_chance:
            hint_pos = right_pos
        else:
            hint_pos = left_pos
    R_text.setText(trial_r_val)
    L_text.setText(trial_l_val)
    polygon.setPos(left_pos)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    studyTrialComponents = [background, R_text, L_text, polygon, key_resp]
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
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
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
        if key_resp.corr: # Then see if the response was correct
            imageVariable = imagePath + "Lgreenwin.bmp" # If yes then display the treasure
            player_score += trial_l_val # Add the value displayed to the players score
            textFeedback = fdbck_winText # Display positive feedback text
        else:
            imageVariable = imagePath + "Lgreenlose.bmp"# Otherwise show the empty chest
            textFeedback = fdbckloseText
    elif key_resp.keys == 'right': # Same as above but on the other side 
        if key_resp.corr:
            imageVariable = imagePath + "Rbluewin.bmp" # The predefined image path is added to the file name
            player_score += trial_r_val # Add the value displayed to the players score
            textFeedback = fdbck_winText # Display positive feedback text
        else:
            imageVariable = imagePath + "Rbluelose.bmp"
            textFeedback = fdbck_loseText
    
    if player_score > level_limit:
        pirate_level += 1
        leveled_up = True
        
        player_score -= level_limit
    
    
    
    # Use this to set the image in the following routine
    # Again be sure that the object called is named the same thing as the object in the builder
    image.setImage(imageVariable)
    
    trials.addData('background.started', background.tStartRefresh)
    trials.addData('background.stopped', background.tStopRefresh)
    trials.addData('R_text.started', R_text.tStartRefresh)
    trials.addData('R_text.stopped', R_text.tStopRefresh)
    trials.addData('L_text.started', L_text.tStartRefresh)
    trials.addData('L_text.stopped', L_text.tStopRefresh)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
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
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    image.setImage(imageVariable)
    R_text_2.setText(trial_r_val)
    L_text_2.setText(trial_l_val)
    fdbck_text.setText(textFeedback)
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        if feedbackFill.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackFill.frameNStart = frameN  # exact frame index
            feedbackFill.tStart = t  # local t and not account for scr refresh
            feedbackFill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackFill, 'tStartRefresh')  # time at next scr refresh
            feedbackFill.setAutoDraw(True)
        if feedbackFill.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackFill.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackFill.tStop = t  # not accounting for scr refresh
                feedbackFill.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackFill, 'tStopRefresh')  # time at next scr refresh
                feedbackFill.setAutoDraw(False)
        
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
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('R_text_2.started', R_text_2.tStartRefresh)
    trials.addData('R_text_2.stopped', R_text_2.tStopRefresh)
    trials.addData('L_text_2.started', L_text_2.tStartRefresh)
    trials.addData('L_text_2.stopped', L_text_2.tStopRefresh)
    trials.addData('fdbck_text.started', fdbck_text.tStartRefresh)
    trials.addData('fdbck_text.stopped', fdbck_text.tStopRefresh)
    trials.addData('feedbackFrame.started', feedbackFrame.tStartRefresh)
    trials.addData('feedbackFrame.stopped', feedbackFrame.tStopRefresh)
    trials.addData('feedbackFill.started', feedbackFill.tStartRefresh)
    trials.addData('feedbackFill.stopped', feedbackFill.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


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
