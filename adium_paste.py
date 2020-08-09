import subprocess as s
import re


def get_clip():
    return s.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')


def get_case_details():
    clip = get_clip()
    case_pattern = re.compile(r'F-CS-\d+')
    case_no = re.search(case_pattern, clip)
    if case_no:
        case_no = case_no.group(0)
    else:
        print('No F-CS case number found :(')
    parsed = str(clip).splitlines()
    subject = parsed[4]
    return case_no, subject


def write_to_clip(output):
    process = s.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=s.PIPE)
    process.communicate(output.encode('utf-8'))


case_no = get_case_details()[0]
subject = get_case_details()[1]

output = case_no + ' ' + subject

write_to_clip(output)
print(output)
