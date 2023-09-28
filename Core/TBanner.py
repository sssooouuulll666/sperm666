from colorama import Fore



_banner = '''
 ######  ### ######  ####### ######    #   
 #     #  #  #     # #     # #     #  ##   
 #     #  #  #     # #     # #     # # #   
 ######   #  #     # #     # ######    #   
 #        #  #     # #     # #   #     #   
 #        #  #     # #     # #    #    #   
 #       ### ######  ####### #     # ##### 
'''



def banner(host, port):
    '''Вывод баннера с ссылкой'''

    print(Fore.GREEN + _banner)
    print(f'сюда метнулся http://{host}:{port}')