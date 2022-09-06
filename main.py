import time
import pandas as pd
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from datetime import date

proverka_dlj_sochanenia_5 = [0]
proverka_dlj_sochanenia = [0]
count_spisoc_dji_prodoljenia_zikla_prodolzenie = [0]
spisok_dat_dlj_ostanovki_zikla = []
count_spisoc_dji_prodoljenia_zikla_dat = [0]
count_spisoc_dji_prodoljenia_zikla = [0]
vse_ostanovka = [0]

s = Service('C:\\Users\\Berserk\\Desktop\\vneberjivie\\firefoxdriver\\geckodriver.exe')
driver = webdriver.Firefox(service=s)


def start_prog():
    driver.get('https://www.qr.com/ru/expit/trades.aspx')
    driver.implicitly_wait(10)
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/div/a[1]')
    element.click()


def find_button_date(nacalo_year, nacalo_mont, day_peradat_znajejie):
    try:
        start = f'20{nacalo_year + 8}.{nacalo_mont}.{day_peradat_znajejie}'
        res = pd.date_range(start=start, end=date.today(), freq="D").tolist()
        for i in range(len(res)):
            count_dat = count_spisoc_dji_prodoljenia_zikla_dat[-1]
            count_spisoc_dji_prodoljenia_zikla_dat.append(count_dat)
            res_1 = str(res[i + count_spisoc_dji_prodoljenia_zikla_dat[-1]])
            print(res_1)
            data_perevod_v_stroky = ''.join(res_1)
            year_except = int(data_perevod_v_stroky[2] + data_perevod_v_stroky[3]) - 8
            mont_except = int(data_perevod_v_stroky[5] + data_perevod_v_stroky[6])
            day_except = int(data_perevod_v_stroky[8] + data_perevod_v_stroky[9])
            if mont_except >= 10:
                mont_except = mont_except
            else:
                mont_except = int(data_perevod_v_stroky[6])
            if day_except >= 10:
                day_except = day_except
            else:
                day_except = int(data_perevod_v_stroky[9])
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,
                                f' /html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/form/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[3]/select/option[{year_except}]').click()
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/form/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/select/option[{mont_except}]').click()
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/form/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/select/option[{day_except}]').click()
            print(data_perevod_v_stroky[0], data_perevod_v_stroky[1], data_perevod_v_stroky[2],
                  data_perevod_v_stroky[3],
                  data_perevod_v_stroky[5], data_perevod_v_stroky[6], data_perevod_v_stroky[8],
                  data_perevod_v_stroky[9])
            driver.implicitly_wait(10)
            element_button()
            driver.implicitly_wait(10)
            print("День", day_except)

            test = str(spisok_dat_dlj_ostanovki_zikla[-1]).replace('.', '-')  # идеи проверка для остановки
            data_na_saite_proverka_1 = datetime.strptime(test, '%d-%m-%Y').date()
            now = datetime.now()
            proverka = now.strftime('%d-%m-%Y')
            if str(data_na_saite_proverka_1) == str(proverka):
                vse_ostanovka.append(1)
            driver.get('https://www.moex.com/ru/expit/trades.aspx')
            if os.path.isfile('tabliza_prozentov_akzi.csv') == True:
                start = start
            else:
                start = '01.01.2010'
            res = pd.date_range(start=start, end=date.today(), freq="D").tolist()
            for k in range(len(res)):
                if vse_ostanovka[-1] == 1:
                    return
                if os.path.isfile('tabliza_prozentov_akzi.csv') == True:
                    count_1 = count_spisoc_dji_prodoljenia_zikla_prodolzenie[-1]
                    count_1 = count_spisoc_dji_prodoljenia_zikla_prodolzenie.append(count_1 + 1)
                    res_1 = str(res[count_spisoc_dji_prodoljenia_zikla_prodolzenie[k + 1]])
                else:
                    count = count_spisoc_dji_prodoljenia_zikla[-1]
                    count = count_spisoc_dji_prodoljenia_zikla.append(count + 1)
                    res_1 = str(res[i + count_spisoc_dji_prodoljenia_zikla[-1]])
                print(res_1)
                data_perevod_v_stroky = ''.join(res_1)
                year_except = int(data_perevod_v_stroky[2] + data_perevod_v_stroky[3]) - 8
                mont_except = int(data_perevod_v_stroky[5] + data_perevod_v_stroky[6])
                day_except = int(data_perevod_v_stroky[8] + data_perevod_v_stroky[9])
                if mont_except >= 10:
                    mont_except = mont_except
                else:
                    mont_except = int(data_perevod_v_stroky[6])
                if day_except >= 10:
                    day_except = day_except
                else:
                    day_except = int(data_perevod_v_stroky[9])
                print(data_perevod_v_stroky[0], data_perevod_v_stroky[1], data_perevod_v_stroky[2],
                      data_perevod_v_stroky[3],
                      data_perevod_v_stroky[5], data_perevod_v_stroky[6], data_perevod_v_stroky[8],
                      data_perevod_v_stroky[9])

                data_zikl = dict(spisok_dat_dlj_ostanovki_zikla=spisok_dat_dlj_ostanovki_zikla)
                df = pd.DataFrame(data_zikl)
                df.to_csv('data_zikl.csv', sep=',', index=False, header=False, mode='w')
                time.sleep(4)  # удалить потом
                find_button_date(nacalo_year=year_except, nacalo_mont=mont_except,
                                 day_peradat_znajejie=day_except)

    except Exception as e:
        print(e)
        with open('ochibka_find_button.txt', 'a') as x:
            x.write(str(spisok_dat_dlj_ostanovki_zikla[-1]) + "\n")
        time.sleep(10)
        driver.refresh()
        pyautogui.press('enter')
        find_button_date(nacalo_year=year_except, nacalo_mont=mont_except, day_peradat_znajejie=day_except)


