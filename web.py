from selenium import webdriver
import selenium
from selenium.webdriver.common import by
from time import sleep
import pandas as pd
from create import inserir_numeros


class Web:
    def __init__(self):
        self.link = 'https://asloterias.com.br/resultados-da-mega-sena-2023'
        self.map = {
            'numeros': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[$NUM$]'
            },
            'concurso': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[$NUM$]'
            }
        }
        self.driver = webdriver.Edge()

    def abrir_site(self):
        self.driver.get(self.link)
        sleep(2)

        jogo = []
        matriz = []
        k = 0
        for i in range(1, 120):
            # print(self.driver.find_element(by.By.XPATH, self.map['concurso']['xpath'].replace('$NUM$', f'{i+3}')).text, end=' | ')
            jogo.append(int(self.driver.find_element(by.By.XPATH, self.map['concurso']['xpath'].replace('$NUM$', f'{i+3}')).text))
            for j in range(1, 7):
                k += 1
                # print(self.driver.find_element(by.By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text, end=' ')
                numero = int(self.driver.find_element(by.By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{k}')).text)
                jogo.append(numero)
            inserir_numeros(jogo[0], jogo[1], jogo[2], jogo[3], jogo[4], jogo[5], jogo[6])
            matriz.append(jogo)
            jogo = []
            print('')
        for linha in range(len(matriz)):
            for coluna in range(6):
                print(matriz[linha][coluna], end='\t')
            print('')

        planilia = pd.DataFrame(matriz)
        planilia.to_excel('C:\\Users\\51399667866\\Documents\\SO\\Python\\aula_01\\mega.xlsx', index=False)











        # print('\033[1;3;32m!MEGA DA VIRADA!\033[m')
        # print(self.driver.find_element(by.By.XPATH, self.map['concurso']['xpath'].replace('$NUM$', f'{123}')).text,end=' | ')
        # for o in range(715, 721):
        #     o += 1
        #     print(self.driver.find_element(by.By.XPATH, self.map['numeros']['xpath'].replace('$NUM$', f'{o}')).text,end=' ')
        # print('')

