

def create_query_map():
    print("test map")


def query_map(source_type, source_id, target_type, relationship):
    edge_map = {'id': 'e00', 'source_id': 'n00', 'target_id': 'n01', 'type': relationship}
    source_map = {'id': 'n00', 'curie': source_id, 'type': source_type}
    target_map = {'id': 'n01', 'type': target_type}
    query_map = {'edges': [edge_map], 'nodes': [source_map, target_map]}
    return_map = {'query_graph': query_map}
    return_map = {'message': return_map}
    print("test map")

    # return
    return return_map


