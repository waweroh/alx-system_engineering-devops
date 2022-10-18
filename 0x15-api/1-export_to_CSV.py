#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    task = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    for work in task.json():
        f = open(str(user.json().get("id")) + ".csv", "a")
        f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                user.json().get("id"), user.json().get("username"),
                work.get("completed"), work.get("title")))
        f.close()
