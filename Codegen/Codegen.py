from playwright.sync_api import Playwright, sync_playwright


with sync_playwright() as p:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://app.apollo.io/#/login?redirectTo=https%3A%2F%2Fapp.apollo.io%2F%23%2F
    page.goto("https://app.apollo.io/#/login?redirectTo=https%3A%2F%2Fapp.apollo.io%2F%23%2F")

    # Click [placeholder="Work Email"]
    page.click("[placeholder=\"Work Email\"]")

    # Fill [placeholder="Work Email"]
    page.fill("[placeholder=\"Work Email\"]", "mhawar2018a@gmail.com")

    # Click [placeholder="Enter your password"]
    page.click("[placeholder=\"Enter your password\"]")

    # Fill [placeholder="Enter your password"]
    page.fill("[placeholder=\"Enter your password\"]", "mhawar2001")

    # Click :nth-match(:text("Log In"), 3)
    # with page.expect_navigation(url="https://app.apollo.io/#/onboarding/select-use-case"):
    with page.expect_navigation():
        page.click(":nth-match(:text(\"Log In\"), 3)")

    # Click #sidebar-nav-prospect-search a i
    page.click("#sidebar-nav-prospect-search a i")
    # assert page.url == "https://app.apollo.io/#/people?finderViewId=5a205be19a57e40c095e1d5f"

    # Click button:has-text("Load")
    page.click("button:has-text(\"Load\")")

    # Click text=More +
    page.click("text=More +")

    # Click text=investor directors
    # with page.expect_navigation(url="https://app.apollo.io/#/people?finderViewId=6193aa5e7bd74600a4730f5f&personTitles[]=investor&personTitles[]=VC&personTitles[]=angel&personTitles[]=seed&personTitles[]=CEO&personTitles[]=director&qPersonTitle=-relations&personSeniorities[]=owner&personSeniorities[]=founder&personSeniorities[]=c_suite&personSeniorities[]=partner&personSeniorities[]=vp&personSeniorities[]=head&personSeniorities[]=director&qNotOrganizationSearchListId=6197acb35a85f600da353568&qSearchListId=6193a9f5bed00100a44903ed"):
    with page.expect_navigation():
        page.click("text=investor directors")

    # Click text=Net New (31)
    page.click('#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div.zp_3cHPT > div.zp_3Lzj1 > div > div > div > div.finder-explorer-sidebar-shown.zp_1cI0A.zp_iYGsF > div.zp_1ybjt > div > div.zp_2Ubb3 > div > div > a:nth-child(2)')
    # assert page.url == "https://app.apollo.io/#/people?finderViewId=6193aa5e7bd74600a4730f5f&personTitles[]=investor&personTitles[]=VC&personTitles[]=angel&personTitles[]=seed&personTitles[]=CEO&personTitles[]=director&qPersonTitle=-relations&personSeniorities[]=owner&personSeniorities[]=founder&personSeniorities[]=c_suite&personSeniorities[]=partner&personSeniorities[]=vp&personSeniorities[]=head&personSeniorities[]=director&qNotOrganizationSearchListId=6197acb35a85f600da353568&qSearchListId=6193a9f5bed00100a44903ed&prospectedByCurrentTeam[]=no&page=1"
   
    for i in range (0,100):

       # Click .zp_3laQp
       page.click(".zp_3laQp")

       # Click text=Select Page
       page.click("text=Select Page")

      # Click span:nth-child(4) .zp-button
       page.click("span:nth-child(4) .zp-button")

       # Click text=Add to Lists
       page.click("text=Add to Lists")

      # Click text=Enter or create lists...
      page.click("text=Enter or create lists...")

      # Click text=investors apollo
      page.click("text=investors apollo")
  
      # Click text=Confirm
      page.click("text=Confirm")

      # Click text=1 - 25 of 311 >> :nth-match(img, 4)
      page.click("text=1 - 25 of 311 >> :nth-match(img, 4)")
      # assert page.url == "https://app.apollo.io/#/people?finderViewId=6193aa5e7bd74600a4730f5f&personTitles[]=investor&personTitles[]=VC&personTitles[]=angel&personTitles[]=seed&personTitles[]=CEO&personTitles[]=director&qPersonTitle=-relations&personSeniorities[]=owner&personSeniorities[]=founder&personSeniorities[]=c_suite&personSeniorities[]=partner&personSeniorities[]=vp&personSeniorities[]=head&personSeniorities[]=director&qNotOrganizationSearchListId=6197acb35a85f600da353568&qSearchListId=6193a9f5bed00100a44903ed&prospectedByCurrentTeam[]=no&page=2"




with sync_playwright() as playwright:
    run(playwright)
