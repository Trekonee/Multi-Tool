from colorama import init, Fore, Style

def maildork(username):
    gg_dork_gen = {
        "General1": f"https://www.google.com/search?q=inurl:%22{username}%22",
        "General2": f"https://www.google.com/search?q=intext:%22{username}%22",
        "General3": f" https://www.google.com/search?q=intext:(%22{username}%22)filetype:txt",
        "General4": f"https://www.google.com/search?q=intext:(%22{username}%22)filetype:csv",
        "General5": f" https://www.google.com/search?q=intext:(%22{username}%22)filetype:pdf",
        "General6": f"https://www.google.com/search?q=intext:(%22{username}%22)filetype:doc",
        "General7": f"https://www.google.com/search?q=intext:(%22{username}%22)filetype:docx",
        "General8": f"https://www.google.com/search?q=intext:(%22{username}%22)filetype:log",
        "General9": f"https://www.google.com/search?q=intext:(%22{username}%22)filetype:xls",
        "General10": f"https://www.google.com/search?q=intext:(%22{username}%22)filetype:xlsx",
    }
    gg_dork_pass = {
        "Password1": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)",
        "Password2": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:txt",
        "Password3": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:csv",
        "Password4": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:pdf",
        "Password5": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:doc",
        "Password6": f" https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:docx",
        "Password7": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:log",
        "Password8": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:xls",
        "Password9": f"https://www.google.com/search?q=intext:%22{username}%22(Password+OR+password+OR+PASSWORD)filetype:xlsx",
    }
    gg_dork_in = {
        "Intitle1": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:txt",
        "Intitle2": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:csv",
        "Intitle3": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:pdf",
        "Intitle4": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:doc",
        "Intitle5": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:docx",
        "Intitle6": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:log",
        "Intitle7": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:xls",
        "Intitle8": f"https://www.google.com/search?q=intitle:(%22{username}%22)filetype:xlsx",
        "Intitle9": f"https://www.google.com/search?q=inurl:%22{username}%22",
    }
    ydx_dork_gen ={
    "General1": f"https://yandex.com/search/?text={username}&mime:txt",
    "General2": f"https://yandex.com/search/?text={username}&mime:pdf",
    "General3": f"https://yandex.com/search/?text={username}&mime:csv",
    "General4": f"https://yandex.com/search/?text={username}&mime:doc",
    "General5": f"https://yandex.com/search/?text={username}&mime:docx",
    "General6": f"https://yandex.com/search/?text={username}&mime:log",
    }
    ydx_dork_pass = {
    "Password1": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:txt",      
    "Password2": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:pdf",              
    "Password3": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:csv",      
    "Password4": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:doc",      
    "Password5": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:docx",       
    "Password6": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:log",
    "Password7": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:xls",  
    "Password8": f"https://yandex.com/search/?text={username}&&(!Password|!password|!PASSWORD)&&mime:xlsx",
    }
    ydx_dork_in = {
    "Intitle1": f"https://yandex.com/search/?text=title:{username}",
    "Intitle2": f"https://yandex.com/search/?text=title:{username}&&mime:txt",
    "Intitle3": f"https://yandex.com/search/?text=title:{username}&&mime:pdf",
    "Intitle4": f"https://yandex.com/search/?text=title:{username}&&mime:csv",
    "Intitle5": f"https://yandex.com/search/?text=title:{username}&&mime:doc",
    "Intitle6": f"https://yandex.com/search/?text=title:{username}&&mime:docx",
    "Intitle7": f"https://yandex.com/search/?text=title:{username}&&mime:xls",
    "Intitle8": f"https://yandex.com/search/?text=title:{username}&&mime:xlsx",
    "Intitle9": f"https://yandex.com/search/?text=title:{username}&&mime:log",
    "Intitle10": f"https://yandex.com/search/?text=inurl:{username}",
    }


    return {'': {'\n[GENERALS DORKS] : \n': gg_dork_gen, '\n[PASSWORDS DORKS] : \n': gg_dork_pass, '\n[INTITLES DORKS] : \n': gg_dork_in, '\n[YANDEX GENERALS DORKS] : \n': ydx_dork_gen, '\n[YANDEX PASSWORDS DORKS] : \n': ydx_dork_pass, '\n[YANDEX INTITLES DORKS] : \n': ydx_dork_in}}


def display_dorks(dorks):
    for suite_name, suite_data in dorks.items():
        print(f"{Fore.RED}{suite_name}{Style.RESET_ALL}")
        for dork_type, dork_dict in suite_data.items():
            print(f"{Fore.RED}{dork_type}{Style.RESET_ALL}")
            for key, link in dork_dict.items():
                colored_link = f"{Fore.WHITE}[find]{Style.RESET_ALL}: {Fore.GREEN}{link}{Style.RESET_ALL}"
                print(colored_link)