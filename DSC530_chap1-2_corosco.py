#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:12:49 2020

@author: corosco

"""


import thinkstats2
from collections import defaultdict

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.
    dct_file: string file name
    dat_file: string file name
    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    """CleanFemResp(df)"""
    return df

def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    """CleanFemPreg(df)"""
    return df

def MakePregMap(df):
    """Make a map from caseid to list of preg indices.

    df: DataFrame

    returns: dict that maps from caseid to list of indices into `preg`
    """
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid]
    return d    
    
def ValidatePregnum(resp, preg):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    preg: pregnancy DataFrame
    """
    # make the map from caseid to list of pregnancy indices
    preg_map = MakePregMap(preg)
    
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print('Inconsistent values in Resp and Preg files')
            print(f'CASEID: {caseid}, Nbr in preg file: {len(indices)}, Nbr in Resp file: {pregnum}')
            return False
    return True

def main():
    resp = ReadFemResp()
    preg = ReadFemPreg()
    # Print out Value Counts for Resp.pregnum
    print('Value Counts for pregnum')
    print(resp.pregnum.value_counts().sort_index())
    # Cross-Validate Resp and Preg and compare pregnum with preg file
    status = ValidatePregnum(resp, preg)
    print(f'Cross validate Resp and Preg files Result: {status}')
    
        
main()