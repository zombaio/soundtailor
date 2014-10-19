#!/usr/bin/env python
'''
@file utilities.py
@brief Various utilities for SoundTailor related Python scripts
@author gm
@copyright gm 2014

This file is part of SoundTailor

SoundTailor is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SoundTailor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with SoundTailor.  If not, see <http://www.gnu.org/licenses/>.
'''

'''
Note that all of this mimics C++ code for testing/prototyping purpose.
Hence it may not really seems "pythonic" and not intended to be in any way.
'''

import numpy
import time

from scipy import signal
from scipy.io.wavfile import write

def GenerateData(freq_low, freq_high, length, sampling_freq):
    '''
    Simple chirp synthesis
    '''
    end_time_s = float(length) / sampling_freq

    time = numpy.arange(0,
                        end_time_s,
                        1.0 / sampling_freq)
    return signal.chirp(t = time,
                        f0 = freq_low,
                        t1 = end_time_s,
                        f1 = freq_high)

def GetMetadata(signal):
    '''
    Get signal basic metadata such as sum, mean etc.

    Return a tuple organized as follows:
    ((text, value)
     ...
     (text, value))
    '''
    return (("Length: ", len(signal)),
            ("Sum: ", numpy.sum(signal)),
            ("Min: ", numpy.min(signal)),
            ("Max: ", numpy.max(signal)),
            ("Mean: ", numpy.mean(signal)),
            ("Var: ", numpy.var(signal)),
            ("RMS: ", numpy.sqrt(numpy.sum(signal ** 2) / len(signal))))

def PrintMetadata(metadatas):
    '''
    Print signal metadata extracted before

    Return a string organized as follows:
    text value ... text value
    '''
    output_str = ""
    for metadata in metadatas:
        output_str += metadata[0] + str(metadata[1])
        output_str += " "
    return output_str

def ZeroCrossings(signal):
    '''
    Return an array holding all indexes before which the input signal crosses zero
    '''
    return numpy.where(numpy.diff(numpy.sign(signal)))[0]

def Diff(signal):
    '''
    Return the differentiated input signal
    '''
    return signal[1:len(signal)] - signal[0:len(signal) - 1]

def WriteWav(signal, filename, sampling_rate):
    '''
    Save input signal as a wav file
    '''
    return write(filename + ".wav",
                            sampling_rate,
                            ((signal * 32768) - 1.0).astype(numpy.int16))

class Chrono(object):
    '''
    Simplistic chrono utility relying on time
    '''
    def __init__(self):
        self._time_before = time.time()

    def GetElapsed(self):
        return time.time() - self._time_before

def PrintTiming(func):
    '''
    Helper for returning the execution time for a function
    Implemented as a decorator
    '''
    def wrapper(*arg):
        chrono = Chrono()
        res = func(*arg)
        print func.func_name + " took " + str(chrono.GetElapsed() * 1000.0) + " ms"
        return res

    return wrapper