def element_button():
    # функция наживает кнопку для вызова таблицы и потом парсит данные таблицы в списки по столбикам
    try:
        global tabliza_prozentov_akzi, tabliza_prozentov_akzi_1, tabliza_prozentov_akzi_2, \
            tabliza_prozentov_akzi_3, tabliza_prozentov_akzi_4, tabliza_prozentov_akzi_5, tabliza_prozentov_akzi_7, tabliza_prozentov_akzi_8, tabliza_prozentov_akzi_9, \
            tabliza_prozentov_akzi_10, tabliza_prozentov_akzi_11, tabliza_prozentov_akzi_12, tabliza_prozentov_akzi_13, spisok_dat_dlj_sverki
        tabliza_prozentov_akzi_1 = []
        tabliza_prozentov_akzi_2 = []
        tabliza_prozentov_akzi_3 = []
        tabliza_prozentov_akzi_4 = []
        tabliza_prozentov_akzi_5 = []
        tabliza_prozentov_akzi_7 = []
        tabliza_prozentov_akzi_8 = []
        tabliza_prozentov_akzi_9 = []
        tabliza_prozentov_akzi_10 = []
        tabliza_prozentov_akzi_11 = []
        tabliza_prozentov_akzi_12 = []
        tabliza_prozentov_akzi_13 = []
        spisok_dat_dlj_sverki = []

        global tabliza_5prozentov_akzi_1, tabliza_5prozentov_akzi_2, \
            tabliza_5prozentov_akzi_3, tabliza_5prozentov_akzi_4, tabliza_5prozentov_akzi_5, tabliza_5prozentov_akzi_7, tabliza_5prozentov_akzi_8, \
            tabliza_5prozentov_akzi_9, tabliza_5prozentov_akzi_10, tabliza_5prozentov_akzi_11, tabliza_5prozentov_akzi_12, tabliza_5prozentov_akzi_13, spisok_dat_dlj_sverki_5
        tabliza_5prozentov_akzi_1 = []
        tabliza_5prozentov_akzi_2 = []
        tabliza_5prozentov_akzi_3 = []
        tabliza_5prozentov_akzi_4 = []
        tabliza_5prozentov_akzi_5 = []
        tabliza_5prozentov_akzi_7 = []
        tabliza_5prozentov_akzi_8 = []
        tabliza_5prozentov_akzi_9 = []
        tabliza_5prozentov_akzi_10 = []
        tabliza_5prozentov_akzi_11 = []
        tabliza_5prozentov_akzi_12 = []
        tabliza_5prozentov_akzi_13 = []
        spisok_dat_dlj_sverki_5 = []

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').click()

        driver.implicitly_wait(10)
        data_na_saite = driver.find_element(By.XPATH,
                                            '/ html / body / div[3] / div[3] / div / div / div[1] / div / div / div / div / table[3] / tbody / tr / td')
        spisok_dat_dlj_ostanovki_zikla.append(data_na_saite.text)

        def test_5(znajeina_5):
            driver.implicitly_wait(10)
            individual_element_5_prozentov = driver.find_elements(By.XPATH,
                                                                  f'/ html / body / div[3] / div[3] / div / div / div[1] / div / div / div / div / table[5] / tbody / tr / td[{znajeina_5}]')
            for i in individual_element_5_prozentov:
                if znajeina_5 == 1:
                    tabliza_5prozentov_akzi_1.append(i.text)
                elif znajeina_5 == 2:
                    tabliza_5prozentov_akzi_2.append(i.text)
                elif znajeina_5 == 3:
                    tabliza_5prozentov_akzi_3.append(i.text)
                elif znajeina_5 == 4:
                    tabliza_5prozentov_akzi_4.append(i.text)
                elif znajeina_5 == 5:
                    tabliza_5prozentov_akzi_5.append(i.text)
                elif znajeina_5 == 7:
                    tabliza_5prozentov_akzi_7.append(i.text)
                elif znajeina_5 == 8:
                    tabliza_5prozentov_akzi_8.append(i.text)
                elif znajeina_5 == 9:
                    tabliza_5prozentov_akzi_9.append(i.text)
                elif znajeina_5 == 10:
                    tabliza_5prozentov_akzi_10.append(i.text)
                elif znajeina_5 == 11:
                    tabliza_5prozentov_akzi_11.append(i.text)
                elif znajeina_5 == 12:
                    tabliza_5prozentov_akzi_12.append(i.text)
                elif znajeina_5 == 13:
                    tabliza_5prozentov_akzi_13.append(i.text)
                    spisok_dat_dlj_sverki_5.append(spisok_dat_dlj_ostanovki_zikla[-1])

        driver.implicitly_wait(10)
        test_5(znajeina_5=1)
        if tabliza_5prozentov_akzi_1[-1] != str('На эту дату нет сделок'):
            proverka_dlj_sochanenia_5.append('Работает')
            driver.implicitly_wait(10)
            test_5(znajeina_5=2), test_5(znajeina_5=3), test_5(znajeina_5=4), test_5(znajeina_5=5), test_5(
                znajeina_5=7),
            test_5(znajeina_5=8), test_5(znajeina_5=9), test_5(znajeina_5=10), test_5(znajeina_5=11),
            test_5(znajeina_5=12), test_5(znajeina_5=13)
            print('Работает 5 процентов таблицу')
        else:
            del tabliza_5prozentov_akzi_1[-1]
            print('Нету сделок на этот день, 5 процентых таблиц')

        def test(znajeina):

            driver.implicitly_wait(10)
            individual_element = driver.find_elements(By.XPATH,
                                                      f'/ html / body / div[3] / div[3] / div / div / div[1] / div / div / div / div / table[7] / tbody / tr / td[{znajeina}]')
            for i in individual_element:
                if znajeina == 1:
                    tabliza_prozentov_akzi_1.append(i.text)
                elif znajeina == 2:
                    tabliza_prozentov_akzi_2.append(i.text)
                elif znajeina == 3:
                    tabliza_prozentov_akzi_3.append(i.text)
                elif znajeina == 4:
                    tabliza_prozentov_akzi_4.append(i.text)
                elif znajeina == 5:
                    tabliza_prozentov_akzi_5.append(i.text)
                elif znajeina == 7:
                    tabliza_prozentov_akzi_7.append(i.text)
                elif znajeina == 8:
                    tabliza_prozentov_akzi_8.append(i.text)
                elif znajeina == 9:
                    tabliza_prozentov_akzi_9.append(i.text)
                elif znajeina == 10:
                    tabliza_prozentov_akzi_10.append(i.text)
                elif znajeina == 11:
                    tabliza_prozentov_akzi_11.append(i.text)
                elif znajeina == 12:
                    tabliza_prozentov_akzi_12.append(i.text)
                elif znajeina == 13:
                    tabliza_prozentov_akzi_13.append(i.text)
                    spisok_dat_dlj_sverki.append(spisok_dat_dlj_ostanovki_zikla[-1])

        driver.implicitly_wait(10)
        test(znajeina=1)
        if tabliza_prozentov_akzi_1[-1] != str('На эту дату нет сделок'):
            proverka_dlj_sochanenia.append('Работает')
            driver.implicitly_wait(10)
            test(znajeina=2), test(znajeina=3), test(znajeina=4), test(znajeina=5), test(znajeina=7), test(znajeina=8),
            test(znajeina=9), test(znajeina=10), test(znajeina=11), test(znajeina=12), test(znajeina=13)
            print('Работает меньше 5 процентов')
        else:
            del tabliza_prozentov_akzi_1[-1]
            print('Нету сделок на этот день меньше 5 процентов')
        if proverka_dlj_sochanenia_5[-1] == 'Работает':
            del proverka_dlj_sochanenia_5[-1]
            if os.path.isfile('tabliza_5prozentov_akzi.csv') == True:
                socharenie_5(header=False, mode='a')
                print('Сохраняю 5')
            else:
                socharenie_5(header=True, mode='a')
                print('Сохраняю 5')

        if proverka_dlj_sochanenia[-1] == 'Работает':
            del proverka_dlj_sochanenia[-1]

            if os.path.isfile('tabliza_prozentov_akzi.csv') == True:
                socharenie(header=False, mode='a')
                print('Сохраняю')
            else:
                socharenie(header=True, mode='a')
                print('Сохраняю')

    except Exception as s:
        print(s)
        with open('ochibka.txt', 'a') as x:
            if len(spisok_dat_dlj_ostanovki_zikla) != 0:
                x.write(str(spisok_dat_dlj_ostanovki_zikla[-1]) + "\n")
        time.sleep(10)
        driver.refresh()
        pyautogui.press('enter')
        element_button()


