import csv
import sys
import os
import json


proj_name = sys.argv[1]
data_path='./GetSmells/getsmells-output/smells/{}/'.format(proj_name)
subfolders = [ f.path for f in os.scandir(data_path) if f.is_dir() ]

array_classlevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]

array_methodlevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]

pieChartArray = [
  ['Smell Name', 'Count'],
  ['packageLevel', 0],
  ['classLevel', 0],
  ['methodLevel', 0]
]


index_dict_class = {}
index_dict_method = {}

for folder in subfolders:
    smells_classes = os.path.join(folder,'smells-classes.csv')
    smells_methods = os.path.join(folder,'smells-methods.csv')

    # process csv data for class-level-smell visualizaiton
    if(os.path.exists(smells_classes)):
        folder_name = folder.split('/')[-1]
        array_classlevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        with open(smells_classes) as csv_file:
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
                            if name_list[i] in index_dict_class:
                                continue
                            array_classlevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            index_dict_class[name_list[i]]=1
                        elif i == len(name_list)-1:

                            total_smell = 0 
                            for j in range(1,12):
                                total_smell += int(row[j])

                            if name_list[i] in index_dict_class:
                                idx = array_classlevel.index([name_list[i],name_list[i-1],0,0])
                                array_classlevel[idx] = [name_list[i],name_list[i-1],total_smell,0]
                            else:
                                array_classlevel.append([name_list[i],name_list[i-1],total_smell,0])
                                index_dict_class[name_list[i]]=1
                        else:
                            if name_list[i] in index_dict_class:
                                continue
                            array_classlevel.append([name_list[i],name_list[i-1],0,0])
                            index_dict_class[name_list[i]]=1
                    line_count += 1

    # process csv data for method-level-smell visualizaiton
    if(os.path.exists(smells_methods)):
        folder_name = folder.split('/')[-1]
        array_methodlevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        with open(smells_methods) as csv_file:
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
                            if name_list[i] in index_dict_method:
                                continue
                            array_methodlevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            index_dict_method[name_list[i]]=1
                        elif i == len(name_list)-1:

                            total_smell = 0 
                            for j in range(1,5):
                                total_smell += int(row[j])
                            array_methodlevel.append([name_list[i],name_list[i-1],total_smell,0])
                            pieChartArray[3][1] += total_smell
                        else:
                            if name_list[i] in index_dict_method:
                                continue
                            array_methodlevel.append([name_list[i],name_list[i-1],0,0])
                            index_dict_method[name_list[i]]=1
                    line_count += 1



# Serializing json 
json_object_piechartArray = json.dumps(pieChartArray, indent = 2) 
json_object_class = json.dumps(array_classlevel, indent = 2) 
json_object_method = json.dumps(array_methodlevel, indent = 2) 
  
# Writing to data.json 
with open("./detailedClass/data.json", "w") as outfile: 
    outfile.write(json_object_class) 

with open("./detailedMethod/data.json", "w") as outfile: 
    outfile.write(json_object_method) 

with open("./overview/data.json", "w") as outfile: 
    outfile.write(json_object_piechartArray) 