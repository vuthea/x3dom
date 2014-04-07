
def prefix_path(lst, path):
    return [path + '/' + entry for entry in lst]


def getPathTuples(data):
    """
    Loop over all elements of a given json object and generate a list of name-path-tuples
    
    @param data: Array of Objects containing the paths
    @type data: JSON Array
    
    @return: List of tuples (name, paths)
    @rtype: List<(String, List<String>)>
    """
    ENTRIES = []
    for entry in data:
        #For components consisting of a single file...
        if entry['type'] == "file":
            #...tuple consists of the file name and a list containing only this file
            ENTRIES.append((entry['path'], [entry['path']]))
        #For components split up in multiple files...
        else:
            #...tuple consists of the common file name for the component and a list
            #of the files building this component
            ENTRIES.append((entry['path'], [f['path'] for f in entry['files']]))
    return ENTRIES



#Load json file

f = open('tools/packages.json', 'r')
import json
json_object = json.load(f)


#Generate path lists for all categories

BASICS = getPathTuples(json_object['grouplist'][0]['data'])

SHADER = getPathTuples(json_object['grouplist'][1]['data'])

GFX = getPathTuples(json_object['grouplist'][2]['data'])

NODES = getPathTuples(json_object['grouplist'][3]['data'])

COMPONENTS =  getPathTuples(json_object['grouplist'][4]['data'])


#Combine categories to create profiles

CORE_PROFILE = BASICS + SHADER + GFX + NODES
MORE_PROFILE = COMPONENTS

FULL_PROFILE = CORE_PROFILE + MORE_PROFILE
