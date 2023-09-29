import requests
from bs4 import BeautifulSoup


import urllib.parse

session = requests.Session()

session.headers.update({
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
'Referer': 'https://aca-prod.accela.com/COSPRINGS/Cap/CapHome.aspx?module=Enforcement&TabName=Enforcement&TabList=Home%7c0%7cPolice%7c1%7cPlanning%7c2%7cPublicWorks%7c3%7cEnforcement%7c4%7cLicensing%7c5%7cStormWater%7c6%7cCurrentTabIndex%7c4'
})

# url = "https://aca-prod.accela.com/COSPRINGS/header.html"
# response=session.get(url)
# session.cookies.update(response.cookies.get_dict())
# print(response.text)

url2='https://aca-prod.accela.com/COSPRINGS/WebService/AnnouncementService.asmx/GetAnnouncementOfSession'
response2=session.get(url2)
session.cookies.update(response2.cookies.get_dict())



url3='https://aca-prod.accela.com/COSPRINGS/Cap/CapHome.aspx?module=Enforcement&TabName=Enforcement&TabList=Home%7c0%7cPolice%7c1%7cPlanning%7c2%7cPublicWorks%7c3%7cEnforcement%7c4%7cLicensing%7c5%7cStormWater%7c6%7cCurrentTabIndex%7c4'
# data={
#     'ctl00$ScriptManager1': 'ctl00$PlaceHolderMain$updatePanel|ctl00$PlaceHolderMain$generalSearchForm$ddlGSPermitType',
#     'ctl00$HeaderNavigation$hdnShoppingCartItemNumber': '',
#     'ctl00$HeaderNavigation$hdnShowReportLink': 'N',
#     'ctl00$PlaceHolderMain$addForMyPermits$collection': 'rdoExistCollection',
#     'ctl00$PlaceHolderMain$addForMyPermits$ddlMyCollection': '',
#     'ctl00$PlaceHolderMain$addForMyPermits$txtName': '',
#     'ctl00$PlaceHolderMain$addForMyPermits$txtDesc': '',
#     'ctl00$PlaceHolderMain$ddlSearchType': '0',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSPermitNumber': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$ddlGSPermitType': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate': '09/30/2013',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate_ext_ClientState': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate': '09/28/2023',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate_ext_ClientState': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ChildControl0': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl0_watermark_exd_ClientState': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ChildControl1': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSNumber$ctl00_PlaceHolderMain_generalSearchForm_txtGSNumber_ChildControl1_watermark_exd_ClientState': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$ddlGSDirection': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSStreetName': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$ddlGSStreetSuffix': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$ddlGSUnitType': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSUnitNo': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSCity': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$ddlGSState$State1': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit_ZipFromAA': '0',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit_zipMask': '',
#     'ctl00$PlaceHolderMain$generalSearchForm$txtGSAppZipSearchPermit_ext_ClientState': '',
#     'ctl00$PlaceHolderMain$hfASIExpanded': '',
#     'ctl00$PlaceHolderMain$txtHiddenDate': '',
#     'ctl00$PlaceHolderMain$txtHiddenDate_ext_ClientState': '',
#     'ctl00$PlaceHolderMain$dgvPermitList$lblNeedReBind': '',
#     'ctl00$PlaceHolderMain$dgvPermitList$gdvPermitList$hfSaveSelectedItems': '',
#     'ctl00$PlaceHolderMain$dgvPermitList$inpHideResumeConf': '',
#     'ctl00$PlaceHolderMain$hfGridId': '',
#     'ctl00$HDExpressionParam': '',
#     'Submit': 'Submit',
#     '__EVENTTARGET': 'ctl00$PlaceHolderMain$updatePanel|ctl00$PlaceHolderMain$generalSearchForm$ddlGSPermitType',
#     '__EVENTARGUMENT': '',
#     '__LASTFOCUS': '',
#     '__VIEWSTATE': viewstate_value,
#     '__VIEWSTATEGENERATOR': view_state_generator_value,
#     'ACA_CS_FIELD': acs_value,
#     '__AjaxControlToolkitCalendarCssLoaded': '',
#     '__VIEWSTATEENCRYPTED': '',
#     '__ASYNCPOST': 'true'
# }
# encoded_data=urllib.parse.urlencode(data)

response3 = session.post(url3)
session.cookies.update(response3.cookies.get_dict())





soup = BeautifulSoup(response3.content, 'html.parser')
viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
viewstate_value = viewstate_input.get('value')
acs_input = soup.find('input', {'name': 'ACA_CS_FIELD'})
acs_value = acs_input.get('value')
event_target=soup.find('input', {'name': '__EVENTTARGET'})
view_state_generator=soup.find('input', {'name': '__VIEWSTATEGENERATOR'})
view_state_generator_value=view_state_generator.get('value')



data={
    'ctl00$ScriptManager1': 'ctl00$PlaceHolderMain$updatePanel|ctl00$PlaceHolderMain$btnNewSearch',
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
    '__EVENTTARGET': 'ctl00$PlaceHolderMain$btnNewSearch',
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

response4 = session.post(url3,data=encoded_data)
print(response4.text)
session.cookies.update(response4.cookies.get_dict())


