import fetch
import extract
import userConfig
import constants

import os
import csv
from datetime import date
from shutil import copyfile

'''
In this module, make reviewbook as userConfig.py
'''

# get search history data
rawHistory = fetch.getFromGoogleAccountHistoryFile(userConfig.GOOGLE_ACCOUNT_HISTORY_URL)

# url of reviewbook(output file)
reviewbookUrl = os.path.join(userConfig.OUTPUT_PATH, userConfig.REVIEWBOOK_FILENAME + '.' + userConfig.REVIEWBOOK_FORMAT)

# if already reviewbook file exist
if os.path.exists(reviewbookUrl):
    # if backup setting is on,
    if userConfig.DO_BACKUP:
        # do backup
        backupFileUrl = os.path.join(userConfig.BACKUP_PATH, userConfig.REVIEWBOOK_FILENAME + str(date.today()) + '.' + userConfig.REVIEWBOOK_FORMAT)
        copyfile(reviewbookUrl, backupFileUrl)

    # extract new word search record(comparing search date).
    with open(reviewbookUrl, 'r', newline='', encoding='UTF-8') as reviewbook:
        newWordRecs = extract.getNewRecsCompDate(csv.reader(reviewbook), rawHistory)
    
    # extract word search record as word status(memorized, not memorized, etc.)
    with open(reviewbookUrl, 'r', newline='', encoding='UTF-8') as reviewbook:
        notMemorizedWordRecs, excludedWordRecs, memorizedWordRecs, onceMemorizedWordRecs = extract.getRecsAsMemorizedSymbol(csv.reader(reviewbook))
    
    # make reviewbook
    with open(reviewbookUrl, 'w', newline='', encoding='UTF-8') as reviewbook:
        writer = csv.writer(reviewbook)
        writer.writerow(constants.FIELDS)
        writer.writerows(newWordRecs)
        writer.writerows(notMemorizedWordRecs)
        writer.writerows(excludedWordRecs)
        writer.writerows(memorizedWordRecs)
        writer.writerows(onceMemorizedWordRecs)
    

# if reviewbook file doesn't exist
else:
    # extract all search word
    wordRecs = extract.getRecs(rawHistory)

    # make reviewbook
    with open(reviewbookUrl, 'w', newline='', encoding='UTF-8') as reviewbook:
        writer = csv.writer(reviewbook)
        writer.writerow(constants.FIELDS)
        writer.writerows(wordRecs)