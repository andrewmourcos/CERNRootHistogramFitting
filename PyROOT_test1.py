#!/bin/env python
import ROOT
from ROOT import gPad
data ="/afs/cern.ch/user/d/daquser/work/public/2017_cc/alignment"

filething = "1506456670Beam_monitor.root"
histoname = "hitmap_BL4Smm3_BL4Smm2"
f_in= ROOT.TFile.Open(data+"/"+filething)
histo = f_in.Get("Histogramming/Beam_monitor/"+histoname)
histo.Draw()
gPad.WaitPrimitive()
