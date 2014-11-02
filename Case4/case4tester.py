#
# case4tester.py
#
import sqlite3
from case4 import *


con = sqlite3.connect('tobaccoSEC19942002.sqlite')
cur = con.cursor()

ap = open('ap.txt').read()
reuters = open('reuters.txt').read()

#test kwicn:
print('\n\ntest function kwicn ---------------------')
for item in kwicn('of',ap, 3):
    print(item)
    

#test dbkwicn:
print('\n\ntest function dbkwicn ---------------------')
for item in dbkwicn(cur, 13, 'tobacco', 3):
    print(item)

#test listOfFirms:
print('\n\ntest function listOfFirms ---------------------')
print(listOfFirms(cur))

#test listOfRTypes:
print('\n\ntest function listOfFirms ---------------------')
print(listOfRTypes(cur))

#test listOfYears:
print('\n\ntest function listOfYears ---------------------')
print(listOfYears(cur))

#test getConceptList:
print('\n\ntest function getConceptList ---------------------')
print(getConceptList('giving'))

#test scoreDocConceptCountScore:
print('\n\ntest function scoreDocConceptCountScore ---------------------')
print(scoreDocConceptCountScore(reuters, 'junk'))

#test scoreDocGroup:
print('\n\ntest function scoreDocGroup ---------------------')
print(scoreDocGroup('Altria',1996, '10-Qs','giving', cur))

#test timeScores:
print('\n\ntest function timeScores ---------------------')
print(timeScores('Altria',range(1994,2003), '10-Qs','junk', cur))

#test timeScoresIndustryReport
print('\n\ntest function timeScoresIndustryReport ---------------------')
timeScoresIndustryReport('tobacco_products', cur)
