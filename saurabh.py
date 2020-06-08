import xlsxwriter
from bs4 import BeautifulSoup
import requests
import pprint
import re
"""
H1: True [Study in <Location> - Courses, Fees & Scope]
H2: True
Meta Title: True
Meta Description: True
URL: True (Remove https://www. and then url should not contain other than: . | - | _ | + | / | A-Z | a-z | 0-9
"""
workbook = xlsxwriter.Workbook('/home/dell/Music/Example.xlsx')
worksheet = workbook.add_worksheet()
# worksheet.write(1, 0, 'hii anchal')
# workbook.close()
DEBUG = False
pp = pprint.PrettyPrinter(indent=2)
sitemap_url = 'https://www.admitkard.com/sitemap.xml'
target_sitemap_url_key = "/location-sitemap.xml"
SPLIT_URL_FROM = "https://www.admitkard.com"
ERROR_STRINGS = {
    "MORE_THAN_ONE_H1_TAG": "Multiple H1 tags found",
    "ZERO_H1_TAGS": "No H1 tags found",
    "H1_TAG_MISMATCH": "H1 tag data is different from expected",
    "MORE_THAN_ONE_META_TAG_TITLE": "Multiple Meta title tags found",
    "ZERO_META_TAGS_TITLE": "No Meta title tags found",
    "META_TAG_TITLE_MISMATCH": "Meta tag title data is different from expected",
    "MORE_THAN_ONE_META_TAG_DESCRIPTION": "Multiple Meta description tags found",
    "ZERO_META_TAGS_DESCRIPTION": "No Meta description tags found",
    "META_TAG_DESCRIPTION_MISMATCH": "Meta tag description data is different from expected",
    "IF URL CONTAIN OTHER THAN . | - | _ | + | / | A-Z | a-z | 0-9" : " URL IS BROKEN"
}

def scrap_url(url):
    content = requests.get(url)
    parsed_content = BeautifulSoup(content.text, 'html.parser')
    return parsed_content
def get_sitemap_content():
    parsed_content = scrap_url(sitemap_url)
    level_0_url_list = parsed_content.find_all('loc')
    if DEBUG:
        pp.pprint({"level 0 URLS": level_0_url_list})
    return level_0_url_list
#For Exam page URL
def extract_target_sitemap_url(url_list):
    for level_0_url in url_list:
        if target_sitemap_url_key in level_0_url.contents[0]:
            target_sitemap_url = level_0_url.contents[0]
    if DEBUG:
        pp.pprint({"Target URL": target_sitemap_url})
    return target_sitemap_url
def get_target_sitemap_content(target_sitemap_url):
    target_sitemap_content = scrap_url(target_sitemap_url)
    # if DEBUG:
    #     pp.pprint({"Target Sitemap URL Content": target_sitemap_content})
    return target_sitemap_content
def extract_target_sitemap_url_list(target_sitemap_url_content):
    level_1_url_list = target_sitemap_url_content.find_all('loc')
    if DEBUG:
        pp.pprint({"End URLS": level_1_url_list})
    return level_1_url_list

def run_seo_checks_for_end_urls(end_urls):
  excel_sheet_row = 0
  for end_url in end_urls:
    run_seo_checks_for_end_url(end_url.contents[0].replace("https://www", "http://staging")
    , excel_sheet_row
    )
    excel_sheet_row += 1
  workbook.close()
        
def run_seo_checks_for_end_url(end_url
, excel_sheet_row
):
    try:
        end_url_content = scrap_url(end_url)
        if DEBUG:
            pp.pprint({"End URL Content": end_url_content})
        head_content = end_url_content.contents[1].contents[0]
        body_content = end_url_content.contents[1].contents[2]
        # run_h1_check(end_url, body_content)
        run_meta_check(end_url, head_content
        , excel_sheet_row
        )
        # run_meta_description_check(end_url, head_content)
        run_url_format_checks(end_url)
    except Exception as e:
        pp.pprint({"EXCEPTION_OCCURED": end_url, "EXCEPTION": str(e)})
"""
********************************************************************************
H1 CHECKS
********************************************************************************
"""
def run_h1_check(end_url, content):
    h1_tag_actual_text = get_actual_h1_tag(end_url, content)
    if h1_tag_actual_text is None:
        pass
    else:
        h1_tag_expected_text = get_expected_h1_tag_text(end_url)
        if str.lower(str(h1_tag_actual_text)) != str.lower(str(h1_tag_expected_text)):
            pp.pprint({ERROR_STRINGS["H1_TAG_MISMATCH"]: end_url, "ACTUAL_H1_TAG_TEXT": h1_tag_actual_text,
                       "EXPECTED_H1_TAG_TEXT": h1_tag_expected_text})
        else:
            pass
def get_expected_h1_tag_text(end_url):
    location = end_url.split('/')[4].split('+')[2]
    h1_tag = "Study in " + location + " - Courses, Fees & Scope"
    return h1_tag.lower()
