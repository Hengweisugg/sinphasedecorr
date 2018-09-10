# sinphasedecorr
Script for creating a 2 channel decorrelated signal pair using sinusoidal phase all-pass pair.

## How to use

Executing Sinphasedecorr.py will read the audio file as source signals, perform filtering, and generate a decorrelated signal pair.

- Set the parameters, phi and T, which indicate the modulation depth and period for phase.

- Set the filename in sf.read()

- Change the names in sf.wrtie() if there are desired filenames.

- The Inter-channel Cross-Correlation (ICCC) of both decorrelated signals pair and the Impulse Response of the filter will be printed

If there is a intended ICCC value, use sinphasedecorr_iccc.py to adjust the parameters to obtain desired ICCC output.

## Reference 

This algorithm is based on the method proposed in the following papers.

Zotter et al. (2011) PHANTOM SOURCE WIDENING WITH DETERMINISTIC FREQUENCY DEPENDENT TIME DELAYS

Zotter et al. (2013) Efficient Phantom Source Widening