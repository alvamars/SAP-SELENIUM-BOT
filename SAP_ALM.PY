from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

import time, json

#excel_credencials = r"C:\Users\Alvaro\Desktop\SELENIUM_PYTHON\employees.xlsx"

#df = pandas.read_excel(excel_credencials)

#Id = df["id"][0]
#psw = df["pass"][0]

#selectores
selector_usuario = "#username"
selector_passw = "#password"
boton_ingresar = ".wr-btn"
link_ingreso = ".content > div:nth-child(2) > p:nth-child(7) > span:nth-child(1) > a:nth-child(1)"
boton_select = "#sapUshellAnchorBarOverflowButton"
boton_select1 = "sapUshellAnchorBarOverflowButton-inner"
despleg_menp = "sapUshellTilesContainer-sortable sapUshellInner"
botonmenu_usuario = "meAreaHeaderButton"
lista_usuario = "__list0-listUl" #no Css es ID
opc_listuser_Salir = "__list0-7-logoutBtn" #no Css es ID
btn_salir = "__mbox-btn-0"
menu_app = "shellAppTitle"
ULlist1 = "sapUshellAllMyAppsDataSourcesList-listUl"
LiList1 = "__item1-sapUshellAllMyAppsDataSourcesList-9"
ULList2 = "oItemsContainerlist-listUl"
LiListfin = "__item2-oItemsContainerlist-33"



#Login con credenciales de json
def Login(page):
    with open("/Users/alvaro/Documents/SELENIUM_PYTHON/employees.json") as json_file:
        data = json.load(json_file)
        
        for p in data["employees"]:
            print("im" + str(p["id"]))
            id = "im" + str(p["id"])
            print(str(p["pass"]) + "is loading..")
            passw = str(p["pass"])

            match page:
                case "intranet":
                    driver.get("https://intranet.imm.gub.uy")

                    time.sleep(1)
                
                case "internet":
                    driver.get("https://portalfuncionariadoim.montevideo.gub.uy")
                    driver.find_element(By.ID,"input_1").send_keys(id)
                    driver.find_element(By.ID,"input_2").send_keys(passw)
                    driver.find_element(By.CLASS_NAME,"credentials_input_submit").click()
                    time.sleep(1)

                case "SAP":
                    driver.find_element(By.ID,"username").send_keys(id)
                    driver.find_element(By.ID,"password").send_keys(passw)
                    driver.find_element(By.CSS_SELECTOR,boton_ingresar).click()
                    
                    time.sleep(3)

                case "SAP.exit":
                    driver.find_element(By.ID,botonmenu_usuario).click()
                    lista_user = driver.find_element(By.ID,lista_usuario)
                    try:
                        lista_usersel = lista_user.find_element(By.XPATH,'//*[@id="__list0-7-logoutBtn-img"]')

                    except:
                        lista_usersel = lista_user.find_element(By.XPATH,'//*[@id="__list0-6-logoutBtn-img"]')


                    lista_usersel.click()
                    time.sleep(2)
                    #btnsalir = driver.find_element(By.ID,'//*[@id="__mbox-btn-0"]')
                    #btnsalir = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/footer/div/button[1]")
                    #btnsalir.click()
                    focused_element = driver.switch_to.active_element
                    focused_element.click()
                case _:
                    return print("opc no valida")
        time.sleep(1)


#iniciar navegador 
driver_service = Service(executable_path="/Users/alvaro/Documents/SELENIUM_PYTHON/DriverFirefox/geckodriver" )
driver = webdriver.Firefox(service=driver_service)

Login("intranet")
#driver.get("https://is.imm.gub.uy/authenticationendpoint/login.do?RelayState=28c75824-4ec6-4d05-bfd5-aa5c6c69d552&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=iwaUNgXvYgdwwcP1TugDQ2QHz9yL8uCDTJnC%2BvEF7ACaqQsYMmof4gNCfA7H25kGIk1wkzqlRa7znQFkL7Ptt4vTSyj2X4Iy5K%2FJVRKJByHbGJi83SDHu7C8f4Ii%2BlUnOOg1CAx58TG6ap3JUQFZUKU%2Fa8ckcLHGSMORiseDZTsv5xK8VKSk56j79XXnT13HnVJ0sE1pS8EPJE8N2E0hyE%2B19Im%2F8q7tKoQ6sWQnGK1LERZtxCzurHEDYtUaIUh0ekk7EykYmIxDND9ybbt%2FOpMNKuXtZgnh5oq5ofnYwb4wf18Y6FsPQyUiOCnRFS5Unt1b%2BndxpELBIQ2qDli9hA%3D%3D&commonAuthCallerPath=%2Fsamlsso&forceAuth=false&passiveAuth=false&tenantDomain=carbon.super&sessionDataKey=b12aba9a-e128-476c-8ece-fe93174368bc&relyingParty=ih.montevideo.gub.uy&type=samlsso&sp=ih.montevideo.gub.uy&isSaaSApp=false&authenticators=BasicAuthenticator:LOCAL#Shell-home")
#with open("employees.json" , "r") as json_file:

