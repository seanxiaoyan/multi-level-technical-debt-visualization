import csv
import sys
import os
import json


proj_name = sys.argv[1]
data_path='./GetSmells/getsmells-output/smells/{}/'.format(proj_name)
subfolders = [ f.path for f in os.scandir(data_path) if f.is_dir() ]

array_packagelevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]

array_classlevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]

array_methodlevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]

pieChartArray = [
  ['Smell Name', 'Count'],
  ['Package Level', 0],
  ['Class Level', 0],
  ['Method Level', 0]
]

barChartArray = [
  ["Smell Name", "Count"],
  ["God Class", 0, "#dc3912"],
  ["Lazy Class", 0, "#dc3912"],
  ["Complex Class", 0, "#dc3912"],
  ["Large Class", 0, "#dc3912"],
  ["Refused Request", 0, "#dc3912"],
  ["Data Class", 0, "#dc3912"],
  ["Feature Envy", 0, "#dc3912"],
  ["Brain Class", 0, "#dc3912"],
  ["Hub Like Dependency", 0, "#dc3912"],
  ["Class Cyclic Dependency", 0, "#dc3912"],
  ["Unhealthy Inheritance", 0, "#dc3912"],
  ["Long Method", 0, "#ff9900"],
  ["Long Parameter List", 0, "#ff9900"],
  ["Shotgun Surgery", 0, "#ff9900"],
  ["Brain Method", 0, "#ff9900"],
  ["Unstable Dependency", 0, "#3366cc"],
  ["Package Cyclic Dependency", 0, "#3366cc"]
  
]

# package
nonleaf_dict_package = {}
leaf_dict_package = {}
self_dict_package = {}
package_array_index = 1

# class
nonleaf_dict_class = {}
leaf_dict_class = {}
self_dict_class = {}
class_array_index = 1

# method
nonleaf_dict_method = {}


