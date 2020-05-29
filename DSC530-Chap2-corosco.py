"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    Modifed by corosco for Chapter 2 exercises"""
from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    p, x = max([(p, x) for x, p in hist.Items()])
    return x


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)


def WeightDifference(live, firsts, others):
    """Explore the difference in weight between first babies and others.

    live: DataFrame of all live births
    firsts: DataFrame of first babies
    others: DataFrame of others
    """
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    print('Mean')
    print('First babies', mean1)
    print('Others', mean2)

    print('Variance')
    print('First babies', var1)
    print('Others', var2)

    print('Difference in lbs', mean1 - mean2)
    print('Difference in oz', (mean1 - mean2) * 16)

    print('Difference relative to mean (%age points)', 
          (mean1 - mean2) / mean0 * 100)

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)
    
    """corosco Mar 27 2020 - Added Code for 2-1 and 2-4"""
    
    # difference between Cohen's d to the difference between the means of the total
    # weights
    print("************** Difference between mean and cohen' d ***********")
    mean_delta = mean2 - mean1
    print(f'Delta beween the weight means: {mean_delta}')
    
    cohen_diff = mean_delta - d
    print(f'Delta between Cohens d and Delta Mean: {cohen_diff}')
    print("************** End Difference between mean and cohen' d *************")
    return
    
def LengthDifference(live, firsts, others):
    """Code added to explore the differences in pregnancy lengths.
    corosco Mar 27th 2020 Ex. 2-1, 2-4"""
    
    mean0 = live.prglngth.mean()
    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()
    std0 = live.prglngth.std()
    std1 = firsts.prglngth.std()
    std2 = others.prglngth.std()


    print('**************Explore Pregnancy Lengths***************')
    print(f'Mean Length of all pregancies: {mean0}')
    print(f'Mean Length of first pregancies: {mean1}')
    print(f'Mean Length of others pregancies: {mean2}')
    print(f'Std deviation of total pregnancy lengths is: {std0}')
    print(f'Std deviation of Firsts pregnancy lengths is: {std1}')
    print(f'Std deviation of Others pregnancy lengths is: {std2}')
    
    # Compute Cohen's d for pregnancy length
    len_d = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)
    print(f'Cohen d for  pregnancy length: {len_d}')
    
    # Compute delta between mean and cohen's d
    mean_delta = mean1 - mean2
    print(f'Delta beween the length means: {mean_delta}')
    cohen_d = mean_delta - len_d
    print(f'Delta between Cohens d and mean_delta: {cohen_d}')
    print('*****************nEnd Explore Pregnancy Lengths **************')
    return 
    
def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # explore the weight difference between first babies and others
    WeightDifference(live, firsts, others)
    
    """ Code added corosco Mar 27 2020 - Explore
    prgenancy lengths Ex 2-1, 2-4"""
    LengthDifference(live, firsts, others)
    
    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)
    
    


if __name__ == '__main__':
    main(*sys.argv)
