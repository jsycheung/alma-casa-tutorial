# make sure you are in the directory that contains your measurement set (.ms file)
vis="sis14_twhya_selfcal.ms"

listobs(vis=vis)
# After the above command you can see the details about the observation in the logger, such as the time on different sources (targets, calibrators, etc.), and info about antennas.
# You can see that the observation is from Nov 19th 2022 07:36:57 UTC to 09:11:04 UTC.
# There are 5 fields, meaning the telescope observed 5 objects, you can see the nature of the objects in scan intent
# For example, you can see J0522-364 is a bandpass calibrator, Ceres is a amplitude calibrator, TW Hya is the observation target (what you are actually interested in)!

#Then we can make the continuum image!
tclean(vis='sis14_twhya_selfcal.ms',
       imagename='phase_cal',
       field='3',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       gridder='standard',
       imsize=[128,128],
       cell=['0.1arcsec'],
       weighting='briggs',
       threshold='0.0mJy',
       interactive=True)