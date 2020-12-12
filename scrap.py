# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:36:20 2020

@author: Admx
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:30:55 2020

@author: Admx
"""
#import libraries (Beautiful soup and the requests for making http calls)
import bs4
from bs4 import BeautifulSoup
import requests


url = 'https://ca.indeed.com/viewjob?cmp=A%26W-Canada&t=Team+Member&jk=f469dc5d556b4b4f&sjdu=vQIlM60yK_PwYat7ToXhk9gAEAskA0z4fGPuCSv8dddLCm3-rV5LvTHF7ypZWB0kAgnSYdYcQ8pBLYc8QqlCCA&tk=1epc3vdpmt4m6800&adid=361880756&ad=-6NYlbfkN0AzmWoxRupQlGOtc1l3nEtTJh_wEe4g12DME3BDzhYzyytuPFtxoqws5pS8zPh2QBIIf9tMiEFhDCa47tJubsBUg_8dUa6DazDTXTx02ZOFdsWhcR8VPd9QPlyg-U-DrBF0iq0PJjecz-YAvmSCi3nOTpcYMQLFycqYXs9KgtS7pQ058x9_TlHDyFSCpEJaMAWvFyM1hTgRPqwoc27Aoh5hezbTq2Gpnx0uNreeGtxAIT4108dV3L7FdTw1_Kon4ww3IChiLC2AgmYwmieeKIEBpLK0ZJaCCewK0LRO1Fv98-kr_s5VLnGmOJupECCY5ng_h6Tjfahr5Q%3D%3D&pub=4a1b367933fd867b19b072952f68dceb&vjs=3';

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

content_wrap = soup.find(id='viewJobSSRRoot')

title_wrap = content_wrap.find_all()


jobsearch-JobInfoHeader-title


jobsearch-JobInfoHeader-title





viewJobSSRRoot






<div id="viewJobSSRRoot"><div class="jobsearch-JobComponent icl-u-xs-mt--sm jobsearch-JobComponent-bottomDivider"><div id="welcomeToIndeedCard"></div><div class="jobsearch-DesktopStickyContainerTrigger"></div><div class="jobsearch-DesktopStickyContainer"><div><div class="jobsearch-JobInfoHeader-title-container "><h1 class="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title">Team Member</h1></div><div class="jobsearch-CompanyInfoWithoutHeaderImage jobsearch-CompanyInfoWithReview"><div class=""><div class="icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle"><div class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating"><div class="icl-u-lg-mr--sm icl-u-xs-mr--xs"><a href="https://ca.indeed.com/cmp/A&amp;W-Restaurants?campaignid=mobvjcmp&amp;from=mobviewjob&amp;tk=1epc3vup13klr000&amp;fromjk=f469dc5d556b4b4f" target="_blank">A&amp;W Canada</a></div><div class="icl-u-lg-block icl-u-lg-mr--sm icl-u-xs-hide"><div class="icl-Ratings icl-Ratings--sm icl-Ratings--gold" itemscope="" itemtype="http://schema.org/AggregateRating"><meta itemprop="ratingValue" content="3.6"><meta itemprop="ratingCount" content="3119"><div class="icl-Ratings-starsCountWrapper" role="img" aria-label="3.6 out of 5 from 3,119 employee ratings"><div class="icl-Ratings-starsWrapper"><div class="icl-Ratings-starsUnfilled"><div class="icl-Ratings-starsFilled" style="width: 42.6px;"></div></div></div><div class="icl-Ratings-count" aria-hidden="true">3,119 reviews</div></div></div></div><div class="icl-u-lg-mr--sm icl-u-xs-mr--xs" aria-hidden="true">-</div><div>Ottawa, ON</div></div></div></div></div></div><div class="jobsearch-JobMetadataHeader-item "><span class="icl-u-xs-mr--xs">$14.25 an hour</span><span class="jobsearch-JobMetadataHeader-item  icl-u-xs-mt--xs"> -  Full-time, Part-time, Permanent</span></div><div class="jobsearch-CompanyReview icl-u-lg-hide"><a class="icl-NavigableContainer-linkWrapper" href="https://ca.indeed.com/cmp/A&amp;W-Restaurants/reviews?campaignid=mobvjcmp&amp;cmpratingc=mobviewjob&amp;from=mobviewjob&amp;tk=1epc3vup13klr000&amp;fromjk=f469dc5d556b4b4f&amp;jt=Team+Member"><div class="icl-NavigableContainer icl-NavigableContainer--hasBorderBottom icl-NavigableContainer--hasBorderTop" role="button" tabindex="0"><div class="icl-NavigableContainer-innerContainer"><div class="jobsearch-CompanyReview--heading">A&amp;W Canada</div><div class="icl-Ratings icl-Ratings--md icl-Ratings--gold" itemscope="" itemtype="http://schema.org/AggregateRating"><meta itemprop="ratingValue" content="3.6"><meta itemprop="ratingCount" content="3119"><div class="icl-Ratings-starsCountWrapper" role="img" aria-label="3.6 out of 5 from 3,119 employee ratings"><div class="icl-Ratings-starsWrapper"><div class="icl-Ratings-starsUnfilled"><div class="icl-Ratings-starsFilled" style="width: 64.2px;"></div></div></div><div class="icl-Ratings-count" aria-hidden="true">3,119 reviews</div></div><div class="icl-Ratings-description" aria-hidden="true">Read what people are saying about working here.</div></div><div class="icl-NavigableContainer-iconContainer"><div class="icl-NavigableContainer-icon icl-NavigableContainer-icon--isLeftArrow"><svg role="none" class="icl-Icon icl-Icon--black icl-Icon--sm" aria-hidden="true" aria-label="chevron-left icon" focusable="false" viewBox="0 0 18 18"><g><path d="M11.56,5.56L10.5,4.5,6,9l4.5,4.5,1.06-1.06L8.12,9Z"></path></g></svg></div><div class="icl-NavigableContainer-icon icl-NavigableContainer-icon--isRightArrow"><svg role="none" class="icl-Icon icl-Icon--black icl-Icon--sm" aria-hidden="true" aria-label="chevron-right icon" focusable="false" viewBox="0 0 18 18"><g><path d="M7.5,4.5L6.44,5.56,9.88,9,6.44,12.44,7.5,13.5,12,9Z"></path></g></svg></div></div></div></div></a></div><div class="icl-u-lg-block icl-u-xs-hide"><div class="icl-u-xs-my--sm"></div></div><div id="indeedApplyExplanationContainer"></div><div id="jobsearch-ViewJobButtons-container" class="jobsearch-ViewJobButtons-container icl-Grid-col icl-u-xs-span12 icl-u-xs-textCenter icl-u-lg-textLeft jobsearch-DesktopStickyContainer-buttonscontainer"><div id="aboveViewjobButtons" class="mosaic mosaic-empty-zone"></div><div class="jobsearch-ButtonContainer-inlineBlock icl-u-lg-inlineBlock jobsearch-indeedApplyButton-bottomMargin"><div id="indeedApplyButtonContainer" class="jobsearch-IndeedApplyButton"><span class="indeed-apply-widget indeed-apply-button-container indeed-apply-status-not-applied" id="indeedApplyWidget" data-indeed-apply-apitoken="aa102235a5ccb18bd3668c0e14aa3ea7e2503cfac2a7a9bf3d6549899e125af4" data-indeed-apply-jobtitle="Team Member" data-indeed-apply-jobid="618f542a35bfc486fdf2" data-indeed-apply-joblocation="Ottawa, ON" data-indeed-apply-jobcompanyname="A&amp;W Canada" data-indeed-apply-joburl="https://ca.indeed.com/viewjob?jk=f469dc5d556b4b4f" data-indeed-apply-posturl="https://dradisindeedapply.sandbox.indeed.net/process-indeedapply" data-indeed-apply-coverletter="optional" data-indeed-apply-resume="required" data-indeed-apply-advnum="7723972011437284" data-indeed-apply-nobuttonui="true" data-indeed-apply-pingbackurl="https://gdc.indeed.com/conv/orgIndApp?co=CA&amp;vjtk=1epc3vup13klr000&amp;jk=f469dc5d556b4b4f&amp;mvj=0&amp;acct_key=dd2567fbf2ae4493&amp;tk=1epc3vdpmt4m6800&amp;trk.origin=jobsearch&amp;sj=1&amp;vjfrom=web&amp;advn=7723972011437284&amp;adid=361880756&amp;ad=-6NYlbfkN0AzmWoxRupQlGOtc1l3nEtTJh_wEe4g12DME3BDzhYzyytuPFtxoqws5pS8zPh2QBIIf9tMiEFhDCa47tJubsBUg_8dUa6DazDTXTx02ZOFdsWhcR8VPd9QPlyg-U-DrBF0iq0PJjecz-YAvmSCi3nOTpcYMQLFycqYXs9KgtS7pQ058x9_TlHDyFSCpEJaMAWvFyM1hTgRPqwoc27Aoh5hezbTq2Gpnx0uNreeGtxAIT4108dV3L7FdTw1_Kon4ww3IChiLC2AgmYwmieeKIEBpLK0ZJaCCewK0LRO1Fv98-kr_s5VLnGmOJupECCY5ng_h6Tjfahr5Q%3D%3D&amp;astse=73f39d8c664f852f&amp;assa=6769" data-indeed-apply-onappliedstatus="_updateIndeedApplyStatus" data-indeed-apply-onready="_onButtonReady" data-indeed-apply-jk="f469dc5d556b4b4f" data-indeed-apply-clickhandler="window.top.postMessage({eventType: 'click'}, '*')" data-indeed-apply-dismisshandler="window.top.postMessage({eventType: 'dismiss'}, '*')" data-indeed-apply-inpageapplyhandler="window.top.postMessage({eventType: 'inpageapply'}, '*')" data-indeed-apply-recentapplies="{&quot;all&quot;:-1,&quot;qualified&quot;:-1}" data-indeed-apply-continueurl="http://ca.indeed.com?sita=1&amp;from=postapply&amp;adid=361880756" data-indeed-apply-recentsearchquery="{&quot;what&quot;:&quot;A&amp;W CANADA&quot;,&quot;where&quot;:&quot;Ottawa, ON&quot;}"><div class="icl-u-lg-hide"><button class="icl-Button icl-Button--branded icl-Button--lg icl-Button--block" buttonsize="block" type="button"><div class="jobsearch-IndeedApplyButton-contentWrapper"><span>Apply Now</span></div></button></div><div class="jobsearch-IndeedApplyButton-buttonWrapper icl-u-lg-block icl-u-xs-hide"><button class="icl-Button icl-Button--branded icl-Button--lg icl-Button--md" buttonsize="md" type="button"><div class="jobsearch-IndeedApplyButton-contentWrapper"><span>Apply Now</span></div></button></div></span></div></div><div id="saveJobButtonContainer" class="icl-u-lg-inlineBlock"><div class=""><div><div><div class="icl-u-lg-hide"><button class="icl-Button icl-Button--secondary icl-Button--lg icl-Button--block" type="button"><span class="icl-ButtonIcon"><svg role="img" class="icl-Icon icl-Icon--inheritColor icl-Icon--sm" aria-label="save-icon" focusable="false" viewBox="0 0 18 18"><g><path d="M12.38,2.25A4.49,4.49,0,0,0,9,3.82,4.49,4.49,0,0,0,5.63,2.25,4.08,4.08,0,0,0,1.5,6.38c0,2.83,2.55,5.15,6.41,8.66L9,16l1.09-1C14,11.52,16.5,9.21,16.5,6.38A4.08,4.08,0,0,0,12.38,2.25ZM9.08,13.91L9,14l-0.08-.08C5.35,10.68,3,8.54,3,6.38A2.56,2.56,0,0,1,5.63,3.75,2.93,2.93,0,0,1,8.3,5.52H9.7a2.91,2.91,0,0,1,2.67-1.77A2.56,2.56,0,0,1,15,6.38C15,8.54,12.65,10.68,9.08,13.91Z"></path></g></svg></span>Save this job</button></div><div class="icl-u-lg-block icl-u-xs-hide"><button class="icl-Button icl-Button--secondary icl-Button--md icl-Button--block" type="button"><span class="icl-ButtonIcon"><svg role="img" class="icl-Icon icl-Icon--inheritColor icl-Icon--sm" aria-label="save-icon" focusable="false" viewBox="0 0 18 18"><g><path d="M12.38,2.25A4.49,4.49,0,0,0,9,3.82,4.49,4.49,0,0,0,5.63,2.25,4.08,4.08,0,0,0,1.5,6.38c0,2.83,2.55,5.15,6.41,8.66L9,16l1.09-1C14,11.52,16.5,9.21,16.5,6.38A4.08,4.08,0,0,0,12.38,2.25ZM9.08,13.91L9,14l-0.08-.08C5.35,10.68,3,8.54,3,6.38A2.56,2.56,0,0,1,5.63,3.75,2.93,2.93,0,0,1,8.3,5.52H9.7a2.91,2.91,0,0,1,2.67-1.77A2.56,2.56,0,0,1,15,6.38C15,8.54,12.65,10.68,9.08,13.91Z"></path></g></svg></span>Save this job</button></div></div></div></div></div><div id="saveJobFailureModal"></div><div id="belowViewjobButtons" class="mosaic mosaic-empty-zone"></div></div><div class="jobsearch-StickyContainerDivider"><div class="jobsearch-StickyContainerDivider-line"></div></div></div><span></span><div id="aboveExtractedJobDescription" class="mosaic mosaic-empty-zone"></div><div class="jobsearch-JobComponent-description icl-u-xs-mt--md"><div id="jobDescriptionText" class="jobsearch-jobDescriptionText"><p>Our newest A&amp;W restaurant is now hiring <b>full time and part time team members </b>to work in our downtown Ottawa location!</p><p>We are looking for candidates with flexible availabilities ranging and a willingness to learn.</p><p>If this sounds like you, then we want to meet you! Apply here to schedule an interview.</p><p>We are offering</p><ul><li>$14.25 + (depending on experience level)</li><li>Regular pay increases</li><li>Excellent training</li><li>Medical and dental benefits for full time employees</li><li>and much more!</li></ul><p>Job Types: Full-time, Part-time, Permanent</p><p>Salary: From $14.25 per hour</p><p>Schedule:</p><ul><li>8 hour shift</li></ul><p>COVID-19 considerations:<br>To keep our staff as safe as possible, we've installed clear plastic barriers, socially distanced dining room, and provided masks, gloves, and hand sanitizer.</p><p>Work remotely:</p><ul><li>No</li></ul></div><div id="belowFullJobDescription" class="mosaic mosaic-empty-zone"></div></div><div id="mapRoot" aria-hidden="true"></div><div id="welcomeToIndeedModal"></div><div id="successfullySignedInModal"></div><div id="thirdPartyApplyCreateAccountModal"></div><div class="jobsearch-JobTab-content"><div id="belowJobDescription" class="mosaic mosaic-empty-zone"></div><div class="jobsearch-JobMetadataFooter"><span>10 days ago</span><div class="mosaic mosaic-provider-reportcontent mosaic-provider-hydrated" id="mosaic-provider-reportcontent"><span class="mosaic-reportcontent-wrapper button"><div><button class="icl-Button icl-Button--secondary icl-Button--md mosaic-reportcontent-button desktop" type="button"><span class="mosaic-reportcontent-button-icon"></span>Report job</button></div><div class="mosaic-reportcontent-content"></div></span></div></div></div><div id="betweenJobDescriptionAndButtons" class="mosaic mosaic-empty-zone"></div><div class="mosaic mosaic-provider-assessments-intervention" id="mosaic-provider-assessments-intervention"></div><div class="icl-Grid icl-Grid--gutters"></div></div></div>








def getSearchPageResult(soup):
    results = []
    for div in soup.find_all(name='div', attrs={'class':'jobsearch-SerpJobCard'}):
        print(div)



url = 'https://ca.indeed.com/jobs?q=customer+service&l=Ottawa%2C+ON'

page = requests.get(url)
print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')


results = getSearchPageResult(soup)



def scrapSearchPage(html_content):
    '''
    Scrap search page to fetch job posting

    Returns
    -------
    None.

    '''
    
    