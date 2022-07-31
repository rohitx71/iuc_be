import requests
import vimeo

client = vimeo.VimeoClient(
  token='837db7a9ea35f5177ad611af6c8e67f7',
  key='49e586b2d358b366ed70c9ef74d019393428470f',
  secret='dpCt69aykdjQBIs9DVJofd4b5AhDnp8QiQu25Uglgn9irzrEwrhpZiPyvGYb4vhN/fUZR9QvtDqPaCiCrKLMP0l0JseXtWPjJB+Y+zBcJEqdWqsrKJ1PRZFJr9DBkepd'
)

# uri = "https://api.vimeo.com/tutorial"
#
# response = client.get(uri)
# print(response.json())


def upload_video():
    file_name = '{path_to_a_video_on_the_file_system}'
    uri = client.upload(file_name, data={
      'name': 'Untitled',
      'description': 'The description goes here.'
    })
    print('Your video URI is: ' +str(uri))
    response = client.get(uri + '?fields=link').json()
    print("Your video link is: "+response['link'])
    return response['link']


def create_video():
    import requests
    url = "https://api.vimeo.com/me/videos"
    requests.post(url, headers={
        "Authorization"
    })

