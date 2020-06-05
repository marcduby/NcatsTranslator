# imports
import pandas as pd 
import json
import requests

def create_query_map():
    '''
    method to test library loaded correctly
    '''
    print("test map")


def query_map(source_type, source_id, target_type, relationship):
    '''
    returns a json reasoner query object
    '''

    # build the map    
    edge_map = {'id': 'e00', 'source_id': 'n00', 'target_id': 'n01', 'type': relationship}
    source_map = {'id': 'n00', 'curie': source_id, 'type': source_type}
    target_map = {'id': 'n01', 'type': target_type}
    query_map = {'edges': [edge_map], 'nodes': [source_map, target_map]}
    return_map = {'query_graph': query_map}
    return_map = {'message': return_map}
    # print("test map")

    # return
    return return_map

def query_map_df(source_type, source_id, target_type, relationship, rest_url):
    '''
    calls the url and returns a pandas dataframe
    adds extra columns to the results DF indicating source/target types
    '''

    # get the query map
    query_map_result = query_map(source_type, source_id, target_type, relationship)

    # make the REST call
    response = requests.post(rest_url, json=query_map_result).json()

    # convert to a pandas dataframe
    result_df = pd.DataFrame(response.get('knowledge_graph').get('edges'))

    # add type columns
    result_df['source_type'] = source_type
    result_df['target_type'] = target_type

    # log results count
    print("got {} row dataframe".format(result_df.shape[0]))

    # return
    return result_df

def query_map_json(source_type, source_id, target_type, relationship, rest_url):
    '''
    calls the url and returns a pandas dataframe
    adds extra columns to the results DF indicating source/target types
    '''

    # get the query map
    query_map_result = query_map(source_type, source_id, target_type, relationship)

    # make the REST call
    response = requests.post(rest_url, json=query_map_result).json()

    # return
    return response


