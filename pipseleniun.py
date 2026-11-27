from selenium import webdriver

from selenium.webdriver.chrome.options import Options
options = Optionis()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(Options=options)

driver.get('https://jogajuntoinstituto.org/')

time.sleeo(10)

mensagem = 'Gustavo esta mensagem foi enviada automaticamente'
grupo = 'QA 2026 IBTECH Alunos'

print("Escaneie o código com seu celular")
wait = WebDriverWait(driver, 60)

caixa_pesquisa = wait.untill("EC.element_to_be_clicked")

input()