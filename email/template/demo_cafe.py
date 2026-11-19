from fullwidth import *
U="https://raw.githubusercontent.com/LIVBETTER/livbetter/3daa96a97bf0c5f9fedfaf3e9156b853824f256a/email/2026-11-19-cafe-morning/fullwidth/"
MENU="https://www.joinlivbetter.com/#cafe"; IV="https://www.joinlivbetter.com/medical#iv"
r=stripes_top()
r+=band(MOSS,img(U,"1_masthead.jpg","Half price drinks tomorrow",MENU))
r+=tear(U,"tear_mp.png",PAPER)
r+=text(PAPER,"Hello {{contact.first_name}},",f"padding:30px 30px 0;font-family:{SANS};font-size:11px;line-height:16px;letter-spacing:4px;text-transform:uppercase;color:#5A5E4E;")
r+=band(PAPER,img(U,"2_cafe.jpg","Come and celebrate"))
r+=button(PAPER,"See the café menu",MENU,"10px 20px 46px")
r+=tear(U,"tear_pm.png",MOSS)
r+=band(MOSS,img(U,"3_bodybrilliant.jpg","Body Brilliant in the house tomorrow"))
r+=button(MOSS,"Find out about IV therapy",IV,"0 20px 44px")
r+=tear(U,"tear_mp.png",PAPER)
r+=band(PAPER,img(U,"5_signoff.jpg","See you tomorrow"))
r+=text(PAPER,'No longer want these emails? <a href="{{email.unsubscribe_link}}" target="_blank" style="color:#1B1F14;text-decoration:underline;">Unsubscribe</a>',f"padding:0 30px 26px;font-family:{SANS};font-size:12px;line-height:20px;color:#5A5E4E;")
r+=stripes_bottom()
open("demo_cafe.html","w").write(page("Full-width demo","demo",r))
