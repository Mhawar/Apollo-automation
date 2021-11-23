from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
 browser = p.chromium.launch(headless=False,slow_mo=50)
 page = browser.new_page()
 page.goto('https://app.apollo.io/#/people?finderViewId=6193aa5e7bd74600a4730f5f&personTitles[]=investor&personTitles[]=VC&personTitles[]=angel&personTitles[]=seed&personTitles[]=CEO&personTitles[]=director&qPersonTitle=-relations&personSeniorities[]=owner&personSeniorities[]=founder&personSeniorities[]=c_suite&personSeniorities[]=partner&personSeniorities[]=vp&personSeniorities[]=head&personSeniorities[]=director&qNotOrganizationSearchListId=6197acb35a85f600da353568&qSearchListId=6193a9f5bed00100a44903ed')


 page.fill('input#o3-input' , 'mhawar2018a@gmail.com')
 page.fill('input#o4-input' , 'mhawar2001')
 page.click('#provider-mounter > div > div.zp_2Pnik > div.zp_2YB95 > div > div.zp_1QN2s > div > div.zp_p7Ra4.zp_2ZLGm > div > form > div.zp_18q8k > div > div')
 page.click('#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div.zp_3cHPT > div.zp_3Lzj1 > div > div > div > div.finder-explorer-sidebar-shown.zp_1cI0A.zp_iYGsF > div.zp_1ybjt > div > div.zp_2Ubb3 > div > div > a:nth-child(2)')

 print("Logged i successfully")
 
 
 for i in range (100):
       
       
       page.click('#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div.zp_3cHPT > div.zp_3Lzj1 > div > div > div > div.finder-explorer-sidebar-shown.zp_1cI0A.zp_iYGsF > div.zp_1ybjt > div > div.zp_mtt5S.zp_2xQfh.zp_vXURL > div > div:nth-child(1) > div.zp_3Lc6D > div > div > div')
       print("clicked 1")
       page.click('body > div.apolloio-css-vars-reset.zp-overlay > div > div > div > a:nth-child(1)')
       print(" 2")
       page.click('#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div.zp_3cHPT > div.zp_3Lzj1 > div > div > div > div.finder-explorer-sidebar-shown.zp_1cI0A.zp_iYGsF > div.zp_1ybjt > div > div.zp_mtt5S.zp_2xQfh.zp_vXURL > div > div:nth-child(1) > div.zp-button-group.zp_3tokH.zp_1JYqA > span:nth-child(4) > div')
       print(" 3")
       page.click('body > div.apolloio-css-vars-reset.zp-overlay > div > div > div > a:nth-child(1)')
       print(" 4")
       page.click('body > div.apolloio-css-vars-reset.zp.zp-modal.zp_1aV2y > div.zp_2gRpu > div > div > div.zp_3wjKN > form > div > div > div > div > div > div > div > div.zp-select-main > div')
       print(" 5")
       page.click('body > div.apolloio-css-vars-reset.zp.zp-modal.zp_1aV2y > div.zp_2gRpu > div > div > div.zp_3wjKN > form > div > div > div > div > div > div > div.Select-menu-outer > div > div:nth-child(1)')
       print(" 6")
       page.click('body > div.apolloio-css-vars-reset.zp.zp-modal.zp_1aV2y > div.zp_2gRpu > div > div > div.zp_2N-K8 > div > div')
       print(" 7")
       page.click('#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div.zp_3cHPT > div.zp_3Lzj1 > div > div > div > div.finder-explorer-sidebar-shown.zp_1cI0A.zp_iYGsF > div.zp_1ybjt > div > div.zp_p7Ra4 > div > div > div > div > div.zp_3Lry3 > div > div.zp-button-group.zp_3tokH.zp_3HFM6 > div:nth-child(3)')
       print("25 have successfully added!!")

time.sleep(10)


 