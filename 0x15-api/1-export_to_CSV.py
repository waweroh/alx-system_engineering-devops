#!/usr/bin/python3
"""Request user todos from API"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    def m_request(resource, argss=None):
        """Retrieve user information from API"""
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if argss:
            url += ('?' + argss[0] + '=' + argss[1])

        result = requests.get(url)
        result = result.json()
        return result

    user = m_request('users', ('id', argv[1]))[0]
    tasks = m_request('todos', ('userId', argv[1]))

    csv_filename = argv[1] + '.csv'
    with open(csv_filename, mode='w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'],
                            user['username'],
                            task['completed'],
                            task['title']])