for folder in subfolders:
    smells_packages = os.path.join(folder,'smells-packages.csv')
    smells_classes = os.path.join(folder,'smells-classes.csv')
    smells_methods = os.path.join(folder,'smells-methods.csv')

    # process csv data for package-level-smell visualization
    if(os.path.exists(smells_packages)):
        folder_name = folder.split('/')[-1]
        array_packagelevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        package_array_index+=1
        with open(smells_packages) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    name_list = row[0].split('.')

                    # process name
                    for i in range(len(name_list)):
                        if i == 0:
                            temp = name_list[i]
                            name_list[i]= os.path.join(f'{proj_name}/{folder_name}/{temp}')
                        else:
                            temp = name_list[i]
                            name_list[i] = os.path.join(name_list[i-1],temp)

                    # count 
                    total_smell = 0 
                    for j in range(1,3):
                        bar_chart_array_index = 15+j
                        barChartArray[bar_chart_array_index][1]+=int(row[j])
                        total_smell += int(row[j])
                    for i in range(len(name_list)):
                        if i == len(name_list)-1:
                            if name_list[i] in nonleaf_dict_package:
                                newName = name_list[i]+'-self'             
                                array_packagelevel.append([newName,name_list[i],total_smell,0])
                                package_array_index+=1
                            else:
                                if i == 0:
                                    array_packagelevel.append([name_list[i],f'{proj_name}/{folder_name}',total_smell,0])
                                else:
                                    array_packagelevel.append([name_list[i],name_list[i-1],total_smell,0])
                                package_array_index+=1                      
                                leaf_dict_package[name_list[i]]=package_array_index
                            pieChartArray[1][1] += total_smell
                       

                        else:
                            if name_list[i] in nonleaf_dict_package:
                                continue # to avoid duplicate

                            if name_list[i] in leaf_dict_package:
                                # check if -self has alrady created
                                if name_list[i] not in self_dict_package:
                                    idx = leaf_dict_package[name_list[i]]
                                    newName = array_packagelevel[idx][0]+'-self'
                                    count = array_packagelevel[idx][2]
                                    array_packagelevel.append([newName,name_list[i],count,0])
                                    array_packagelevel[idx][2]=0
                                    package_array_index+=1
                                    self_dict_package[name_list[i]]=1
                                continue # continue to avoid duplicate


                            if i == 0:
                                array_packagelevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            else:
                                array_packagelevel.append([name_list[i],name_list[i-1],0,0])
                      
                            
                            package_array_index+=1
                            nonleaf_dict_package[name_list[i]]=package_array_index

                    line_count += 1


    # process csv data for class-level-smell visualizaiton
    if(os.path.exists(smells_classes)):
        folder_name = folder.split('/')[-1]
        array_classlevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        class_array_index+=1
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
                            if name_list[i] in nonleaf_dict_class:
                                continue # continue to avoid duplicate
                            array_classlevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            class_array_index+=1
                            nonleaf_dict_class[name_list[i]]=class_array_index

                        elif i == len(name_list)-1:
                            total_smell = 0 

                            for j in range(1,12):
                                barChartArray[j][1]+=int(row[j])
                                total_smell += int(row[j])
                            if name_list[i] in nonleaf_dict_class:
                                newName = name_list[i]+'-self'             
                                array_classlevel.append([newName,name_list[i],total_smell,0])
                                class_array_index+=1
                                pieChartArray[2][1] += total_smell
                                self_dict_class[name_list[i]]=1

                            else:
                                array_classlevel.append([name_list[i],name_list[i-1],total_smell,0])
                                class_array_index+=1
                                pieChartArray[2][1] += total_smell
                                leaf_dict_class[name_list[i]]=class_array_index

                        else:
                            if name_list[i] in nonleaf_dict_class:
                                continue # continue to avoid duplicate

                            if name_list[i] in leaf_dict_class:
                                #check if self has alrady created
                                if name_list[i] not in self_dict_class:
                                    idx = leaf_dict_class[name_list[i]]
                                    newName = array_classlevel[idx][0]+'-self'
                                    count = array_classlevel[idx][2]
                                    array_classlevel.append([newName,name_list[i],count,0])
                                    class_array_index+=1
                                    self_dict_class[name_list[i]]=1
                                continue # continue to avoid duplicate

                            array_classlevel.append([name_list[i],name_list[i-1],0,0])
                            class_array_index+=1
                            nonleaf_dict_class[name_list[i]]=class_array_index

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
                            if name_list[i] in nonleaf_dict_method:
                                continue
                            array_methodlevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            nonleaf_dict_method[name_list[i]]=1

                        elif i == len(name_list)-1:
                            total_smell = 0 
                            for j in range(1,5):
                                bar_chart_array_index = 11+j
                                barChartArray[bar_chart_array_index][1]+=int(row[j])
                                total_smell += int(row[j])
                            array_methodlevel.append([name_list[i],name_list[i-1],total_smell,0])
                            pieChartArray[3][1] += total_smell

                        else:
                            if name_list[i] in nonleaf_dict_method:
                                continue
                            array_methodlevel.append([name_list[i],name_list[i-1],0,0])
                            nonleaf_dict_method[name_list[i]]=1

                    line_count += 1



# Serializing json 
json_object_piechartArray = json.dumps(pieChartArray, indent = 2) 
json_object_barchartArray = json.dumps(barChartArray, indent = 2) 
json_object_package = json.dumps(array_packagelevel, indent = 2) 
json_object_class = json.dumps(array_classlevel, indent = 2) 
json_object_method = json.dumps(array_methodlevel, indent = 2) 
  
# Writing to data.json 
with open("./detailedPackage/data.json", "w") as outfile: 
    outfile.write(json_object_package) 

with open("./detailedClass/data.json", "w") as outfile: 
    outfile.write(json_object_class) 

with open("./detailedMethod/data.json", "w") as outfile: 
    outfile.write(json_object_method) 

with open("./overview/pieChartData.json", "w") as outfile: 
    outfile.write(json_object_piechartArray) 

with open("./overview/barChartData.json", "w") as outfile: 
    outfile.write(json_object_barchartArray) 