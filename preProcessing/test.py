import csv
import sys
import os
import json


proj_name = sys.argv[1]
data_path='../GetSmells/getsmells-output/smells/{}/'.format(proj_name)
subfolders = [ f.path for f in os.scandir(data_path) if f.is_dir() ]

data=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]

index = 2
index_dict = {}

for folder in subfolders:
    csv_file_path = os.path.join(folder,'smells-classes.csv')
    if(os.path.exists(csv_file_path)):
        folder_name = folder.split('/')[-1]
        data.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    name_list = row[0].split('.')

                    for i in range(len(name_list)):
                        if i == 0:
                            temp = name_list[i]
                            name_list[i]= os.path.join(f'{proj_name}/{folder_name}/{temp}')
                        else:
                            temp = name_list[i]
                            name_list[i] = os.path.join(name_list[i-1],temp)


                    for i in range(len(name_list)):
                        if i == 0:
                            if name_list[i] in index_dict:
                                continue
                            data.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            index_dict[name_list[i]]=1
                        elif i == len(name_list)-1:

                            total_smell = 0 
                            for j in range(1,12):
                                total_smell += int(row[j])

                            if name_list[i] in index_dict:
                                idx = data.index([name_list[i],name_list[i-1],0,0])
                                data[idx] = [name_list[i],name_list[i-1],total_smell,0]
                            else:
                                data.append([name_list[i],name_list[i-1],total_smell,0])
                                index_dict[name_list[i]]=1
                        else:
                            if name_list[i] in index_dict:
                                continue
                            data.append([name_list[i],name_list[i-1],0,0])
                            index_dict[name_list[i]]=1
                    line_count += 1

# Serializing json  
json_object = json.dumps(data, indent = 2) 
  
# Writing to sample.json 
with open("../detailedClass/data.json", "w") as outfile: 
    outfile.write(json_object) 