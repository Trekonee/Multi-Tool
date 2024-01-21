import webbrowser

def google_dorks(username):
    # Utilisation de Google Dorks pour rechercher le nom d'utilisateur
    search_query = f'{username} site:linkedin.com OR site:facebook.com OR site:twitter.com OR site:snapchat.com/add OR site:telegram.me'
    search_url = f'https://www.google.com/search?q={search_query}'
    webbrowser.open(search_url)
    
    input("[#TREKONEE#] Press Enter to return to the menu...")