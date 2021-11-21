# Testikattavuusraportti
    * ``` poetry add coverage --dev ```
    * ``` coverage run --branch -m pytest src```
    * ``` coverage report -m ```
    * ``` coverage html ```
    * Järkevää voisi olla esimerkiksi jättää testihakemisto, käyttöliittymän koodin hakemisto ja src/index.py-tiedosto testikattavuuden ulkopuolle.
# Invoke
    * Toteutus dekoraattori @task avulla