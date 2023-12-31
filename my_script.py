# make sure you are in the directory that contains your measurement set (.ms file)
# assign ms name to the variable vis, so that we don't need to type the long name every time!
vis="sis14_twhya_selfcal.ms"

listobs(vis=vis)
# After the above command you can see the details about the observation in the logger, such as the time on different sources (targets, calibrators, etc.), and info about antennas.
# You can see that the observation is from Nov 19th 2022 07:36:57 UTC to 09:11:04 UTC.
# There are 5 fields, meaning the telescope observed 5 objects, you can see the nature of the objects in scan intent
# For example, you can see J0522-364 is a bandpass calibrator, Ceres is a amplitude calibrator, TW Hya is the observation target (what you are actually interested in)!

plotms(vis=vis, xaxis='u', yaxis='v', avgchannel='10000', avgspw=False, avgtime='1e9', avgscan=False, coloraxis="field", showgui=True)
# if you run into an display environment variable error, quit casa and run this command in the terminal. Then open casa again and it should work. remember to assign the ms name to vis again.
export DISPLAY=:1

# After running the above plotms command, you can see the uv plot! This is the visibility. If we do fourier transform on the uv plot, then you will get the sky brightness.
# In the command, the color axis is 'field', meaning that different colors on the plot indicate different fields (or sources)

# Then we can make the continuum image!
# We first ran the command without specifying niter, so we only got the warning but the casa viewer won't appear because we're not trying to clean it (niter not specified).
tclean(vis=vis,
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

# remove any file that starts with phase_cal
os.system('rm -rf phase_cal.*')

# Now we re-run the command with niter=5000 so now casa viewer appears because it knows we are trying to interactive clean.
tclean(vis=vis,
       imagename='phase_cal',
       field='3',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       gridder='standard',
       imsize=[128,128],
       cell=['0.1arcsec'],
       weighting='briggs',
       threshold='0mJy',
       niter=5000,
       interactive=True)