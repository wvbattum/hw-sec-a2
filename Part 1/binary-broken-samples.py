import hashlib

# we used this file to generate the samples

OUTPUT_SAMPLES_FILE_NAME = 'Part 1/broken_sample.bin'
NUMBERS = 20000

output_samples = open(OUTPUT_SAMPLES_FILE_NAME, 'wb')

for count in range(0, NUMBERS):
    output_samples.write(hashlib.sha256(bytes(count)).digest()[:4])

output_samples.close()