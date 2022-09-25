# %%
import numpy as np
import pandas as pd
import requests

# %% Set Access Token and Instance URL
access_token = "<enter_here>"
instance_url = "<enter_here>"

# %%
def sf_api_call(action, parameters = {}, method = 'get', data = {}):
    """
    Helper function to make calls to Salesforce REST API.
    Parameters: action (the URL), URL params, method (get, post or patch), data for POST/PATCH.
    """
    headers = {
        'Content-type': 'application/json',
        'Accept-Encoding': 'gzip',
        'Authorization': 'Bearer %s' % access_token
    }
    if method == 'get':
        r = requests.request(method, instance_url+action, headers=headers, params=parameters, timeout=120)
    elif method in ['post', 'patch']:
        r = requests.request(method, instance_url+action, headers=headers, json=data, params=parameters, timeout=120)
    else:
        # other methods not implemented in this example
        raise ValueError('Method should be get or post or patch.')
    # print('Debug: API %s call: %s' % (method, r.url) )
    if r.status_code < 300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))
    
def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }
    
def query_sf(query):
    call = sf_api_call('/services/data/v53.0/queryAll/',parameters={
            'q': query
        })

    rows = call.get('records', [])
    next = call.get('nextRecordsUrl', None)
    while next:
        call = sf_api_call(next)
        rows.extend(call.get('records', []))
        next = call.get('nextRecordsUrl', None)
    rows_flatten = [flatten_dict(r) for r in rows]
    # return rows_flatten
    rows_df = pd.DataFrame.from_dict(rows_flatten)
    rows_columns = [x.lower() for x in list(filter(lambda x: not(x.endswith(("attributes_url","attributes_type"))), rows_df.columns))]
    rows_df.columns = [x.lower() for x in rows_df.columns]
    return rows_df[rows_columns]
 
# %%
query = '''
SELECT Id, Name, BillingCity FROM Account LIMIT 10
'''
query_sf(query)
# %%
