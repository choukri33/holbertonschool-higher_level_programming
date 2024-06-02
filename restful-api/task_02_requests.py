import requests
import csv

def fetch_and_print_posts():
    # Fetch response
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Print response status
    print(f"Status Code: {response.status_code}")

    # Print page title if response is OK
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Fetch response
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # If response is OK, save data to csv
    if response.status_code == 200:
        posts = response.json()
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Save to CSV
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_save)