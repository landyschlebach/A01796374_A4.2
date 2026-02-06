# Actividad 4.2: Estándar de codificación PEP-8 & Pylint
```
A01796374_A4.2/
 ├── results/                 <- Resultados de las ejecuciones de cada programa con los recursos de apoyo proporcionados
 │   ├── Compute Statistics/
 │   │   ├── StatisticsResultsTC1.txt
 │   │   ├── StatisticsResultsTC2.txt
 │   │   ├── StatisticsResultsTC3.txt
 │   │   ├── StatisticsResultsTC4.txt
 │   │   ├── StatisticsResultsTC5.txt
 │   │   ├── StatisticsResultsTC6.txt
 │   │   ├── StatisticsResultsTC7.txt
 │   │   ├── README.md       <- Print screens of results per each test case
 │   ├── Converter/
 │   │   ├── ConvertionResultsTC1.txt
 │   │   ├── ConvertionResultsTC2.txt
 │   │   ├── ConvertionResultsTC3.txt
 │   │   ├── ConvertionResultsTC4.txt
 │   │   ├── README.md       <- Print screens of results per each test case
 │   ├── Count Words/
 │   │   ├── WordCountResultsTC1.txt
 │   │   ├── WordCountResultsTC2.txt
 │   │   ├── WordCountResultsTC3.txt
 │   │   ├── WordCountResultsTC4.txt
 │   │   ├── WordCountResultsTC5.txt
 │   │   ├── README.md       <- Print screens of results per each test case
 ├── computeStatistics.py
 ├── convertNumbers.py 
 ├── wordCount.py 
 └── README.md
 ```
**Nota:**\
En cada uno de los programas desarrollados se obtuvo un score de ~9.90 en pylint debido al nombre del archivo.
Para obtener un score de 10.00/10, manteniendo los nombres indicados en la rúbrica se implementó la siguiente regla:
```
# pylint: disable=invalid-name
```

## Pylint: Resultados
Ejercicio de programación #1 (Compute Statistics)
```
PS C:\Users\landyschlebach> pylint computeStatistics.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.90/10, +0.10)
```

Ejercicio de programación #2 (Converter)
```
PS C:\Users\landyschlebach> pylint convertNumbers.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.89/10, +0.11)
```

Ejercicio de programación #3 (Count Words)
```
PS C:\Users\landyschlebach> pylint wordCount.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.84/10, +0.16)
```
