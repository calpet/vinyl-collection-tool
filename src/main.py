from discogs_client import Client

DISCOGS_TOKEN = 'JeWKUafDsePRffhtyLIQNbvHVbISRglQSXPebBUz'
DISCOGS_APPLICATION = 'LPShuffler/0.1'


class Album:
    def __init__(self, title: str, artist: str) -> None:
        self.title = title
        self.artist = artist


if __name__ == "__main__":
    client = Client(DISCOGS_APPLICATION, user_token=DISCOGS_TOKEN)
    user = client.identity()
    collection = user.collection_folders[0].releases
    page_cap = collection.pages
    for i in range(1, page_cap + 1):
        page = collection.page(i)
        albums = []
        for item in page:
            data = item.release.data
            print(data)
            title = item.release.title
            artist = item.release.artists[0].name
            albums.append(Album(title, artist))
        for album in albums:
            print(f"{album.artist} - {album.title}\n")
