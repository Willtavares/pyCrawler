from selenium import webdriver
import csv

especializacoes = ["ginecologista","dermatologista","psicologo",
                    "ortopedista-traumatologista","psiquiatra",
                    "oftalmologista","cardiologista","endocrinologista",
                    "dentista","urologista","neurologista","nutricionista"]
max_page_num = ["/1", "/2", "/3", "/4", "/5", "/6", "/7", "/8", "/9", "/10"]

with open('coleta.csv', 'w') as f:
    f.write("Nome, Especialidade, Rua, Cidade \n")

driver = webdriver.Chrome('C:/Users/William/Downloads/chromedriver_win32/chromedriver.exe')

ulr_adicao = [ str(i) + j for i in especializacoes for j in max_page_num]
for i in range(len(ulr_adicao)):
    url = "https://www.doctoralia.com.br/"+ ulr_adicao[i]
    print(url)
    driver.get(url)

    nome = driver.find_elements_by_xpath('//div[@class="col-xs-9 col-sm-10  col-md-9 content"]//h3[@class="rank-element-name h4 padding-right-2"]//span[@itemprop="name"]')
    especialidade = driver.find_elements_by_xpath('//div[@class="col-xs-9 col-sm-10  col-md-9 content"]//h4[@class="h3 text-muted text-base-size text-base-weight offset-xs-bottom-0 offset-sm-bottom-0"]')
    rua = driver.find_elements_by_xpath('//div[@class="col-xs-9 col-sm-10  col-md-9 content"]//ul[@class="list-unstyled rank-element-addresses"]//li[@class="padding-left-2"]//p//span[@class="street"]')
    cidade = driver.find_elements_by_xpath('//div[@class="col-xs-9 col-sm-10  col-md-9 content"]//ul[@class="list-unstyled rank-element-addresses"]//li[@class="padding-left-2"]//p//span[@class="city"]')

    i=1
    number_pag_itens = len(nome)
    with open('coleta.csv', 'a') as f:
        while i < number_pag_itens:
            f.write(nome[i].text + "," + especialidade[i].text + "," + rua[i].text + "," + cidade[i].text + "\n")
            i += 1
            print("Printando o I: " + str(i))    
            
driver.close()