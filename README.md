Required Dependencies (install menggunakan command jika terjadi error):
1. Python
2. requests (pip install requests)
3. pytest (pip install pytest)
4. allure-pytest (pip install allure-pytest)
5. pytest-html (pip install pytest-html)

buka cmd
Navigasikan ke folder GorestAPIAutomation

set token menggunakan command:
set GOREST_TOKEN=Bearer (input token anda)

jalankan command untuk melakukan testing:
pytest --alluredir=reports

jalankan command untuk mencetak reports:
pytest --html=report.html

report.html akan terbentuk pada folder GorestAPIAutomation

buka report.html untuk membuka report
