import json
import os

image_folder_path = "flickr30k-images"
caption_folder_path = "flickr30k/results_20130124.token"

image_list = os.listdir(image_folder_path)

with open(caption_folder_path,'r') as f:
    content = f.read().split('\n')


dictionary = {}
for i in range(0, len(content), 5):
    image_name = content[i].split('#')[0]
    ls = []
    for j in range(i, i+5):
        caption = content[j].split(maxsplit=1)[-1]
        ls.append(caption)
    
    ls.append(os.path.join(image_folder_path, image_name))
    dictionary[image_name] = ls

f.close()


# train set
with open('train.txt', 'r') as f:
    content = f.read().split('\n')

train_list = [i + '.jpg' for i in content]
train_dict = {k:dictionary[k] for k in train_list if k in dictionary}
f1 = open("train.json", "w")
json.dump(train_dict, f1, indent=4)
f1.close()
f.close()

print("Successfully split train set!")

# validation set
with open('validation.txt', 'r') as f:
    content = f.read().split('\n')

validation_list = [i + '.jpg' for i in content]
validation_dict = {k:dictionary[k] for k in validation_list if k in dictionary}
f1 = open("validation.json", "w")
json.dump(validation_dict, f1, indent=4)
f1.close()
f.close()

print("Successfully split validation set!")


# test set
with open('test.txt', 'r') as f:
    content = f.read().split('\n')

test_list = [i + '.jpg' for i in content]
test_dict = {k:dictionary[k] for k in test_list if k in dictionary}
f1 = open("test.json", "w")
json.dump(test_dict, f1, indent=4)
f1.close()
f.close()

print("Successfully split test set!")