#driver.get("https://grp.imm.gub.uy/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=100&sap-language=ES&sap-ushell-config-url=cfg/sap/PersonalizationOff.json#Shell-home")

time.sleep(3)
driver.find_element(By.LINK_TEXT,"SAP").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT,"aquí").click()
time.sleep(5)

Login("SAP")
driver.refresh()
time.sleep(6)



driver.find_element(By.ID,menu_app).click()
time.sleep(1)
ListaApp = driver.find_element(By.ID,ULlist1)
ListaApp.find_element(By.ID,LiList1).click()
listacompra = driver.find_element(By.ID,ULList2)
listacompra.find_element(By.ID,LiListfin).click()
#contenedor = driver.find_element(By.ID,"u577A225")
#driver.find_element(By.ID,"ls-inputfieldhelpbutton").click()
#driver.find_element(By.ID,"screenarea1.B10701").click()
#//*[@id="M0:46:::11:34-r"]
time.sleep(2)
focused_element = driver.switch_to.active_element
print("foco en ----")
print(focused_element.get_attribute('outerHTML'))
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys(Keys.TAB)
focused_element.send_keys("ALV")
print("foco en ----")
print(focused_element.get_attribute('outerHTML'))
#driver.find_element(By.ID,"M0:50::btn[8]").click()

#for x in range(62):
#    focused_element.send_keys(Keys.TAB)
#focused_element.click()
#focused_element.send_keys("A")
"""""
tableimput = contenedor.find_element(By.XPATH,'//*[@id="M0:46:::11:34-r"]')
celda = tableimput.find_element(By.CLASS_NAME,"lsField__inputcontainer")
celda.find_element(By.CLASS_NAME,"lsField__input").send_keys("ALV")

driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/div/form/div/div[4]/div/div[34]/table/tbody/tr/td/input").send_keys("ALV")
driver.find_element(By.ID,"M0:46:::18:34").send_keys("01.01.2022")
driver.find_element(By.ID,"M0:46:::18:59").send_keys("31.12.2022")

driver.find_element(By.ID,"M0:50::btn[8]").click()

time.sleep(12)
"""""
"""""
driver.find_element(By.ID,boton_select1).click
time.sleep(2)
list_imput = driver.find_element(By.ID,"__container5-groupheader")
list_imput.find_element(By.XPATH,'//*[@id="__tile100"]').click
"""""



time.sleep(3)
Login("SAP.exit")


#"Mosaico Visualizar documentos de compras por imputacion
#40
"""""
SAPdespleg1 = driver.find_element(By.ID,despleg_menp)
SAPdespleg1.click()
SAPdespleg1_select = Select(SAPdespleg1)
SAPdespleg1_opcion = SAPdespleg1_select.select_by_index(12)
SAPdespleg1_opcion.click()
"""""
#SAPopc_Cimputa =  driver.find_element(By.ID,"__tile115")
#SAPopc_Cimputa.click()
#SAPopcSel = Select(SAPopc_Cimputa).select_by_visible_text("Visua­li­zar_docu­men­tos_de_com­pras_por_impu­tación")
#SAPopcSel.click()

#driver.find_element(By.ID,"__item0-anchorNavigationBar-4").click()
#driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/div/section/div/div[5]/div/div/ul/li[41]/div/a").click()
#driver.find_element(By.ID,"__tile115").click()
"""""
 /html/body/div[2]/div/div/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/div/section/div/div[5]/div/div/ul/li[41]/div/a/div/div
/html/body/div[2]/div/div/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/div/section/div/div[5]/div/div/ul/li[41]/div/a/div
/html/body/div[2]/div/div/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/div/section/div/div[5]/div/div/ul/li[41]/div/a
/html/body/div[2]/div/div/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/div/section/div/div[5]/div/div/ul/li[41]/div/a/div/div/div[1]/div
"""
time.sleep(8)
#driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/div/section/div/div[5]/div/div/ul/li[41]/div/a/div/div").click()
#Select(driver.find_element_by_id(boton_select1)).select_by_visible_text("IM_MM_CREAR_RESERVAS")
#time.sleep(10)
#operando dentro de SAP

#driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/div/form/div/div[4]/div/div[34]/table/tbody/tr/td/input").send_keys("ALV")
#driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/div/form/div/div[4]/div/div[66]/table/tbody/tr/td/input").send_keys("01.01.2022")
#driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/div/form/div/div[4]/div/div[68]/table/tbody/tr/td/input").send_keys("30.12.2022")
#driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/div/form/div/div[5]/div/div/div[1]/span[2]/div").click()



    #data = json.load(json_file)

   # for p in data ["employees"]:
       # print(p["name"]+" is loading!")

       

        

       # userId = driver.find_element_by_id("username")
       # userId.send_keys(p["id"])

       # userPass = driver.find_element_by_id("password")
       # userId.send_keys(p["pass"])



driver.close()