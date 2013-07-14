#! /usr/bin/env python

# Roman-Kana Table for Py3.3
# By MITSUDA Tetsuo

# Roma-ji Table:Hiragana
#---------------------------
ROMANHIRAGANATABLE = {
# A-O
    'A'   :u'\u3042',
    'I'   :u'\u3044',
    'U'   :u'\u3046',
    'E'   :u'\u3048',
    'O'   :u'\u304a',
# K@
    'KA'  :u'\u304b',
    'KI'  :u'\u304d',
    'KU'  :u'\u304f',
    'KE'  :u'\u3051',
    'KO'  :u'\u3053',
# S@
    'SA'  :u'\u3055',
    'SI'  :u'\u3057',
    'SU'  :u'\u3059',
    'SE'  :u'\u305b',
    'SO'  :u'\u305d',
# T@
    'TA'  :u'\u305f',
    'TI'  :u'\u3061',
    'TU'  :u'\u3064',
    'TE'  :u'\u3066',
    'TO'  :u'\u3068',
# N@
    'NA'  :u'\u306a',
    'NI'  :u'\u306b',
    'NU'  :u'\u306c',
    'NE'  :u'\u306d',
    'NO'  :u'\u306e',
# H@
    'HA'  :u'\u306f',
    'HI'  :u'\u3072',
    'HU'  :u'\u3075',
    'HE'  :u'\u3078',
    'HO'  :u'\u307b',
# M@
    'MA'  :u'\u307e',
    'MI'  :u'\u307f',
    'MU'  :u'\u3080',
    'ME'  :u'\u3081',
    'MO'  :u'\u3082',
# Y@
    'YA'  :u'\u3084',
    'YU'  :u'\u3086',
    'YO'  :u'\u3088',
# R@
    'RA'  :u'\u3089',
    'RI'  :u'\u308a',
    'RU'  :u'\u308b',
    'RE'  :u'\u308c',
    'RO'  :u'\u308d',
# W@
    'WA'  :u'\u308f',
    'WI'  :u'\u3046\u3043',
    'WU'  :u'\u3046',
    'WE'  :u'\u3046\u3047',
    'WO'  :u'\u3092',

# NN 

    'NN'  :u'\u3093',

# TSU
    'TSU'  :u'\u3064',
# G@
    'GA'  :u'\u304c',
    'GI'  :u'\u304e',
    'GU'  :u'\u3050',
    'GE'  :u'\u3052',
    'GO'  :u'\u3054',
# Z@
    'ZA'  :u'\u3056',
    'ZI'  :u'\u3058',
    'ZU'  :u'\u305a',
    'ZE'  :u'\u305c',
    'ZO'  :u'\u305e',
# D@
    'DA'  :u'\u3060',
    'DI'  :u'\u3062',
    'DU'  :u'\u3065',
    'DE'  :u'\u3067',
    'DO'  :u'\u3069',
# B@
    'BA'  :u'\u3070',
    'BI'  :u'\u3073',
    'BU'  :u'\u3076',
    'BE'  :u'\u3079',
    'BO'  :u'\u307c',
# P@
    'PA'  :u'\u3071',
    'PI'  :u'\u3074',
    'PU'  :u'\u3077',
    'PE'  :u'\u307a',
    'PO'  :u'\u307d',

# F@
    'FA'  :u'\u3075\u3041',
    'FI'  :u'\u3075\u3043',
    'FU'  :u'\u3075',
    'FE'  :u'\u3075\u3047',
    'FO'  :u'\u3075\u3049',

# C@
    'CA'  :u'\u304b',
    'CI'  :u'\u3057',
    'CU'  :u'\u304f',
    'CE'  :u'\u305b',
    'CO'  :u'\u3053',

# L@
    'LA'  :u'\u3041',
    'LI'  :u'\u3043',
    'LU'  :u'\u3045',
    'LE'  :u'\u3047',
    'LO'  :u'\u3049',
# X@
    'XA'  :u'\u3041',
    'XI'  :u'\u3043',
    'XU'  :u'\u3045',
    'XE'  :u'\u3047',
    'XO'  :u'\u3049',

# KY@
    'KYA' :u'\u304d\u3083',
    'KYI' :u'\u304d\u3043',
    'KYU' :u'\u304d\u3085',
    'KYE' :u'\u304d\u3047',
    'KYO' :u'\u304d\u3087',

# SH@
    'SHA' :u'\u3057\u3083',
    'SHI' :u'\u3057',
    'SHU' :u'\u3057\u3085',
    'SHE' :u'\u3057\u3047',
    'SHO' :u'\u3057\u3087',

# SY@
    'SYA' :u'\u3057\u3083',
    'SYI' :u'\u3057\u3043',
    'SYU' :u'\u3057\u3085',
    'SYE' :u'\u3057\u3047',
    'SYO' :u'\u3057\u3087',

# TY@
    'TYA' :u'\u3061\u3083',
    'TYI' :u'\u3061\u3043',
    'TYU' :u'\u3061\u3085',
    'TYE' :u'\u3061\u3047',
    'TYO' :u'\u3061\u3087',
# CH@
    'CYA' :u'\u3061\u3083',
    'CYI' :u'\u3061\u3043',
    'CYU' :u'\u3061\u3085',
    'CYE' :u'\u3061\u3047',
    'CYO' :u'\u3061\u3087',
# NY@
    'NYA' :u'\u306b\u3083',
    'NYI' :u'\u306b\u3043',
    'NYU' :u'\u306b\u3085',
    'NYE' :u'\u306b\u3047',
    'NYO' :u'\u306b\u3087',

# HY@
    'HYA' :u'\u3072\u3083',
    'HYI' :u'\u3072\u3043',
    'HYU' :u'\u3072\u3085',
    'HYE' :u'\u3072\u3047',
    'HYO' :u'\u3072\u3087',

# MY@
    'MYA' :u'\u307f\u3083',
    'MYI' :u'\u307f\u3043',
    'MYU' :u'\u307f\u3085',
    'MYE' :u'\u307f\u3047',
    'MYO' :u'\u307f\u3087',

# RY@
    'RYA' :u'\u308a\u3083',
    'RYI' :u'\u308a\u3043',
    'RYU' :u'\u308a\u3085',
    'RYE' :u'\u308a\u3047',
    'RYO' :u'\u308a\u3087',

# THI@
    'THA' :u'\u3066\u3083',
    'THI' :u'\u3066\u3043',
    'THU' :u'\u3066\u3085',
    'THE' :u'\u3066\u3047',
    'THO' :u'\u3066\u3087',

# GY@
    'GYA' :u'\u304e\u3083',
    'GYI' :u'\u304e\u3043',
    'GYU' :u'\u304e\u3085',
    'GYE' :u'\u304e\u3047',
    'GYO' :u'\u304e\u3087',
# ZY@
    'ZYA' :u'\u3058\u3083',
    'ZYI' :u'\u3058\u3043',
    'ZYU' :u'\u3058\u3085',
    'ZYE' :u'\u3058\u3047',
    'ZYO' :u'\u3058\u3087',

# JY@
    'JYA' :u'\u3058\u3083',
    'JYI' :u'\u3058\u3043',
    'JYU' :u'\u3058\u3085',
    'JYE' :u'\u3058\u3047',
    'JYO' :u'\u3058\u3087',
    
# J@
    'JA' :u'\u3058\u3083',
    'JI' :u'\u3058',
    'JU' :u'\u3058\u3085',
    'JE' :u'\u3058\u3047',
    'JO' :u'\u3058\u3087',

# DY@
    'DYA' :u'\u3062\u3083',
    'DYI' :u'\u3062\u3043',
    'DYU' :u'\u3062\u3085',
    'DYE' :u'\u3062\u3047',
    'DYO' :u'\u3062\u3087',
# BY@
    'BYA' :u'\u3073\u3083',
    'BYI' :u'\u3073\u3043',
    'BYU' :u'\u3073\u3085',
    'BYE' :u'\u3073\u3047',
    'BYO' :u'\u3073\u3087',
# PY@
    'PYA' :u'\u3074\u3083',
    'PYI' :u'\u3074\u3043',
    'PYU' :u'\u3074\u3085',
    'PYE' :u'\u3074\u3047',
    'PYO' :u'\u3074\u3087',
# FY@
    'FYA' :u'\u3075\u3083',
    'FYI' :u'\u3075\u3043',
    'FYU' :u'\u3075\u3085',
    'FYE' :u'\u3075\u3047',
    'FYO' :u'\u3075\u3087',

# DH@
    'DHA' :u'\u3067\u3083',
    'DHI' :u'\u3067\u3043',
    'DHU' :u'\u3067\u3085',
    'DHE' :u'\u3067\u3047',
    'DHO' :u'\u3067\u3087',

# XY@
    'XYA' :u'\u3083',
    'XYI' :u'\u3043',
    'XYU' :u'\u3085',
    'XYE' :u'\u3047',
    'XYO' :u'\u3087',

# XTU
    'XTU' :u'\u3063',
    

######[NOT TRANSELATE]##########
## V@
#    'VA'  :u'\u30f4\u3041',
#    'VI'  :u'\u30f4\u3043',
#    'VU'  :u'\u30f4',
#    'VE'  :u'\u30f4\u3047',
#    'VO'  :u'\u30f4\u3049',
## VH@
#    'VYA' :u'\u30f4\u3083',
#    'VYI' :u'\u30f4\u3043',
#    'VYU' :u'\u30f4\u3085',
#    'VYE' :u'\u30f4\u3047',
#    'VYO' :u'\u30f4\u3087',
## XWA,LWA
#    'XWA' :u'\u308e',
#    'LWA' :u'\u308e',
#################################
    }