def socharenie_5(header, mode):
    data = dict(tabliza_5prozentov_akzi_1=tabliza_5prozentov_akzi_1,
                tabliza_5prozentov_akzi_2=tabliza_5prozentov_akzi_2,
                tabliza_5prozentov_akzi_3=tabliza_5prozentov_akzi_3,
                tabliza_5prozentov_akzi_4=tabliza_5prozentov_akzi_4,
                tabliza_5prozentov_akzi_5=tabliza_5prozentov_akzi_5,
                tabliza_5prozentov_akzi_7=tabliza_5prozentov_akzi_7,
                tabliza_5prozentov_akzi_8=tabliza_5prozentov_akzi_8,
                tabliza_5prozentov_akzi_9=tabliza_5prozentov_akzi_9,
                tabliza_5prozentov_akzi_10=tabliza_5prozentov_akzi_10,
                tabliza_5prozentov_akzi_11=tabliza_5prozentov_akzi_11,
                tabliza_5prozentov_akzi_12=tabliza_5prozentov_akzi_12,
                tabliza_5prozentov_akzi_13=tabliza_5prozentov_akzi_13,
                spisok_dat_dlj_sverki_5=spisok_dat_dlj_sverki_5)

    df = pd.DataFrame(data)
    df.to_csv('tabliza_5prozentov_akzi.csv', sep=',', index=False, header=header, mode=mode)


