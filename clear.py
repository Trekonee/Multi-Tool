import os

def clear_screen():
    # Vérifiez le système d'exploitation
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
        
        print("""
    ████████╗   ██████╗    ███████╗   ██╗  ██╗    ██████╗    ███╗   ██╗   ███████╗   ███████╗
    ╚══██╔══╝   ██╔══██╗   ██╔════╝   ██║ ██╔╝    ██╔═████╗  ████╗  ██║   ██╔════╝   ██╔════╝
       ██║      ██████╔╝   █████╗     █████╔╝     ██║██╔██║  ██╔██╗ ██║   █████╗     █████╗
       ██║      ██╔══██╗   ██╔══╝     ██╔═██╗     ████╔╝██║  ██║╚██╗██║   ██╔══╝     ██╔══╝  
       ██║      ██║  ██║   ███████╗   ██║  ██╗    ╚██████╔╝  ██║ ╚████║   ███████╗   ███████╗
       ╚═╝      ╚═╝  ╚═╝   ╚══════╝   ╚═╝  ╚═╝     ╚═════╝   ╚═╝  ╚═══╝   ╚══════╝   ╚══════╝
                                 Made By @TrekOnee
      """)