# Nasal "N"
#----------------------------------
ROMANHIRAGANATABLE_NASAL = {
# N
    'N' :u'\u3093',
    }
#----------------------------------

# Geminate : like "T|TE"
ROMANHIRAGANA_GEMINATECONSOANT = [
'K','S','T','H','M','Y','R','W',
'G','Z','J','D','B',
'P','F','C','L','X',
#'V',
]


# Geminate string : 'LTU'
HIRAGANA_GEMINATESTRING = u'\u3063'

#---------------------------

# Roma-ji Table:Hiragana
#---------------------------
ROMANKATAKANATABLE = {
# A-O
    'A'   :u'\u30a2',
    'I'   :u'\u30a4',
    'U'   :u'\u30a6',
    'E'   :u'\u30a8',
    'O'   :u'\u30aa',
# K@
    'KA'  :u'\u30ab',
    'KI'  :u'\u30ad',
    'KU'  :u'\u30af',
    'KE'  :u'\u30b1',
    'KO'  :u'\u30b3',
# S@
    'SA'  :u'\u30b5',
    'SI'  :u'\u30b7',
    'SU'  :u'\u30b9',
    'SE'  :u'\u30bb',
    'SO'  :u'\u30bd',
# T@
    'TA'  :u'\u30bf',
    'TI'  :u'\u30c1',
    'TU'  :u'\u30c4',
    'TE'  :u'\u30c6',
    'TO'  :u'\u30c8',
# N@
    'NA'  :u'\u30ca',
    'NI'  :u'\u30cb',
    'NU'  :u'\u30cc',
    'NE'  :u'\u30cd',
    'NO'  :u'\u30ce',
# H@
    'HA'  :u'\u30cf',
    'HI'  :u'\u30d2',
    'HU'  :u'\u30d5',
    'HE'  :u'\u30d8',
    'HO'  :u'\u30db',
# M@
    'MA'  :u'\u30de',
    'MI'  :u'\u30df',
    'MU'  :u'\u30e0',
    'ME'  :u'\u30e1',
    'MO'  :u'\u30e2',
# Y@
    'YA'  :u'\u30e4',
    'YU'  :u'\u30e6',
    'YO'  :u'\u30e8',
# R@
    'RA'  :u'\u30e9',
    'RI'  :u'\u30ea',
    'RU'  :u'\u30eb',
    'RE'  :u'\u30ec',
    'RO'  :u'\u30ed',
# W@
    'WA'  :u'\u30ef',
    'WI'  :u'\u30a6\u30a3',
    'WU'  :u'\u30a6',
    'WE'  :u'\u30a6\u30a7',
    'WO'  :u'\u30f2',

# NN 

    'NN'  :u'\u30f3',

# TSU
    'TSU'  :u'\u30c4',

# G@
    'GA'  :u'\u30ac',
    'GI'  :u'\u30ae',
    'GU'  :u'\u30b0',
    'GE'  :u'\u30b2',
    'GO'  :u'\u30b4',
# Z@
    'ZA'  :u'\u30b6',
    'ZI'  :u'\u30b8',
    'ZU'  :u'\u30ba',
    'ZE'  :u'\u30bc',
    'ZO'  :u'\u30be',
# D@
    'DA'  :u'\u30c0',
    'DI'  :u'\u30c2',
    'DU'  :u'\u30c5',
    'DE'  :u'\u30c7',
    'DO'  :u'\u30c9',
# B@
    'BA'  :u'\u30d0',
    'BI'  :u'\u30d3',
    'BU'  :u'\u30d6',
    'BE'  :u'\u30d9',
    'BO'  :u'\u30dc',
# P@
    'PA'  :u'\u30d1',
    'PI'  :u'\u30d4',
    'PU'  :u'\u30d7',
    'PE'  :u'\u30da',
    'PO'  :u'\u30dd',

# F@
    'FA'  :u'\u30d5\u30a1',
    'FI'  :u'\u30d5\u30a3',
    'FU'  :u'\u30d5',
    'FE'  :u'\u30d5\u30a7',
    'FO'  :u'\u30d5\u30a9',

# C@
    'CA'  :u'\u30ab',
    'CI'  :u'\u30b7',
    'CU'  :u'\u30af',
    'CE'  :u'\u30bb',
    'CO'  :u'\u30b3',

# L@
    'LA'  :u'\u30a1',
    'LI'  :u'\u30a3',
    'LU'  :u'\u30a5',
    'LE'  :u'\u30a7',
    'LO'  :u'\u30a9',
# X@
    'XA'  :u'\u30a1',
    'XI'  :u'\u30a3',
    'XU'  :u'\u30a5',
    'XE'  :u'\u30a7',
    'XO'  :u'\u30a9',

# KY@
    'KYA' :u'\u30ad\u30e3',
    'KYI' :u'\u30ad\u30a3',
    'KYU' :u'\u30ad\u30e5',
    'KYE' :u'\u30ad\u30a7',
    'KYO' :u'\u30ad\u30e7',

# SH@
    'SHA' :u'\u30b7\u30e3',
    'SHI' :u'\u30b7',
    'SHU' :u'\u30b7\u30e5',
    'SHE' :u'\u30b7\u30a7',
    'SHO' :u'\u30b7\u30e7',

# SY@
    'SYA' :u'\u30b7\u30e3',
    'SYI' :u'\u30b7\u30a3',
    'SYU' :u'\u30b7\u30e5',
    'SYE' :u'\u30b7\u30a7',
    'SYO' :u'\u30b7\u30e7',

# TY@
    'TYA' :u'\u30c1\u30e3',
    'TYI' :u'\u30c1\u30a3',
    'TYU' :u'\u30c1\u30e5',
    'TYE' :u'\u30c1\u30a7',
    'TYO' :u'\u30c1\u30e7',
# CH@
    'CYA' :u'\u30c1\u30e3',
    'CYI' :u'\u30c1\u30a3',
    'CYU' :u'\u30c1\u30e5',
    'CYE' :u'\u30c1\u30a7',
    'CYO' :u'\u30c1\u30e7',
# NY@
    'NYA' :u'\u30cb\u30e3',
    'NYI' :u'\u30cb\u30a3',
    'NYU' :u'\u30cb\u30e5',
    'NYE' :u'\u30cb\u30a7',
    'NYO' :u'\u30cb\u30e7',

# HY@
    'HYA' :u'\u30d2\u30e3',
    'HYI' :u'\u30d2\u30a3',
    'HYU' :u'\u30d2\u30e5',
    'HYE' :u'\u30d2\u30a7',
    'HYO' :u'\u30d2\u30e7',

# MY@
    'MYA' :u'\u30df\u30e3',
    'MYI' :u'\u30df\u30a3',
    'MYU' :u'\u30df\u30e5',
    'MYE' :u'\u30df\u30a7',
    'MYO' :u'\u30df\u30e7',

# RY@
    'RYA' :u'\u30ea\u30e3',
    'RYI' :u'\u30ea\u30a3',
    'RYU' :u'\u30ea\u30e5',
    'RYE' :u'\u30ea\u30a7',
    'RYO' :u'\u30ea\u30e7',

# THI@
    'THA' :u'\u30c6\u30e3',
    'THI' :u'\u30c6\u30a3',
    'THU' :u'\u30c6\u30e5',
    'THE' :u'\u30c6\u30a7',
    'THO' :u'\u30c6\u30e7',

# GY@
    'GYA' :u'\u30ae\u30e3',
    'GYI' :u'\u30ae\u30a3',
    'GYU' :u'\u30ae\u30e5',
    'GYE' :u'\u30ae\u30a7',
    'GYO' :u'\u30ae\u30e7',
# ZY@
    'ZYA' :u'\u30b8\u30e3',
    'ZYI' :u'\u30b8\u30a3',
    'ZYU' :u'\u30b8\u30e5',
    'ZYE' :u'\u30b8\u30a7',
    'ZYO' :u'\u30b8\u30e7',

# JY@
    'JYA' :u'\u30b8\u30e3',
    'JYI' :u'\u30b8\u30a3',
    'JYU' :u'\u30b8\u30e5',
    'JYE' :u'\u30b8\u30a7',
    'JYO' :u'\u30b8\u30e7',

# J@
    'JA' :u'\u30b8\u30e3',
    'JI' :u'\u30b8',
    'JU' :u'\u30b8\u30e5',
    'JE' :u'\u30b8\u30a7',
    'JO' :u'\u30b8\u30e7',

# DY@
    'DYA' :u'\u30c2\u30e3',
    'DYI' :u'\u30c2\u30a3',
    'DYU' :u'\u30c2\u30e5',
    'DYE' :u'\u30c2\u30a7',
    'DYO' :u'\u30c2\u30e7',
# BY@
    'BYA' :u'\u30d3\u30e3',
    'BYI' :u'\u30d3\u30a3',
    'BYU' :u'\u30d3\u30e5',
    'BYE' :u'\u30d3\u30a7',
    'BYO' :u'\u30d3\u30e7',
# PY@
    'PYA' :u'\u30d4\u30e3',
    'PYI' :u'\u30d4\u30a3',
    'PYU' :u'\u30d4\u30e5',
    'PYE' :u'\u30d4\u30a7',
    'PYO' :u'\u30d4\u30e7',
# FY@
    'FYA' :u'\u30d5\u30e3',
    'FYI' :u'\u30d5\u30a3',
    'FYU' :u'\u30d5\u30e5',
    'FYE' :u'\u30d5\u30a7',
    'FYO' :u'\u30d5\u30e7',

# DH@
    'DHA' :u'\u30c7\u30e3',
    'DHI' :u'\u30c7\u30a3',
    'DHU' :u'\u30c7\u30e5',
    'DHE' :u'\u30c7\u30a7',
    'DHO' :u'\u30c7\u30e7',

# XY@
    'XYA' :u'\u30e3',
    'XYI' :u'\u30a3',
    'XYU' :u'\u30e5',
    'XYE' :u'\u30a7',
    'XYO' :u'\u30e7',

# XTU
    'XTU' :u'\u30c3',
    
# V@
    'VA'  :u'\u30f4\u30a1',
    'VI'  :u'\u30f4\u30a3',
    'VU'  :u'\u30f4',
    'VE'  :u'\u30f4\u30a7',
    'VO'  :u'\u30f4\u30a9',
# VH@
    'VYA' :u'\u30f4\u30e3',
    'VYI' :u'\u30f4\u30a3',
   'VYU' :u'\u30f4\u30e5',
    'VYE' :u'\u30f4\u30a7',
    'VYO' :u'\u30f4\u30e7',

######[NOT TRANSELATE]##########
## XWA,LWA
#    'XWA' :u'\u30ee',
#    'LWA' :u'\u30ee',
#################################
    }