def get_actual_h1_tag(end_url, content):
    h1_tags_data = content.find_all('h1')
    if len(h1_tags_data) > 1:
        pp.pprint({ERROR_STRINGS["MORE_THAN_ONE_H1_TAG"]: end_url})
        return None
    elif len(h1_tags_data) == 0 or len(h1_tags_data[0].contents) == 0:
        pp.pprint({ERROR_STRINGS["ZERO_H1_TAGS"]: end_url})
        return None
    else:
        h1_tag_text = h1_tags_data[0].contents[0]
        return h1_tag_text.lower()
"""
********************************************************************************
META CHECKS
********************************************************************************
"""
def run_meta_check(end_url, content
, excel_sheet_row
):
    print(excel_sheet_row, 'excel sheet row inside meta check')
    meta_tag_actual_text = get_actual_meta_tag(end_url, content)
    if meta_tag_actual_text is None:
        pass
    else:
        meta_tag_expected_text = get_expected_meta_tag_text(end_url)
        if re.search(meta_tag_expected_text,meta_tag_actual_text) is None:
            print(":->", ERROR_STRINGS["META_TAG_TITLE_MISMATCH"], end_url)
            worksheet.write(excel_sheet_row, 0, end_url)
            worksheet.write(excel_sheet_row, 1, meta_tag_actual_text)
            worksheet.write(excel_sheet_row, 2, meta_tag_expected_text)
            print(
                "ACTUAL_META_TAG_TITLE_TEXT :->", meta_tag_actual_text,
                '\n'
                "EXPECTED_META_TAG_TITLE_TEXT :->", meta_tag_expected_text)
            print("\n")
        else:
            pass
def get_actual_meta_tag(end_url, content):
    meta_tags_data = content.find_all('title')
    if len(meta_tags_data) > 1:
        pp.pprint({ERROR_STRINGS["MORE_THAN_ONE_META_TAG_TITLE"]: end_url})
        print("\n")
        return None
    elif len(meta_tags_data) == 0 or len(meta_tags_data[0].contents) == 0:
        pp.pprint({ERROR_STRINGS["ZERO_META_TAGS_TITLE"]: end_url})
        print("\n")
        return None
    else:
        meta_tag_text = meta_tags_data[0].contents[0]
        return meta_tag_text.lower()
def get_expected_meta_tag_text(end_url):
    location = end_url.split('/')[4].split('+')[2]
    meta_title = "^[0-9]+" + " colleges in " + location + " offering " + "[0-9]+" + " courses$"
    return meta_title.lower()
"""
********************************************************************************
META DESCRIPTION CHECKS
********************************************************************************
"""
def run_meta_description_check(end_url, content):
    meta_tag_description_actual_text = get_actual_meta__description_tag(end_url, content)
    if meta_tag_description_actual_text is None:
        pass
    else:
        meta_tag_description_expected_text = get_expected_meta_tag_description_text(end_url)
        if re.search(meta_tag_description_expected_text,meta_tag_description_actual_text) is None:
            pp.pprint({ERROR_STRINGS["META_TAG_DESCRIPTION_MISMATCH"]: end_url,
                       "ACTUAL_META_TAG_DESCRIPTION_TEXT": meta_tag_description_actual_text,
                       "EXPECTED_META_TAG_DESCRIPTION_TEXT": meta_tag_description_expected_text})
        else:
            pass
def get_actual_meta__description_tag(end_url, content):
    meta_tags_data = content.find_all('meta')
    meta_description_tags = [x for x in meta_tags_data if 'name' in x.attrs and x.attrs['name'] == "description"]
    if len(meta_description_tags) > 1:
        pp.pprint({ERROR_STRINGS["MORE_THAN_ONE_META_TAG_DESCRIPTION"]: end_url})
        return None
    elif len(meta_description_tags) == 0 or len(meta_description_tags[0].contents) == 0:
        pp.pprint({ERROR_STRINGS["ZERO_META_TAGS_DESCRIPTION"]: end_url})
        return None
    else:
        meta_tag_text = meta_description_tags[0].attrs['content']
        meta_tag_text = meta_tag_text.replace(' ', '')
        return meta_tag_text.lower()
def get_expected_meta_tag_description_text(end_url):
    location = end_url.split('/')[4].split('+')[2]
    meta_description = "^Study in " + location + "-" + "[0-9+]" + " Colleges in " + location + " Countries Offering " + "[0-9]+" + " Courses. Get Complete Details About " + location + " on AdmitKard$"
    meta_description = meta_description.replace(' ', '')
    return meta_description.lower()
"""
********************************************************************************
URL CHECKS
********************************************************************************
"""
def run_url_format_checks(level_1_url_list):
    end_of_url = level_1_url_list.split("com")[1]
    check_end_url = re.search("^[A-Za-z0-9.\-_+\/ ]*$", end_of_url)
    if check_end_url is None:
        print(end_of_url, "URL IS BROKEN", level_1_url_list)
"""
********************************************************************************
END
********************************************************************************
"""
level_0_url_list = get_sitemap_content()
target_sitemap_url = extract_target_sitemap_url(level_0_url_list)
target_sitemap_url_content = get_target_sitemap_content(target_sitemap_url)
end_urls = extract_target_sitemap_url_list(target_sitemap_url_content)
run_seo_checks_for_end_urls(end_urls)

