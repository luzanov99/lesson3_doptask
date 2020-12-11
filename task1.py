import csv
import copy

with open('data-398-2020-12-081.csv', 'r') as f:
    fields = ['id', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street']
    reader = csv.DictReader(f, fields, delimiter=';')
    list_street=[]
    d1 = []
    d2=dict()
    # Записываю в два списка название всех улиц из файла
    for row in reader:
        element=copy.copy((row['Street']))
        list_street.append(element)
        d1.append(element)
    #Преобразую один список в множество неповторяющихся улиц
    list_street=set(list_street)
    # Создаю словарь со списокм улиц и количеством остановок , устанавливаю значение 0 для каждой улицы
    for Street in list_street:
        d2[Street]=0
    # Подсчитываю количество остановок на улице
    for Street1 in d1:
        if Street1 in d2:
            d2[Street1]+=1
    # Создаю список значение и ключей для вывода максимального количества
    v=list(d2.values())
    k=list(d2.keys())
    result=k[v.index(max(v))]
    print(f'На улице {result} больше всего остановок {max(v)}')
  
    
           
