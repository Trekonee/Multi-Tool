from colorama import init, Fore, Style
import requests

def generate_links(username):
    links = {
        'Facebook': f'https://www.facebook.com/{username}',
        'Twitter': f'https://www.twitter.com/{username}',
        'Instagram': f'https://www.instagram.com/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}',
        'TikTok': f'https://www.tiktok.com/@{username}',
        'Telegram': f'https://t.me/{username}',
        'Snapchat': f'https://www.snapchat.com/add/{username}',
        'GitHub' : f'https://github.com/{username}',
        'Tinder': f'https://www.tinder.com/@{username}',
        'Amazon': f'https://www.amazon.com/s?field-keywords={username}',
        'Hinge': f'https://hinge.co/u/{username}',
        'Bumble': f'https://bumble.com/@{username}',
        'Badoo': f'https://badoo.com/profile/{username}',
        'Kick': f'https://www.kick.com/user/{username}',
        'Twitch': f'https://www.twitch.tv/{username}',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'Myspace': f'https://myspace.com/{username}',
        'Bereal': f'https://bereal.com/{username}',
        'Crunchyroll': f'https://www.crunchyroll.com/user/{username}',
        'Discord': f'https://discord.com/users/{username}',
        'Pinterest': f'https://www.pinterest.com/{username}',
        'Quora': f'https://www.quora.com/profile/{username}',
        'Steam': f'https://steamcommunity.com/id/{username}',
        'Threads': f'https://threads.com/user/{username}',
        'Deezer': f'https://www.deezer.com/profile/{username}',
        'Spotify': f'https://open.spotify.com/user/{username}',
        'Apple Music': f'https://music.apple.com/profile/{username}'
    }

    return links

def display_links(links):
    print("\nLinks to profiles:")
    for site, link in links.items():
        response = requests.get(link)
        status_code = response.status_code
        
        if status_code == 200:
            print(f"{site}:{Style.RESET_ALL} {Fore.GREEN}{link}{Style.RESET_ALL}")
        else:
            print(f"{site}:{Style.RESET_ALL} {Fore.RED}(nothing){Style.RESET_ALL}")