import re
import pysrt
from openpyxl import Workbook
import os

# Function to detect if a word is too long
def word_too_long(text):
    return any(len(word) > 13 for word in text.split())

# Function to detect if there is only one word
def one_word(text):
    return len(text.split()) == 1

# Function to detect three successive identical letters
def three_successive_letters(text):
    return bool(re.search(r'\b(\w)\1{2,}\b', text))

# Function to detect a single letter (except 'و')
def one_letter(text):
    return bool(re.search(r'\b(?![و])\w\b', text))

# Function to detect certain keywords related to numbers
def maybe_numbers_missing(text):
    return bool(re.search(r'\b(رقم|عدد|عنوان|جنيه|ريال)\b', text))

# Function to detect repetitions within a phrase
def repetition(text):
    return bool(re.search(r'\b(\S+(\s+\S+)*)\s+\1\b', text))

def detect_alerts(subs):
    alerts = []
    for sub in subs:
        if word_too_long(sub.text):
            alerts.append({
                'Alert Type': 'Word too long',
                'Phrase': sub.text,
                'Timecode': f"{sub.start} --> {sub.end}"
            })
        if one_word(sub.text):
            alerts.append({
                'Alert Type': 'One word',
                'Phrase': sub.text,
                'Timecode': f"{sub.start} --> {sub.end}"
            })
        if three_successive_letters(sub.text):
            alerts.append({
                'Alert Type': 'Three successive letters',
                'Phrase': sub.text,
                'Timecode': f"{sub.start} --> {sub.end}"
            })
        if one_letter(sub.text):
            alerts.append({
                'Alert Type': 'One letter',
                'Phrase': sub.text,
                'Timecode': f"{sub.start} --> {sub.end}"
            })
        if maybe_numbers_missing(sub.text):
            alerts.append({
                'Alert Type': 'Maybe numbers are missing',
                'Phrase': sub.text,
                'Timecode': f"{sub.start} --> {sub.end}"
            })
        if repetition(sub.text):
            alerts.append({
                'Alert Type': 'Repetition',
                'Phrase': sub.text,
                'Timecode': f"{sub.start} --> {sub.end}"
            })
    return alerts

def generate_excel(alerts):
    wb = Workbook()
    ws = wb.active
    ws.append(['Alert Type', 'Phrase', 'Timecode'])
    
    for alert in alerts:
        ws.append([alert['Alert Type'], alert['Phrase'], alert['Timecode']])
    
    excel_file_name = "alerts.xlsx"
    wb.save(excel_file_name)
    print(f"Alerts have been saved to '{excel_file_name}'.")

def main():
    file_path = 'C:\\Users\\userfl\\Desktop\\tist\\Test (1).srt'
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' could not be found.")
        
        subs = pysrt.open(file_path, encoding='utf-8')
        if subs:
            alerts = detect_alerts(subs)
            generate_excel(alerts)
        else:
            print(f"Error: No subtitles found in '{file_path}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
