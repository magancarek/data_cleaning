# Aplikacja Data Cleaning

Aplikacja realizowana w ramach przedmiotu **Pracownia informatyczna**

## Uruchomienie

- Instalacja zależności z pliku *requirements.txt*

```bash
pip install -r requirements.txt
```

- Uruchomienie aplikacji

```bash
python3 main.py
```

## Działanie

Aplikacja data cleaning pozwoli użytkownikowi zaobserwować wartości odstające. Po uruchomieniu aplikacji pojawia się okno główne z przyciskiem DODAJ do wczytywania pliku z danymi w formacie csv, które będą analizowane.
Po wczytaniu danych aplikacja zwróci w nowym oknie informacje o wartościach odstających - okno z wykresem punktowym mający na celu ich wizualną prezentację oraz macierz odległości.


### Technologie
- [wxPython](https://docs.wxpython.org/)
- [pandas](https://pandas.pydata.org/docs/)
- [scipy](https://docs.scipy.org/doc/scipy/)
- [numpy](https://numpy.org/doc/)
- [matplotlib](https://matplotlib.org/)