def socharenie(header, mode):
    data = dict(tabliza_prozentov_akzi_1=tabliza_prozentov_akzi_1,
                tabliza_prozentov_akzi_2=tabliza_prozentov_akzi_2,
                tabliza_prozentov_akzi_3=tabliza_prozentov_akzi_3,
                tabliza_prozentov_akzi_4=tabliza_prozentov_akzi_4,
                tabliza_prozentov_akzi_5=tabliza_prozentov_akzi_5,
                tabliza_prozentov_akzi_7=tabliza_prozentov_akzi_7,
                tabliza_prozentov_akzi_8=tabliza_prozentov_akzi_8,
                tabliza_prozentov_akzi_9=tabliza_prozentov_akzi_9,
                tabliza_prozentov_akzi_10=tabliza_prozentov_akzi_10,
                tabliza_prozentov_akzi_11=tabliza_prozentov_akzi_11,
                tabliza_prozentov_akzi_12=tabliza_prozentov_akzi_12,
                tabliza_prozentov_akzi_13=tabliza_prozentov_akzi_13,
                spisok_dat_dlj_sverki=spisok_dat_dlj_sverki)

    df = pd.DataFrame(data)
    df.to_csv('tabliza_prozentov_akzi.csv', sep=',', index=False, header=header, mode=mode)


def main():
    if os.path.isfile('data_zikl.csv') == True:
        os.remove('data_zikl.csv')
    if os.path.isfile('ochibka.txt') == True:
        os.remove('ochibka.txt')
    if os.path.isfile('ochibka_find_button.txt') == True:
        os.remove('ochibka_find_button.txt')
    start_prog()
    time.sleep(3)
    if os.path.isfile('tabliza_prozentov_akzi.csv') == True:
        znajienie = pd.read_csv('tabliza_prozentov_akzi.csv', low_memory=False)['tabliza_prozentov_akzi_2'].tolist()
        znajienie_start = znajienie[-1]
        znajienie_start = datetime.strptime(znajienie_start, "%d.%m.%Y")
        res = pd.date_range(start=znajienie_start, end=date.today(), freq="D").tolist()
        for i in range(len(res)):
            if i == 1:
                res_1 = str(res[i])
                print(res_1)
                data_perevod_v_stroky = ''.join(res_1)
                year_except = int(data_perevod_v_stroky[2] + data_perevod_v_stroky[3]) - 8
                mont_except = int(data_perevod_v_stroky[5] + data_perevod_v_stroky[6])
                day_except = int(data_perevod_v_stroky[8] + data_perevod_v_stroky[9])
                if mont_except >= 10:
                    mont_except = mont_except
                else:
                    mont_except = int(data_perevod_v_stroky[6])
                if day_except >= 10:
                    day_except = day_except
                else:
                    day_except = int(data_perevod_v_stroky[9])
                find_button_date(nacalo_year=int(year_except), nacalo_mont=int(mont_except),
                                 day_peradat_znajejie=int(day_except))

    else:
        find_button_date(nacalo_year=2, nacalo_mont=1, day_peradat_znajejie=1)


main()

if __name__ == 'main':
    main()
