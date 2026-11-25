from fullwidth import *
U="https://raw.githubusercontent.com/LIVBETTER/livbetter/ccc29799e91d70f07304f214ae59a8fe5e67a2c3/email/2026-11-24-members-week/"
GC="https://momence.com/gcc/43664"; MEM="https://www.joinlivbetter.com/#memberships"
r=stripes_top()
r+=band(MOSS,img(U,"1_masthead.jpg","Members' Week, 26 to 30 November. Our best offers of the year, through Black Friday. A £50 bonus on every £100 of gift cards, and a surprise in store on Friday.",GC))
r+=tear(U,"tear_mp.png",PAPER)
r+=text(PAPER,"Hello {{contact.first_name}},",f"padding:30px 30px 0;font-family:{SANS};font-size:11px;line-height:16px;letter-spacing:4px;text-transform:uppercase;color:#5A5E4E;")
r+=band(PAPER,img(U,"2_giftcards.jpg","No. 01, gift cards, 26 to 30 November: give one, get £50. For every £100 you spend, a £50 bonus card for you, up to £150 bonus on £300. Your bonus card is added after you buy. Gift cards are sent by email, or picked up or posted from the clinic.",GC))
r+=button(PAPER,"Buy a gift card",GC,"6px 20px 44px")
r+=tear(U,"tear_pm.png",MOSS)
r+=band(MOSS,img(U,"3_membership.jpg","No. 02, membership: start now, keep this price. Your price locked for 12 months, a guest HBOT Duo session for a friend, and your £99 trial pass taken off your first month.",MEM))
r+=button(MOSS,"Choose my membership",MEM,"0 20px 44px")
r+=tear(U,"tear_mp.png",PAPER)
r+=band(PAPER,img(U,"4_blackfriday.jpg","No. 03, Black Friday, 27 November: something's waiting. Come in on Friday. Visit the clinic or The LIV Café and there'll be a little something waiting for you at 56 London End. And on Thursday, three gift cards to win on our Instagram, @livbetter.uk."))
r+=band(PAPER,img(U,"5_signoff.jpg","See you this week. LIVBETTER, 56 London End, Beaconsfield HP9 2JH. Gift card bonus: for every £100 spent on LIVBETTER gift cards from 26 to 30 November 2026, get a £50 bonus card, up to £150 bonus per customer. The bonus card is added after purchase. Membership offer applies to new memberships started during Members' Week. Instagram giveaway terms are on the post. Offers cannot be used with any other offer or discount. Treatments are for over-18s only. T&Cs apply."))
r+=text(PAPER,'No longer want these emails? <a href="{{email.unsubscribe_link}}" target="_blank" style="color:#1B1F14;text-decoration:underline;">Unsubscribe</a>',f"padding:0 30px 26px;font-family:{SANS};font-size:12px;line-height:20px;color:#5A5E4E;")
r+=stripes_bottom()
open("members_week.html","w").write(page("Members' Week: a £50 bonus on every £100 of gift cards","Thursday to Monday: a £50 bonus card on every £100 of gift cards, your membership price locked, and a surprise in store on Black Friday.",r))
