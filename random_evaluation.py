import json
import numpy as np
import cPickle as pickle
import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        while True:
            rand = random.randint(start, stop)
            if rand not in random_list:
                random_list.append(rand)
                break
    return random_list


path = './annotations/test_annotation.pkl'# reading annotations

with open(path, 'rb') as f:
	partitions = pickle.load(f)
test_im_names = partitions['test_im_names']

color_label = partitions['color_label']
type_label = partitions['type_label']
sky_label = partitions['sky_label']

bumper_label = partitions['bumper_label']
wheel_label = partitions['wheel_label']
luggage_label = partitions['luggage_label']
d_part_label = partitions['d_part_label']

query_order = partitions['query_order']
gallery_order = partitions['gallery_order']

reid_result = []

for i in range(len(query_order)): # generate random submission
    reid_result.append({"query_id": i, "ans_ids": random_int_list(0,len(gallery_order)-1,1000)})
    print('Generating Random Submission of Query Image {query_id}'.format(query_id = i))
results = {'reid_result':reid_result}
    
with open("./submission_random.json", "w") as f:
  f.write(json.dumps(results).decode('unicode-escape')) 
