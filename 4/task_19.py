# #todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# # id) - номер по порядку (от 1 до 10);
# # значение из списка algoritm

# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#              "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#              "Наивный байесовский классификатор", "CART" ]

# # Каждое значение из списка должно находится на отдельной строке.
# # Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....
if __name__ == "__main__":
    algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
                "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
                "Наивный байесовский классификатор", "CART" ]

    with open("./algoritm.csv", mode="w", encoding="utf-8-sig") as file:
        for index, value in enumerate(algoritm,start=1):
            file.write(f'{index});"{value}"\n')