# Nasal "N"
#----------------------------------
ROMANKATAKANATABLE_NASAL = {
# N
    'N' :u'\u30f3',
    }
#----------------------------------

# Geminate : like "T|TE"
ROMANKATAKANA_GEMINATECONSOANT = [
'K','S','T','H','M','Y','R','W',
'G','Z','J','D','B',
'P','F','C','L','X',
'V',
]


# Geminate string : 'LTU'
KATAKANA_GEMINATESTRING = u'\u30c3'


####################################
# class:RomaKanaTable
#
class RomaKanaTable:
    
    kanatable = []
    naseltable = {}
    geminatelist = []
    geminatestring = ""
    normal_max = 0
    rklist = []
    tpflag = False

    #---------------------------------------------------------------------
    # INIT
    def init(self):
        self.kanatable = []
        self.naseltable = {}
        self.geminatelist = []
        self.geminatestring = ""
        self.normal_max = 0
        self.rklist = []
        self.tpflag = False

    #---------------------------------------------------------------------
    # Make kana table
    def makeTable(self,normal,nasel,geminate,gemistr):

        self.init();
        # normal
        self.normal_max = 0
        for x in normal:
            if( len(x) > self.normal_max):
                self.normal_max = len(x) 

        if( self.normal_max == 0):
           return None

        for x in range(self.normal_max):
            self.kanatable.append({})

        for x in normal:
            l = len(x)
            if(l > 0 ):
                if x in self.kanatable[l-1]:
                    print( u"Already registed...")
                else:
                    self.kanatable[l-1][x] = normal[x]

        # nasel
        if( len(nasel) == 0 ):
            return None 
        for x in nasel:
            self.naseltable[x] = nasel[x]

        # geminate
        if( len(geminate) == 0 ):
            return None 
        for x in geminate:
            self.geminatelist.append(x)
        
        # gemistr
        # (xtu,ltu)
        self.geminatestring = gemistr

    #---------------------------------------------------------------------
    # Roma-ji to Kana conversion (1line)
    def convertline(self,s):
        l = len(s)
        c = 0
        p = ""
        
        self.rklist = []
        
        if(self.normal_max == 0 ):
            return
        
        while(c < l):
           ss = s[c:c+self.normal_max]
           if( len(ss) == 0 ):
               break
           (sa,sb,sc,sd)=self.convert(ss,p)
           if( (len(sc) > 0) & (sc == p) ):
               # Delete a character from end-of-list.
               # (like "T|TE" pattern)
               self.rklist.pop()
           
           self.rklist.append((sc+sa,sb))
           
           if( len(sb) > 0):
               # Hit-it!!
               c = c+len(sa)
               p= ""
           else:
               
               p = ss[0:1]
               c = c+1
        return( self.rklist )
    #---------------------------------------------------------------------
    # Roma-ji to Kana conversion:Geminate
    # ms = "KA" , rs= "K" -> "K|KA"="\u3063\u304b"
    def convert(self,ms,rs):
        sa = "" # roman
        sb = "" # kana
        sc = "" # ganinmate 
        sd = "" # n/c
        f = False
        # evaluate : 3 ,2, 1 characters string.
        for i in range(self.normal_max,0,-1):
            sa =ms[0:i]
            if( sa in self.kanatable[i-1] ):
               sb = self.kanatable[i-1][sa]
               break
        
        # HIT
        if( len(sb) > 0 ):
            sc = ""
            
            # Geminate 1
            for x in self.geminatelist:
                if( x == rs ):
                    f = True
            
            # Geminate 2
            if( (sa[0:1] == rs) & f):
                sb =self.geminatestring + sb
                sc = rs
        elif(sa in self.naseltable):
            # "n" , Same as "NN", but this is special!!
            sb = self.naseltable[sa]
        else:
            sd =ms[0:1]
            
        return((sa,sb,sc,sd))

    #---------------------------------------------------------------------
    # Get Kana string
    # 
    def getkana(self,r_t,o):
        lst = self.convertline(r_t)
        h_t = ""
        for (x,y) in lst:
            if(o):
                c = y
            else:
                c=( y if len(y) != 0 else x ) # (>Py2.5)
            
            h_t = h_t + c
        
        return(h_t)

