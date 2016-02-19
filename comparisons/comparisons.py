import csv
import random

# waveform types: 'impulse', 'random', 'sine'
waveform_type = 'random'

# come up with some data to start
sample_history = []
sample_num = []

if waveform_type == 'impulse':
    # give enough samples to initialize
    for i in range(16):
        sample_history.append(0)
        sample_num.append(len(sample_num))

    # then give enough samples to filter effectively
    for i in range(64):
        sample_history.append(32767)
        sample_num.append(len(sample_num))

else:
    sample_history = [random.randint(0,32768) for i in range(0, 80)]
    sample_num = [e for e in range(0, 80)]

# standard moving average
moving_avg_array = []
moving_avg_depth = 16
for i, sample in enumerate(sample_history):
    if i < (moving_avg_depth - 1):
        # initialization of the filter
        moving_avg_array.append(sample_history[0])
    else:
        new_accum = 0
        for j in range(0,moving_avg_depth):
            new_accum += sample_history[i-j]
        moving_avg_array.append(new_accum/moving_avg_depth)

# perform the moving average filter on them
moving_avg_lean = []
accum = 0
avg = 0
for sample in sample_history:
    accum += sample
    accum -= avg
    avg = accum >> 3
    moving_avg_lean.append(avg)

rows = []
for i, enumerate in enumerate(sample_num):
    rows.append([sample_num[i], sample_history[i], moving_avg_array[i], moving_avg_lean[i]])

with open('data.csv', 'wb') as f:
    my_writer = csv.writer(f)
    my_writer.writerows(rows)
