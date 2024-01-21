from colorama import init, Fore, Style

def phonedork(username):
    gg_phone_gen = {
        'General1': f"https://www.google.com/search?q=inurl:%22+{username}%22",
        'General2': f"https://www.google.com/search?q=intext:(%22+{username}%22)",
        'General3': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:txt",
        'General4': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:csv",
        'General5': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:pdf",
        'General6': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:doc",
        'General7': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:docx",
        'General8': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:log",
        'General9': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:xls",
        'General10': f"https://www.google.com/search?q=intext:(%22+{username}%22)filetype:xlsx",
    }
    gg_phone_in = {
        "Intitle1": f"https://www.google.com/search?q=intitle:(%22+{username}%22)",
        "Intitle2": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:txt",
        "Intitle3": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:csv",
        "Intitle4": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:pdf",
        "Intitle5": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:doc",
        "Intitle6": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:docx",
        "Intitle7": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:log",
        "Intitle8": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:xls",
        "Intitle9": f"https://www.google.com/search?q=intitle:(%22+{username}%22)filetype:xlsx",
    }
    gg_phone_fp = {
        'FingerPrint1': f"https://www.google.com/search?q=site:www.instagram.com+intext:%22%22+{username}%22%22",
        'FingerPrint2': f"https://www.google.com/search?q=site:www.twitter.com+intext:%22%22+{username}%22%22",
        'FingerPrint3': f"https://www.google.com/search?q=site:www.facebook.com+intext:%22%22+{username}%22%22",
        'FingerPrint4': f"https://www.google.com/search?q=site:www.vk.com+intext:%22%22+{username}%22%22",
        'FingerPrint5': f"https://www.google.com/search?q=site:www.linkedin.com+intext:%22%22+{username}%22%22",
    }
    ydx_phone_gen = {
        'General1': f"https://yandex.com/search/?text=+{username}",
        'General2': f"https://yandex.com/search/?text=(+{username})mime:txt",
        'General3': f"https://yandex.com/search/?text=(+{username})mime:pdf",
        'General4': f"https://yandex.com/search/?text=(+{username})mime:csv",
        'General5': f"https://yandex.com/search/?text=(+{username})mime:doc",
        'General6': f"https://yandex.com/search/?text=(+{username})mime:log",
        'General7': f"https://yandex.com/search/?text=(+{username})mime:docx",
        'General8': f"https://yandex.com/search/?text=(+{username})mime:xls",
        'General9': f"https://yandex.com/search/?text=(+{username})mime:xlsx",
        'General10': f"https://yandex.com/search/?text=(+{username})mime:odt",
    }
    ydx_phone_in = {
        "Intitle1": f"https://yandex.com/search/?text=title:+{username}",
        "Intitle2": f"https://yandex.com/search/?text=title:(+{username})mime:txt",
        "Intitle3": f"https://yandex.com/search/?text=title:(+{username})mime:pdf",
        "Intitle4": f"https://yandex.com/search/?text=title:(+{username})mime:csv",
        "Intitle5": f"https://yandex.com/search/?text=title:(+{username})mime:doc",
        "Intitle6": f"https://yandex.com/search/?text=title:(+{username})mime:docx",
        "Intitle7": f"https://yandex.com/search/?text=title:(+{username})mime:log",
        "Intitle8": f"https://yandex.com/search/?text=title:(+{username})mime:xls",
        "Intitle9": f"https://yandex.com/search/?text=title:(+{username})mime:xlsx",
        "Intitle10": f"https://yandex.com/search/?text=inurl:+{username}",
    }
    ydx_phone_fp = {
        'FingerPrint1': f"https://yandex.com/search/?text=site:instagram.com+'+{username}'",
        'FingerPrint2': f'https://yandex.com/search/?text=site:twitter.com+"+{username}"',
        'FingerPrint3': f'https://yandex.com/search/?text=site:facebook.com+"+{username}"',
        'FingerPrint4': f'https://yandex.com/search/?text=site:vk.com+"+{username}"',
        'FingerPrint5': f' https://yandex.com/search/?text=site:linkedin.com+"+{username}"',
    }
    ydx_phone_nf_gen = {
        'General1': f"https://yandex.com/search/?text={username}",
        'General2': f"https://yandex.com/search/?text=({username})mime:txt",
        'General3': f"https://yandex.com/search/?text=({username})mime:pdf",
        'General4': f"https://yandex.com/search/?text=({username})mime:csv",
        'General5': f"https://yandex.com/search/?text=({username})mime:doc",
        'General6': f"https://yandex.com/search/?text=({username})mime:log",
        'General7': f"https://yandex.com/search/?text=({username})mime:docx",
        'General8': f"https://yandex.com/search/?text=({username})mime:xls",
        'General9': f"https://yandex.com/search/?text=({username})mime:xlsx",
        'General10': f"https://yandex.com/search/?text=({username})mime:odt",
    }
    ydx_phone_nf_in = {
        "Intitle1": f"https://yandex.com/search/?text=title:{username}",
        "Intitle2": f"https://yandex.com/search/?text=title:({username})mime:pdf",
        "Intitle3": f"https://yandex.com/search/?text=title:({username})mime:csv",
        "Intitle4": f"https://yandex.com/search/?text=title:({username})mime:doc",
        "Intitle5": f"https://yandex.com/search/?text=title:({username})mime:docx",
        "Intitle6": f"https://yandex.com/search/?text=title:({username})mime:log",
        "Intitle7": f"https://yandex.com/search/?text=title:({username})mime:xls",
        "Intitle8": f"https://yandex.com/search/?text=title:({username})mime:xlsx",
        "Intitle9": f"https://yandex.com/search/?text=title:({username})mime:odt",
    }
    ydx_phone_nf_fp = {
        'FingerPrint1': f'https://yandex.com/search/?text=site:instagram.com+"{username}"',
        'FingerPrint2': f'https://yandex.com/search/?text=site:twitter.com+"{username}"',
        'FingerPrint3': f'https://yandex.com/search/?text=site:facebook.com+"{username}"',
        'FingerPrint4': f'https://yandex.com/search/?text=site:vk.com+"{username}"',
        'FingerPrint5': f'https://yandex.com/search/?text=site:linkedin.com+"{username}"',
    }
    return {
    '': {
        "\nGOOGLE GENERAL DORK : \n": gg_phone_gen,
        "\nGOOGLE FINGERPRINT DORK : \n": gg_phone_fp,
        "\nGOOGLE INTITLE DORK : \n": gg_phone_in,
        "\nYANDEX GENERAL DORK : \n": ydx_phone_gen,
        "\nYANDEX FINGERPRINT DORK : \n": ydx_phone_fp,
        "\nYANDEX INTITLE DORK : \n": ydx_phone_in,
        "\nYANDEX NATIONAL NUMBER GENERAL DORK: \n": ydx_phone_gen,
        "\nYANDEX NATIONAL NUMBER FINGERPRINT DORK : \n": ydx_phone_nf_fp,
        "\nYANDEX NATIONAL NUMBER INTITLE DORK : \n": ydx_phone_nf_in
        }
    } 

def display_phone_dorks(phone_dorks):
    for suite_name, suite_data in phone_dorks.items():
        print(f"{Fore.WHITE}[find]{Style.RESET_ALL}: {Fore.RED}{suite_name}{Style.RESET_ALL}")
        for dork_type, dork_dict in suite_data.items():
            print(f"{Fore.WHITE}[find]{Style.RESET_ALL}: {Fore.RED}{dork_type}{Style.RESET_ALL}")
            for key, link in dork_dict.items():
                colored_link = f"{Fore.WHITE}[find]{Style.RESET_ALL}: \033[92m{link}{Style.RESET_ALL}"
                print(colored_link)
            print()