def getkana(myText,k,o):
    ht = RomaKanaTable()
    ht.init()

    if(k):
        ht.makeTable(ROMANKATAKANATABLE,ROMANKATAKANATABLE_NASAL,
                     ROMANKATAKANA_GEMINATECONSOANT,KATAKANA_GEMINATESTRING)
    else:
        ht.makeTable(ROMANHIRAGANATABLE,ROMANHIRAGANATABLE_NASAL,
                     ROMANHIRAGANA_GEMINATECONSOANT,HIRAGANA_GEMINATESTRING)
    
    return(ht.getkana(myText,o))
    
    
#####
# Main
if __name__=='__main__':
    ht = RomaKanaTable()
    ht.init()
    ht.makeTable(ROMANHIRAGANATABLE,ROMANHIRAGANATABLE_NASAL,
                 ROMANHIRAGANA_GEMINATECONSOANT,HIRAGANA_GEMINATESTRING)
    #print ht.kanatable

    for x in ["KONNNITIWA","SUTTAMONDA","XXYULLUYYU","!@AS#SA"]:
        ht.convertline(x)
        a = ""
        b = ""
        c = ""
        # Test
        for (y,z) in ht.rklist:
            a = a+"|"+y
            b = b+"|"+z
            c = c+( z if len(z) != 0 else y ) # (>Py2.5)
        print( x,"->",a ,"=" , b ," (",c,")" )