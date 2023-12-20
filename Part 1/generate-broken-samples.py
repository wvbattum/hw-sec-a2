import re

RANDOM_SAMPLES_FILE_NAME = 'Part 1/samples.txt'
OUTPUT_SAMPLES_FILE_NAME = 'Part 1/samples_out.txt'
COPY_LINES = 10

random_samples_file = open(RANDOM_SAMPLES_FILE_NAME, 'r')
random_samples_lines = random_samples_file.readlines()

output_samples = open(OUTPUT_SAMPLES_FILE_NAME, 'w')

count = 0
reg_inst = re.compile('\s*\d+.*')
line_to_copy = ''
for line in random_samples_lines:
    if count == 0:
        if reg_inst.match(line):
            line_to_copy = line
            count += 1
    if COPY_LINES > count > 0:
        # copy specific set line
        output_samples.write(line_to_copy)
        count += 1
    else:
        # copy current line
        output_samples.write(line)

output_samples.close()