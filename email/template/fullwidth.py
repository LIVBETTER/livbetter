"""LIVBETTER full-width email builder. Every band's colour runs edge to edge; content stays in a 600px column."""
MOSS="#172507"; PAPER="#ECE9E2"; LIME="#DAF24B"
SANS="'Instrument Sans',Helvetica,Arial,sans-serif"
def band(bg,inner,pad="0"):
    return (f'<tr><td bgcolor="{bg}" align="center" style="background-color:{bg};padding:{pad};">'
            f'<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;"><tr><td style="font-size:0;line-height:0;">{inner}</td></tr></table></td></tr>\n')
def img(U,f,alt,link=None):
    i=f'<img src="{U}{f}" width="600" alt="{alt}" style="display:block;width:100%;max-width:600px;height:auto;border:0;outline:none;text-decoration:none;">'
    return f'<a href="{link}" target="_blank" style="text-decoration:none;">{i}</a>' if link else i
def stripes_top():
    rows=[(LIME,5),(MOSS,2),(LIME,1),(MOSS,2),(LIME,1),(MOSS,3)]
    return ''.join(f'<tr><td bgcolor="{c}" height="{h}" style="background-color:{c};height:{h}px;font-size:0;line-height:0;">&nbsp;</td></tr>\n' for c,h in rows)
def stripes_bottom():
    rows=[(PAPER,3),(LIME,1),(PAPER,2),(MOSS,1),(PAPER,1),(LIME,6)]
    return ''.join(f'<tr><td bgcolor="{c}" height="{h}" style="background-color:{c};height:{h}px;font-size:0;line-height:0;">&nbsp;</td></tr>\n' for c,h in rows)
def tear(U,f,fallback):
    url=U+f
    return (f'<tr><td background="{url}" bgcolor="{fallback}" height="26" style="background-color:{fallback};background-image:url(\'{url}\');background-repeat:repeat-x;background-position:center top;height:26px;font-size:0;line-height:0;">&nbsp;</td></tr>\n')
def text(bg,html,style):
    return f'<tr><td bgcolor="{bg}" align="center" style="background-color:{bg};"><table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;"><tr><td align="center" style="{style}">{html}</td></tr></table></td></tr>\n'
def button(bg,label,link,pad):
    b=(f'<table role="presentation" class="btn" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto;"><tr><td align="center" bgcolor="{LIME}" style="border-radius:999px;mso-padding-alt:14px 34px;">'
       f'<a href="{link}" target="_blank" style="display:inline-block;padding:16px 34px;font-family:{SANS};font-size:13px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:#152305;text-decoration:none;border-radius:999px;">{label}</a></td></tr></table>')
    return text(bg,b,f"padding:{pad};")
def page(title,preheader,rows,first_bg=MOSS):
    return f'''<!DOCTYPE html>
<html lang="en-GB"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="x-apple-disable-message-reformatting">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600&family=Bodoni+Moda:ital,opsz@1,6..96&display=swap" rel="stylesheet">
<style>body{{margin:0;padding:0;background:{PAPER};}} a{{color:inherit;}} @media (max-width:620px){{.wrap{{width:100%!important;}} .btn a{{padding:14px 24px!important;font-size:12px!important;letter-spacing:2px!important;}}}}</style>
</head>
<body style="margin:0;padding:0;background:{PAPER};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{preheader}&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;">
{rows}</table>
</body></html>
'''
