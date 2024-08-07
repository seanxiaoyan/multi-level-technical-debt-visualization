import csv
import sys
import os
import json


proj_name = sys.argv[1]
data_path = os.path.join(os.getcwd(),'GetSmells','getsmells-output','smells','{}'.format(proj_name))

subfolders = [ f.path for f in os.scandir(data_path) if f.is_dir() ]

array_packagelevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_unstable_dep=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_pk_cyc_dep=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]


array_classlevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_god=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_lazy=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_complex=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_large=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_refused=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_data=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_feature=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_brain=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_hub=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_cyc=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_classlevel_unhealthy=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]


array_methodlevel=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_methodlevel_lmethod=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_methodlevel_lparemeterlist=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_methodlevel_shotgun=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]
array_methodlevel_brain=[['child', 'Parent', 'size', 'color'],
[f'{proj_name}',None,0,0]]



pieChartArray = [
  ['Smell Name', 'Count'],
  ['Package Level', 0],
  ['Class Level', 0],
  ['Method Level', 0]
]

barChartArray = [
  ["Smell Name", "Count"],
  ["God Class", 0, "#D5BB9E"],
  ["Lazy Class", 0, "#D5BB9E"],
  ["Complex Class", 0, "#D5BB9E"],
  ["Large Class", 0, "#D5BB9E"],
  ["Refused Request", 0, "#D5BB9E"],
  ["Data Class", 0, "#D5BB9E"],
  ["Feature Envy", 0, "#D5BB9E"],
  ["Brain Class", 0, "#D5BB9E"],
  ["Hub Like Dependency", 0, "#D5BB9E"],
  ["Class Cyclic Dependency", 0, "#D5BB9E"],
  ["Unhealthy Inheritance", 0, "#D5BB9E"],
  ["Long Method", 0, "#178CCB"],
  ["Long Parameter List", 0, "#178CCB"],
  ["Shotgun Surgery", 0, "#178CCB"],
  ["Brain Method", 0, "#178CCB"],
  ["Unstable Dependency", 0, "#803C05"],
  ["Package Cyclic Dependency", 0, "#803C05"]
  
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
        folder_name = folder.replace('\\','/').split('/')[-1]
        

        array_packagelevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_unstable_dep.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_pk_cyc_dep.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])

        package_array_index+=1

        with open(smells_packages) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if not row:
                    continue
                if line_count == 0:
                    line_count += 1
                else:
                    name_list = row[0].split('.')

                    # process name
                    for i in range(len(name_list)):
                        if i == 0:
                            temp = name_list[i]
                            name_list[i]= os.path.join(f'{proj_name}/{folder_name}/{temp}').replace('\\','/')
                        else:
                            temp = name_list[i]
                            name_list[i] = os.path.join(name_list[i-1],temp).replace('\\','/')

                    # count 
                    total_smell = 0 
                    unstable_dep_smell = 0
                    pk_cyc_dep_smell = 0

                    j = 1
                    bar_chart_array_index = 15+j
                    barChartArray[bar_chart_array_index][1]+=int(row[j])

                    total_smell += int(row[j]) 
                    unstable_dep_smell += int(row[j]) 

                    j = 2
                    bar_chart_array_index = 15+j
                    barChartArray[bar_chart_array_index][1]+=int(row[j])
                    
                    total_smell += int(row[j]) 
                    pk_cyc_dep_smell += int(row[j]) 

                    for i in range(len(name_list)):
                        if i == len(name_list)-1:
                            if name_list[i] in nonleaf_dict_package:
                                newName = name_list[i]+'-self'       

                                array_packagelevel.append([newName,name_list[i],total_smell,0])
                                array_pk_cyc_dep.append([newName,name_list[i],pk_cyc_dep_smell,0])
                                array_unstable_dep.append([newName,name_list[i],unstable_dep_smell,0])

                                package_array_index+=1


                            else:
                                if i == 0:
                                    array_packagelevel.append([name_list[i],f'{proj_name}/{folder_name}',total_smell,0])
                                    array_pk_cyc_dep.append([name_list[i],f'{proj_name}/{folder_name}',pk_cyc_dep_smell,0])
                                    array_unstable_dep.append([name_list[i],f'{proj_name}/{folder_name}',unstable_dep_smell,0])

                                else:
                                    array_packagelevel.append([name_list[i],name_list[i-1],total_smell,0])
                                    array_pk_cyc_dep.append([name_list[i],name_list[i-1],pk_cyc_dep_smell,0])
                                    array_unstable_dep.append([name_list[i],name_list[i-1],unstable_dep_smell,0])

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
                                    count_pk_cyc_dep = array_pk_cyc_dep[idx][2]
                                    count_unstable_dep = array_unstable_dep[idx][2]

                                    array_packagelevel.append([newName,name_list[i],count,0])
                                    array_pk_cyc_dep.append([newName,name_list[i],count_pk_cyc_dep,0])
                                    array_unstable_dep.append([newName,name_list[i],count_unstable_dep,0])

                                    array_packagelevel[idx][2]=0
                                    array_pk_cyc_dep[idx][2]=0
                                    array_unstable_dep[idx][2]=0

                                    package_array_index+=1
                                    self_dict_package[name_list[i]]=1
                                continue # continue to avoid duplicate


                            if i == 0:
                                array_packagelevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                                array_pk_cyc_dep.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                                array_unstable_dep.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            else:
                                array_packagelevel.append([name_list[i],name_list[i-1],0,0])
                                array_pk_cyc_dep.append([name_list[i],name_list[i-1],0,0])
                                array_unstable_dep.append([name_list[i],name_list[i-1],0,0])
                      
                            
                            package_array_index+=1
                            nonleaf_dict_package[name_list[i]]=package_array_index

                    line_count += 1


    # process csv data for class-level-smell visualizaiton
    if(os.path.exists(smells_classes)):
        folder_name = folder.replace('\\','/').split('/')[-1]

        array_classlevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_god.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_lazy.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_complex.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_large.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_refused.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_data.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_feature.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_brain.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_hub.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_cyc.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_classlevel_unhealthy.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])

        class_array_index+=1
        with open(smells_classes) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if not row:
                    continue
                if line_count == 0:
                    line_count += 1
                else:
                    name_list = row[0].split('.')

                    for i in range(len(name_list)):
                        if i == 0:
                            temp = name_list[i]
                            name_list[i]= os.path.join(f'{proj_name}/{folder_name}/{temp}').replace('\\','/')
                        else:
                            temp = name_list[i]
                            name_list[i] = os.path.join(name_list[i-1],temp).replace('\\','/')

                    for i in range(len(name_list)):
                        if i == 0:
                            
                            if name_list[i] in nonleaf_dict_class:
                                continue # continue to avoid duplicate
                            # construct treemap data array
                            array_classlevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_god.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_lazy.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_complex.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_large.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_refused.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_data.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_feature.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_brain.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_hub.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_cyc.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_classlevel_unhealthy.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            
                            class_array_index+=1
                            nonleaf_dict_class[name_list[i]]=class_array_index

                        elif i == len(name_list)-1:
                            # count smell
                            total_smell = 0
                            smell_god = 0
                            smell_lazy = 0
                            smell_complex = 0
                            smell_large = 0
                            smell_refuesd = 0
                            smell_data = 0
                            smell_feature = 0
                            smell_brain = 0
                            smell_hub = 0
                            smell_class_cyc = 0
                            smell_unhealthy = 0 

                            j = 1
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_god += int(row[j])


                            j = 2
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_lazy += int(row[j])

                            j = 3
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_complex += int(row[j])

                            j = 4
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_large += int(row[j])

                            j = 5
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_refuesd += int(row[j])

                            j = 6
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_data += int(row[j])

                            j = 7
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_feature += int(row[j])

                            j = 8
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_brain += int(row[j])

                            j = 9
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_hub += int(row[j])

                            j = 10
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_class_cyc += int(row[j])

                            j = 11
                            barChartArray[j][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_unhealthy += int(row[j])

                            
                            if name_list[i] in nonleaf_dict_class:
                                newName = name_list[i]+'-self'  
                                # construct treemap data array
                                array_classlevel.append([newName,name_list[i],total_smell,0])
                                array_classlevel_god.append([newName,name_list[i],smell_god,0])
                                array_classlevel_lazy.append([newName,name_list[i],smell_lazy,0])
                                array_classlevel_complex.append([newName,name_list[i],smell_complex,0])
                                array_classlevel_large.append([newName,name_list[i],smell_large,0])
                                array_classlevel_refused.append([newName,name_list[i],smell_refuesd,0])
                                array_classlevel_data.append([newName,name_list[i],smell_data,0])
                                array_classlevel_feature.append([newName,name_list[i],smell_feature,0])
                                array_classlevel_brain.append([newName,name_list[i],smell_brain,0])
                                array_classlevel_hub.append([newName,name_list[i],smell_hub,0])
                                array_classlevel_cyc.append([newName,name_list[i],smell_class_cyc,0])
                                array_classlevel_unhealthy.append([newName,name_list[i],smell_unhealthy,0])

                                class_array_index+=1
                                pieChartArray[2][1] += total_smell
                                self_dict_class[name_list[i]]=1

                            else:
                                array_classlevel.append([name_list[i],name_list[i-1],total_smell,0])
                                array_classlevel_god.append([name_list[i],name_list[i-1],smell_god,0])
                                array_classlevel_lazy.append([name_list[i],name_list[i-1],smell_lazy,0])
                                array_classlevel_complex.append([name_list[i],name_list[i-1],smell_complex,0])
                                array_classlevel_large.append([name_list[i],name_list[i-1],smell_large,0])
                                array_classlevel_refused.append([name_list[i],name_list[i-1],smell_refuesd,0])
                                array_classlevel_data.append([name_list[i],name_list[i-1],smell_data,0])
                                array_classlevel_feature.append([name_list[i],name_list[i-1],smell_feature,0])
                                array_classlevel_brain.append([name_list[i],name_list[i-1],smell_brain,0])
                                array_classlevel_hub.append([name_list[i],name_list[i-1],smell_hub,0])
                                array_classlevel_cyc.append([name_list[i],name_list[i-1],smell_class_cyc,0])
                                array_classlevel_unhealthy.append([name_list[i],name_list[i-1],smell_unhealthy,0])

                                class_array_index+=1
                                pieChartArray[2][1] += total_smell
                                leaf_dict_class[name_list[i]]=class_array_index

                        else:
                            # construct treemap data array
                            if name_list[i] in nonleaf_dict_class:
                                continue # continue to avoid duplicate

                            if name_list[i] in leaf_dict_class:
                                #check if self has alrady created
                                if name_list[i] not in self_dict_class:
                                    idx = leaf_dict_class[name_list[i]]
                                    newName = array_classlevel[idx][0]+'-self'
                                    count = array_classlevel[idx][2]
                                    count_god = array_classlevel_god[idx][2]
                                    count_lazy = array_classlevel_lazy[idx][2]
                                    count_complex = array_classlevel_complex[idx][2]
                                    count_large = array_classlevel_large[idx][2]
                                    count_refused = array_classlevel_refused[idx][2]
                                    count_data = array_classlevel_data[idx][2]
                                    count_feature = array_classlevel_feature[idx][2]
                                    count_brain = array_classlevel_brain[idx][2]
                                    count_hub = array_classlevel_hub[idx][2]
                                    count_cyc = array_classlevel_cyc[idx][2]
                                    count_unhealthy = array_classlevel_unhealthy[idx][2]
                                    
                                    array_classlevel.append([newName,name_list[i],count,0])
                                    array_classlevel_god.append([newName,name_list[i],count_god,0])
                                    array_classlevel_lazy.append([newName,name_list[i],count_lazy,0])
                                    array_classlevel_complex.append([newName,name_list[i],count_complex,0])
                                    array_classlevel_large.append([newName,name_list[i],count_large,0])
                                    array_classlevel_refused.append([newName,name_list[i],count_refused,0])
                                    array_classlevel_data.append([newName,name_list[i],count_data,0])
                                    array_classlevel_feature.append([newName,name_list[i],count_feature,0])
                                    array_classlevel_brain.append([newName,name_list[i],count_brain,0])
                                    array_classlevel_hub.append([newName,name_list[i],count_hub,0])
                                    array_classlevel_cyc.append([newName,name_list[i],count_cyc,0])
                                    array_classlevel_unhealthy.append([newName,name_list[i],count_unhealthy,0])
                                    

                                    class_array_index+=1
                                    self_dict_class[name_list[i]]=1
                                continue # continue to avoid duplicate

                            array_classlevel.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_god.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_lazy.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_complex.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_large.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_refused.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_data.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_feature.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_brain.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_hub.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_cyc.append([name_list[i],name_list[i-1],0,0])
                            array_classlevel_unhealthy.append([name_list[i],name_list[i-1],0,0])
                            class_array_index+=1
                            nonleaf_dict_class[name_list[i]]=class_array_index

                    line_count += 1

    # process csv data for method-level-smell visualizaiton
    if(os.path.exists(smells_methods)):
        folder_name = folder.replace('\\','/').split('/')[-1]
        array_methodlevel.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_methodlevel_lmethod.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_methodlevel_lparemeterlist.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_methodlevel_brain.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])
        array_methodlevel_shotgun.append([f'{proj_name}/{folder_name}',f'{proj_name}',0,0])

        with open(smells_methods) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if not row:
                    continue
                if line_count == 0:
                    line_count += 1

                else:
                    name_list = row[0].split('.')
                    for i in range(len(name_list)):
                        if i == 0:
                            temp = name_list[i]
                            name_list[i]= os.path.join(f'{proj_name}/{folder_name}/{temp}').replace('\\','/')

                        else:
                            temp = name_list[i]
                            name_list[i] = os.path.join(name_list[i-1],temp).replace('\\','/')
                    for i in range(len(name_list)):
                        if i == 0:
                            if name_list[i] in nonleaf_dict_method:
                                continue
                            array_methodlevel.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_methodlevel_lmethod.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_methodlevel_lparemeterlist.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_methodlevel_shotgun.append([name_list[i],f'{proj_name}/{folder_name}',0,0])
                            array_methodlevel_brain.append([name_list[i],f'{proj_name}/{folder_name}',0,0])

                            nonleaf_dict_method[name_list[i]]=1

                        elif i == len(name_list)-1:
                            #count smell
                            total_smell = 0 
                            smell_lmethod = 0
                            smell_lparameter = 0
                            smell_shotgun = 0
                            smell_brain = 0

                            j=1
                            bar_chart_array_index = 11+j
                            barChartArray[bar_chart_array_index][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_lmethod += int(row[j])

                            j=2
                            bar_chart_array_index = 11+j
                            barChartArray[bar_chart_array_index][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_lparameter += int(row[j])

                            j=3
                            bar_chart_array_index = 11+j
                            barChartArray[bar_chart_array_index][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_shotgun += int(row[j])

                            j=4
                            bar_chart_array_index = 11+j
                            barChartArray[bar_chart_array_index][1]+=int(row[j])
                            total_smell += int(row[j])
                            smell_brain += int(row[j])
    
                            array_methodlevel.append([name_list[i],name_list[i-1],total_smell,0])
                            array_methodlevel_lmethod.append([name_list[i],name_list[i-1],smell_lmethod,0])
                            array_methodlevel_lparemeterlist.append([name_list[i],name_list[i-1],smell_lparameter,0])
                            array_methodlevel_shotgun.append([name_list[i],name_list[i-1],smell_shotgun,0])
                            array_methodlevel_brain.append([name_list[i],name_list[i-1],smell_brain,0])

                            pieChartArray[3][1] += total_smell

                        else:
                            if name_list[i] in nonleaf_dict_method:
                                continue
                            array_methodlevel.append([name_list[i],name_list[i-1],0,0])
                            array_methodlevel_lmethod.append([name_list[i],name_list[i-1],0,0])
                            array_methodlevel_lparemeterlist.append([name_list[i],name_list[i-1],0,0])
                            array_methodlevel_shotgun.append([name_list[i],name_list[i-1],0,0])
                            array_methodlevel_brain.append([name_list[i],name_list[i-1],0,0])

                            nonleaf_dict_method[name_list[i]]=1

                    line_count += 1



# Serializing json 
json_object_piechartArray = json.dumps(pieChartArray, indent = 2) 
json_object_barchartArray = json.dumps(barChartArray, indent = 2) 

json_object_package = json.dumps(array_packagelevel, indent = 2) 
json_object_package_unstable = json.dumps(array_unstable_dep, indent = 2) 
json_object_package_cyc = json.dumps(array_pk_cyc_dep, indent = 2) 

json_object_class = json.dumps(array_classlevel, indent = 2) 
json_object_god = json.dumps(array_classlevel_god, indent = 2) 
json_object_lazy = json.dumps(array_classlevel_lazy, indent = 2) 
json_object_complex = json.dumps(array_classlevel_complex, indent = 2) 
json_object_large = json.dumps(array_classlevel_large, indent = 2) 
json_object_refused = json.dumps(array_classlevel_refused, indent = 2) 
json_object_data = json.dumps(array_classlevel_data, indent = 2) 
json_object_feature = json.dumps(array_classlevel_feature, indent = 2) 
json_object_brain = json.dumps(array_classlevel_brain, indent = 2) 
json_object_hub = json.dumps(array_classlevel_hub, indent = 2) 
json_object_class_cyc = json.dumps(array_classlevel_cyc, indent = 2) 
json_object_unhealthy = json.dumps(array_classlevel_unhealthy, indent = 2) 

json_object_method = json.dumps(array_methodlevel, indent = 2) 
json_object_lmethod = json.dumps(array_methodlevel_lmethod, indent = 2) 
json_object_lparameter = json.dumps(array_methodlevel_lparemeterlist, indent = 2) 
json_object_shotgun = json.dumps(array_methodlevel_shotgun, indent = 2) 
json_object_brain_method = json.dumps(array_methodlevel_brain, indent = 2) 
  
# Writing to data.json 
# package level
pathPAll = os.path.join(os.getcwd(),'detailedPackage','data-all.json')
with open(pathPAll, "w") as outfile: 
    outfile.write(json_object_package) 

pathPUD = os.path.join(os.getcwd(),'detailedPackage','data-unstable-dependency.json')
with open(pathPUD, "w") as outfile: 
    outfile.write(json_object_package_unstable) 

pathPCD = os.path.join(os.getcwd(),'detailedPackage','data-cyclic-dependency.json')
with open(pathPCD, "w") as outfile: 
    outfile.write(json_object_package_cyc) 

# class level
pathCAll = os.path.join(os.getcwd(),'detailedClass','data-all.json')
with open(pathCAll, "w") as outfile: 
    outfile.write(json_object_class) 

pathCGC = os.path.join(os.getcwd(),'detailedClass','data-god-class.json')
with open(pathCGC, "w") as outfile: 
    outfile.write(json_object_god) 

pathCLC = os.path.join(os.getcwd(),'detailedClass','data-lazy-class.json')
with open(pathCLC, "w") as outfile: 
    outfile.write(json_object_lazy) 

pathCCC = os.path.join(os.getcwd(),'detailedClass','data-complex-class.json')
with open(pathCCC, "w") as outfile: 
    outfile.write(json_object_complex) 

pathClargeC = os.path.join(os.getcwd(),'detailedClass','data-large-class.json')
with open(pathClargeC, "w") as outfile: 
    outfile.write(json_object_large) 

pathCRR = os.path.join(os.getcwd(),'detailedClass','data-refused-request.json')
with open(pathCRR, "w") as outfile: 
    outfile.write(json_object_refused) 

pathCDC = os.path.join(os.getcwd(),'detailedClass','data-data-class.json')
with open(pathCDC, "w") as outfile: 
    outfile.write(json_object_data) 

pathCFE = os.path.join(os.getcwd(),'detailedClass','data-feature-envy.json')
with open(pathCFE, "w") as outfile: 
    outfile.write(json_object_feature) 

pathCBC = os.path.join(os.getcwd(),'detailedClass','data-brain-class.json')
with open(pathCBC, "w") as outfile: 
    outfile.write(json_object_brain) 

pathCHD = os.path.join(os.getcwd(),'detailedClass','data-hub-like-dependency.json')
with open(pathCHD, "w") as outfile: 
    outfile.write(json_object_hub) 

pathCCCC = os.path.join(os.getcwd(),'detailedClass','data-class-cyclic-dependency.json')
with open(pathCCCC, "w") as outfile: 
    outfile.write(json_object_class_cyc) 

pathCUD = os.path.join(os.getcwd(),'detailedClass','data-unhealthy-inheritance-dependency.json')
with open(pathCUD, "w") as outfile: 
    outfile.write(json_object_unhealthy) 

# method level
pathMAll = os.path.join(os.getcwd(),'detailedMethod','data-all.json')
with open(pathMAll, "w") as outfile: 
    outfile.write(json_object_method) 

pathMLM = os.path.join(os.getcwd(),'detailedMethod','data-long-method.json')
with open(pathMLM, "w") as outfile: 
    outfile.write(json_object_lmethod) 

pathMLPL = os.path.join(os.getcwd(),'detailedMethod','data-long-parameter-list.json')
with open(pathMLPL, "w") as outfile: 
    outfile.write(json_object_lparameter) 

pathMSS = os.path.join(os.getcwd(),'detailedMethod','data-shotgun-surgery.json')
with open(pathMSS, "w") as outfile: 
    outfile.write(json_object_shotgun) 

pathMBM = os.path.join(os.getcwd(),'detailedMethod','data-brain-method.json')
with open(pathMBM, "w") as outfile: 
    outfile.write(json_object_brain_method) 

# overview
pathPiechart = os.path.join(os.getcwd(),'overview','pieChartData.json')
with open(pathPiechart, "w") as outfile: 
    outfile.write(json_object_piechartArray) 

pathBarchart = os.path.join(os.getcwd(),'overview','barChartData.json')
with open(pathBarchart, "w") as outfile: 
    outfile.write(json_object_barchartArray) 
