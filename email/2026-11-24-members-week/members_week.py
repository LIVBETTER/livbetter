from fullwidth import *
U="https://raw.githubusercontent.com/LIVBETTER/livbetter/03f1705458de8b0bce1319491b9f2a36fd4bf8af/email/2026-11-24-members-week/"
GC="https://momence.com/gcc/43664"; HBOT="https://www.joinlivbetter.com/#hbot"
r=stripes_top()
r+=band(MOSS,img(U,"1_masthead.jpg","Members' Week, 26 to 30 November. Our best offers of the year, through Black Friday. A £50 bonus on every £100 of gift cards, and a surprise in store on Friday.",GC))
r+=tear(U,"tear_mp.png",PAPER)
r+=text(PAPER,"Hello {{contact.first_name}},",f"padding:30px 30px 0;font-family:{SANS};font-size:11px;line-height:16px;letter-spacing:4px;text-transform:uppercase;color:#5A5E4E;")
r+=band(PAPER,img(U,"2_giftcards.jpg","No. 01, gift cards, 26 to 30 November: give one, get £50. For every £100 you spend, a £50 bonus card for you, up to £150 bonus on £300. Your bonus card is added after you buy. Gift cards are sent by email, or picked up or posted from the clinic. Bonus cards can be used from 1 December 2026. Up to £150 bonus per customer. T&Cs apply. Cannot be used with any other offer or discount.",GC))
r+=button(PAPER,"Buy a gift card",GC,"6px 20px 44px")
r+=tear(U,"tear_pm.png",MOSS)
r+=band(MOSS,img(U,"3_hbot.jpg","No. 02, hyperbaric oxygen, 26 to 30 November: more time in the chamber. HBOT Duo or Solo. Buy 5 sessions, get 1 free. Buy 10, get 3 free. Buy 20, get 5 free. Buy a pack between Thursday 26 and Monday 30 November and we add your free sessions after you buy. T&Cs apply. Cannot be used with any other offer or discount.",HBOT))
r+=button(MOSS,"Buy an HBOT pack",HBOT,"0 20px 44px")
r+=tear(U,"tear_mp.png",PAPER)
r+=band(PAPER,img(U,"4_blackfriday.jpg","No. 03, Black Friday, 27 November: something's waiting. Our best deal of the year, in store only. Come into 56 London End on Black Friday, Friday 27 November. We're keeping it a secret until then. And on Thursday, three gift cards to win on our Instagram, @livbetter.uk."))
r+=band(PAPER,img(U,"5_signoff.jpg","See you this week. LIVBETTER, 56 London End, Beaconsfield HP9 2JH. Gift card bonus: for every £100 spent on LIVBETTER gift cards from 26 to 30 November 2026, get a £50 bonus card, up to £150 bonus per customer. The bonus card is added after purchase and can be used from 1 December 2026. HBOT packs: buy 5, 10 or 20 HBOT sessions (Duo or Solo) between 26 and 30 November 2026 and get 1, 3 or 5 free sessions, added after purchase. Instagram giveaway terms are on the post. Offers cannot be used with any other offer or discount. Treatments are for over-18s only. T&Cs apply."))
r+=text(PAPER,'No longer want these emails? <a href="{{email.unsubscribe_link}}" target="_blank" style="color:#1B1F14;text-decoration:underline;">Unsubscribe</a>',f"padding:0 30px 26px;font-family:{SANS};font-size:12px;line-height:20px;color:#5A5E4E;")
r+=stripes_bottom()
open("members_week.html","w").write(page("Members' Week: £50 on every £100, and free HBOT sessions","Thursday to Monday: a £50 bonus on every £100 of gift cards, free sessions on HBOT packs, and our best deal of the year in store on Friday.",r))
