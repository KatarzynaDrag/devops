# dev_ops_lato_2025
## ZADANIE 8 Git action deployment pipeline

Cel laboratoriów. 
Celem laboratoriów jest zapoznanie się z narzędziem git actions a konkretnie z obsługą sekretów jak i możliwością deployowania obrazów do zdalnego repo

# ZADANIE WYKONYWANE NA WŁASNYM KONCIE

### 1 Zaktualizować repo w kilku krokach 
- 1.1 Zaktualizować wszystkie metadane projektu 
```bash
git fetch --all
```

- 1.2 Przełączyć się na branch main 
```bash
git checkout main
```

- 1.3 Pobrać zmiany w kodzie 
```bash
git pull 
```
- 1.3 Stworzyć swój branch roboczy Lab8/nr_indeksu i się na niego przełączyć 



### 2  Utworzyć konto na Docker Hubie
Konto będzie konieczne w celu umieszczenia gotowego obrazu 
- Należy stworzyć konto i zalogować się na docker hubie 
- Utworzyć prywatne repozytorium na obrazy kontenerów 
- Stworzyć token dostępu (ustawienia profilu). UWAGA STWORZONY TOKEN SKOPIOWAĆ, nie ma możliwości ponownego odczytu. Wtedy trzeba zrobić token od zera

###  Utworzyć sekrety na git actions
Sekrety będą potrzebne do obsługi logowania bez podawania hasła w yaml'u
https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions

Sekret stworzyć na zasadzie docker_hub_nr_indeksu.

### 3 Stworzyć folder w oparciu o env_00000
- 3.1 Skopiować zawartość do nowego folderu o nazwie env_nrIndeksu


### 4 OPIS głównego zadania
Mamy 3 joby. Jeden job jest odpowiedzialny za unit testy, drugi za testy funkcjonalne i  trzeci za deployment zbudowanego obrazu. 
Należy tak napisać skrypt yaml aby: 
- Wykonywał się tylko na naszym branchu 
- Uruchamiał się kolejno unit_test->function_test->deployment
- Testowany kod i build z niego dotyczył tylko naszego folderu
- Wykorzystywał nasze sekrety do logowania się do Docker HUBa (ZAKAZ WRZUCANIA SWOICH LOGINÓW I HASEŁ DO YAMLA)
- Naprawić błędy w oprogramowaniu - testy funkcyjne 
- Upewnić się czy udało się wdrożyć poprawny obraz

### 5 Test naszego obrazu 
Należy pobrać obraz na nasz lokalny komputer i go uruchomić (uwaga konieczne będzie logowanie do docker huba za pomocą narzędzi CLI Docker) https://docs.docker.com/reference/cli/docker/login/ 
- Po uruchomieniu obrazu za pomocą komendy docker run -d -p 5000:5000 nazwa_naszego_obrazu uruchomić testy funkcjonalne lokalnie 

### 6 Sprawozdanie 

- 6.1 Sprawozdanie ma być dokumentacją pracy tj opisem wykonanych kroków wraz z zdjęciami i opisem wykorzystywanych metod. Ma ona pozwolić na odtworzenie zadania z wykorzystaniem instrukcji ze sprawozdania 
- 6.2 Ma być ono zapisane za pomocą markdowna w nowo stworzonym  folderze. 


### Zaliczenie laboratoriów 
- Sprawozdanie w docelowej lokalizacji 
- Gotowe do oddania praca i sprawozdanie w postaci commita na branchu z zadaniem  
- Wszelkie edycje skryptów testowych i automatyzujących workflow jest zabronione (czyli plików nie wymienionych w instrukcji)
- Pushe mają być wykonywane WYŁĄCZNIE Z NASZYCH KONT GITHUB 


### Tematy dodatkowe 
- Dlaczego istotne jest wykonywanie deploymentu po testach a nie przed 
- Czym szczególnym różniły się testy funkcjonalne od unit testów
- Dlaczego dobrą praktyką jest instalowanie requirementsów w oddzielnej komendzie RUN (w dockerfile)
- Dlaczego należy korzystać z przygotowanych magazynów haseł 


