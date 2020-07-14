#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 14, 2020, at 11:22
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
expName = 'amin_test'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Daniel\\Documents\\GitHub\\Pirate_tasks\\anim_test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
inner_rect = visual.Rect(
    win=win, name='inner_rect',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[0,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
outer_rect = visual.Rect(
    win=win, name='outer_rect',
    width=(0.02, 0.2)[0], height=(0.02, 0.2)[1],
    ori=0, pos=(0, -0.05),
    lineWidth=2, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
# Set initial vaules for bar
height = 0.02
width = 0.02

x_pos = 0
y_pos = -0.14

# timings for bar
rect_start = 1
rect_dur = 3

# Set rate of change (i.e. change between frames)
height_RoC = 0.002
yPos_RoC = height_RoC/2

# Two options for final version:
# 1. Set duration, in which case the RoCs will be scaled by the score (variable speed/fixed duration)
# 1. Set rate of change, in which case the duration will be scaled by score (variable duration/ fixed speed)

# Put variables into lists
rect_dims = [width, height]
rect_pos = [x_pos, y_pos]


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [text, inner_rect, outer_rect]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
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
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *inner_rect* updates
    if inner_rect.status == NOT_STARTED and tThisFlip >= rect_start-frameTolerance:
        # keep track of start time/frame for later
        inner_rect.frameNStart = frameN  # exact frame index
        inner_rect.tStart = t  # local t and not account for scr refresh
        inner_rect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inner_rect, 'tStartRefresh')  # time at next scr refresh
        inner_rect.setAutoDraw(True)
    if inner_rect.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inner_rect.tStartRefresh + rect_dur-frameTolerance:
            # keep track of stop time/frame for later
            inner_rect.tStop = t  # not accounting for scr refresh
            inner_rect.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inner_rect, 'tStopRefresh')  # time at next scr refresh
            inner_rect.setAutoDraw(False)
    if inner_rect.status == STARTED:  # only update if drawing
        inner_rect.setPos(rect_pos, log=False)
        inner_rect.setSize(rect_dims, log=False)
    
    # *outer_rect* updates
    if outer_rect.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        outer_rect.frameNStart = frameN  # exact frame index
        outer_rect.tStart = t  # local t and not account for scr refresh
        outer_rect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(outer_rect, 'tStartRefresh')  # time at next scr refresh
        outer_rect.setAutoDraw(True)
    if outer_rect.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > outer_rect.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            outer_rect.tStop = t  # not accounting for scr refresh
            outer_rect.frameNStop = frameN  # exact frame index
            win.timeOnFlip(outer_rect, 'tStopRefresh')  # time at next scr refresh
            outer_rect.setAutoDraw(False)
    # Update size and positions on each frame
    
    # Only change once the bars have appreared 
    if inner_rect.status == STARTED:
        # Only update the height/y properties (index 1 for both)
        rect_dims[1] += height_RoC
        rect_pos[1] += yPos_RoC
    
        # This calculates where the top of the bar is:
        # Position of bar + half the height (as position is always measured from middle)
        bar_top = rect_pos[1] + rect_dims[1]/2
    
        # If bar goes beyond upper limit of frame then reset it
        if bar_top > 0.05:
            rect_dims[1] = height
            rect_pos[1] = y_pos
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('inner_rect.started', inner_rect.tStartRefresh)
thisExp.addData('inner_rect.stopped', inner_rect.tStopRefresh)
thisExp.addData('outer_rect.started', outer_rect.tStartRefresh)
thisExp.addData('outer_rect.stopped', outer_rect.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
