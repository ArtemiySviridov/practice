import requests
from bs4 import BeautifulSoup
from loguru import logger


def error_processing(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.MissingSchema:
        logger.error("Incorrect URL! | Enter the URL following the example! | "
                     "Example: https://vk.com/artist/aaaaaaaaaa")
        return
    except requests.exceptions.InvalidSchema:
        logger.error("Use the correct scheme in the request URL. | "
                     "Enter the URL following the example! | "
                     "Example: https://vk.com/artist/aaaaaaaaaa")
        return
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return

    return response


def parse_top_ten_tracks(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    artist_name = soup.find('h1', class_='MusicAuthor_block__title MusicAuthor_block__title--hidden').text

    tracks = soup.find_all('a', class_='audio_row__title_inner _audio_row__title_inner')

    result = {
        'artist': artist_name,
        'tracks': []
    }

    for track in tracks:
        result['tracks'].append(track)

    return result


def print_top_ten_tracks(tracks):
    for i in range(10):
        print(f"{i + 1}. {tracks[i].text}")


def main():
    link = input('Enter link to artist on VK: ')
    errors = error_processing(link)
    if not errors:
        return
    parsed_tracks = parse_top_ten_tracks(errors)
    if not parsed_tracks:
        return
    print(f"Top 10 tracks of {parsed_tracks['artist']}:")
    print_top_ten_tracks(parsed_tracks['tracks'])


main()
