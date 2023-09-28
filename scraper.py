import requests
from bs4 import BeautifulSoup


import urllib.parse

url='https://aca-prod.accela.com/COSPRINGS/Cap/CapHome.aspx?module=Enforcement&TabName=Enforcement&TabList=Home%7c0%7cPolice%7c1%7cPlanning%7c2%7cPublicWorks%7c3%7cEnforcement%7c4%7cLicensing%7c5%7cStormWater%7c6%7cCurrentTabIndex%7c4'
# Send a request to the website
response = requests.get(url)
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'ApplicationGatewayAffinityCORS=c144fc4bda0d9cce7851076f46fbf365; ApplicationGatewayAffinity=c144fc4bda0d9cce7851076f46fbf365; ACA_SS_STORE=dhy5h3ljivzvfbaur0h2t1zq; ACA_USER_PREFERRED_CULTURE=en-US; ACA_CS_KEY=cccfce599c01497ca9fe3d4ef0fa1aee; TabNav=Home|0|Police|1|Planning|2|PublicWorks|3|Enforcement|4|Licensing|5|StormWater|6|CurrentTabIndex|4; .ASPXANONYMOUS=2saPb04RLwRvL2QVy-uIo2U6ZXcAEg7AJq-KxO0ERy97meUtRJPFHsCD7-Afv03SF07kdik-EZbrQrafaW-wTY1Hs2jL109HLCw8gds_S0A-JE0DyzNhEHrRIAY_ekVHneCYMt17kVW5VivNZ3hh0GM1WHo1; LASTEST_REQUEST_TIME=1695900203205; _dd_s=rum=1&id=fe5d563d-74c3-4a70-bc91-aa86aa5db5a2&created=1695889159907&expire=1695897512098; LASTEST_REQUEST_TIME=1695901323688',
  'Origin': 'https://aca-prod.accela.com',
  'Referer': 'https://aca-prod.accela.com/COSPRINGS/Cap/CapHome.aspx?module=Enforcement&TabName=Enforcement&TabList=Home%7c0%7cPolice%7c1%7cPlanning%7c2%7cPublicWorks%7c3%7cEnforcement%7c4%7cLicensing%7c5%7cStormWater%7c6%7cCurrentTabIndex%7c4',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'X-MicrosoftAjax': 'Delta=true',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
if response.status_code == 200:
    data={}
    response = requests.request("POST", url, headers=headers)
  
    soup = BeautifulSoup(response.content, 'html.parser')
    viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
    viewstate_value = viewstate_input.get('value')
    acs_input = soup.find('input', {'name': 'ACA_CS_FIELD'})
    acs_value = acs_input.get('value')
    event_target=soup.find('input', {'name': '__EVENTTARGET'})
    view_state_generator=soup.find('input', {'name': '__VIEWSTATEGENERATOR'})
    view_state_generator_value=view_state_generator.get('value')

    
    data={
    'ctl00$ScriptManager1': 'ctl00$PlaceHolderMain$dgvPermitList$updatePanel|ctl00$PlaceHolderMain$dgvPermitList$gdvPermitList$ctl13$ctl03',
    'ctl00$HeaderNavigation$hdnShoppingCartItemNumber': '',
    'ctl00$HeaderNavigation$hdnShowReportLink': 'N',
    'ctl00$PlaceHolderMain$addForMyPermits$collection': 'rdoExistCollection',
    'ctl00$PlaceHolderMain$addForMyPermits$ddlMyCollection': '',
    'ctl00$PlaceHolderMain$addForMyPermits$txtName': '',
    'ctl00$PlaceHolderMain$addForMyPermits$txtDesc': '',
    'ctl00$PlaceHolderMain$ddlSearchType': '0',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSPermitNumber': '',
    'ctl00$PlaceHolderMain$generalSearchForm$ddlGSPermitType': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate': '09/30/2013',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate_ext_ClientState': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate': '09/28/2023',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate_ext_ClientState': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ChildControl0': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl0_watermark_exd_ClientState': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ChildControl1': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl1_watermark_exd_ClientState': '',
    'ctl00$PlaceHolderMain$generalSearchForm$ddlGSDirection': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSStreetName': '',
    'ctl00$PlaceHolderMain$generalSearchForm$ddlGSStreetSuffix': '',
    'ctl00$PlaceHolderMain$generalSearchForm$ddlGSUnitType': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSUnitNo': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSCity': '',
    'ctl00$PlaceHolderMain$generalSearchForm$ddlGSState$State1': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit_ZipFromAA': '0',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit_zipMask': '',
    'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit_ext_ClientState': '',
    'ctl00$PlaceHolderMain$hfASIExpanded': '',
    'ctl00$PlaceHolderMain$txtHiddenDate': '',
    'ctl00$PlaceHolderMain$txtHiddenDate_ext_ClientState': '',
    'ctl00$PlaceHolderMain$dgvPermitList$lblNeedReBind': '',
    'ctl00$PlaceHolderMain$dgvPermitList$gdvPermitList$hfSaveSelectedItems': '',
    'ctl00$PlaceHolderMain$dgvPermitList$inpHideResumeConf': '',
    'ctl00$PlaceHolderMain$hfGridId': '',
    'ctl00$HDExpressionParam': '',
    'Submit': 'Submit',
    '__EVENTTARGET': 'ctl00$PlaceHolderMain$dgvPermitList$gdvPermitList$ctl13$ctl03',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': viewstate_value,
    '__VIEWSTATEGENERATOR': view_state_generator_value,
    'ACA_CS_FIELD': acs_value,
    '__AjaxControlToolkitCalendarCssLoaded': '',
    '__VIEWSTATEENCRYPTED': '',
    '__ASYNCPOST': 'true'
}
    encoded_data=urllib.parse.urlencode(data)
 
    response = requests.request("POST", url, headers=headers,data=encoded_data)
    print(response.content)

else:
    print(f'Error: {response.status_code}')