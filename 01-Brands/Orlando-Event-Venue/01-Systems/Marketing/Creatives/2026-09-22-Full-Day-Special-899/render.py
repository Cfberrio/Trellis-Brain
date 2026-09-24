from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

# v3 VARIANT C — "ticket stamp": no gradients; one compact ink card holds the price block.
K=2; CW,CH=1080*K,1350*K
ACCENT=(2,132,199); INK=(11,15,25); WHITE=(255,255,255)
HERO=('/System/Library/Fonts/HelveticaNeue.ttc',9)          # Condensed Black
LBL=('/System/Library/Fonts/Avenir Next.ttc',8)             # Heavy
ARIAL='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def F(spec,size):
    p,i=spec if isinstance(spec,tuple) else (spec,0)
    return ImageFont.truetype(p, round(size*K), index=i)

# ---------- background (outpaint + hi-res overlay, original screen kept) — UNCHANGED from v2 ----------
bg = Image.open('outpaint.png').convert('RGB').resize((CW,CH), Image.LANCZOS)
crop = Image.open('venue-crop.png').convert('RGB')
sx = CW/2204
ov = crop.resize((CW, round(1536*sx)), Image.LANCZOS)
oy = round(568*CH/2304)
a = np.full((ov.height, ov.width), 255, np.uint8); fe=60
ramp=np.linspace(0,255,fe).astype(np.uint8); a[:fe,:]=ramp[:,None]; a[-fe:,:]=ramp[::-1][:,None]
ov.putalpha(Image.fromarray(a)); bg.paste(ov,(0,oy),ov)
img=bg.convert('RGBA')

# ---------- NO legibility gradients in v3 (client feedback) ----------

# ---------- text helpers ----------
def tw(text,font,tr): return sum(font.getlength(c) for c in text)+tr*K*(len(text)-1)
def draw_tracked(d,x,y,text,font,fill,tr,stroke=0,stroke_fill=None):
    for c in text:
        if stroke:
            d.text((x,y),c,font=font,fill=fill,stroke_width=round(stroke*K),stroke_fill=stroke_fill)
        else:
            d.text((x,y),c,font=font,fill=fill)
        x+=font.getlength(c)+tr*K
layer=Image.new('RGBA',(CW,CH),(0,0,0,0)); D=ImageDraw.Draw(layer)
shadow=Image.new('RGBA',(CW,CH),(0,0,0,0)); SD=ImageDraw.Draw(shadow)
def cap(font):
    bb=font.getbbox('H'); return bb[1], bb[3]-bb[1]
def centered_text(y,text,font,tr,fill=WHITE,stroke=2.5,shadow_on=True):
    """white type, ink stroke + soft ink shadow; y = top of cap height. returns cap height"""
    w=tw(text,font,tr); x=(CW-w)/2; top,th=cap(font)
    if shadow_on: draw_tracked(SD,x,y-top+4*K,text,font,INK+(235,),tr,stroke=stroke+1.5,stroke_fill=INK+(235,))
    draw_tracked(D,x,y-top,text,font,fill,tr,stroke=stroke,stroke_fill=INK+(255,))
    return th

# ---------- top block ----------
lock=Image.open('oev-lockup-stacked-white.png').convert('RGBA')
lw=118*K; lock=lock.resize((lw, round(lock.height*lw/lock.width)), Image.LANCZOS)
y=50*K; layer.paste(lock,((CW-lw)//2,y),lock); y+=lock.height+26*K
y+=centered_text(y,"EVENT VENUE",F(LBL,27),7)+34*K

# ---------- price card ("ticket stamp") ----------
f1=F(LBL,24);  t1="FULL DAY SPECIAL"; tr1=5
fh=F(HERO,148); th_="$899";          trh=-3
f3=F(LBL,24);  t3="24-HOUR ACCESS";  tr3=5
padx=34*K; pad_top=26*K; gap1=10*K; gap2=16*K; bar_pady=15*K
R=18*K; BORDER=round(4*K)
w1=tw(t1,f1,tr1); wh=tw(th_,fh,trh); w3=tw(t3,f3,tr3)
top1,h1=cap(f1); hbb=fh.getbbox(th_); hh=hbb[3]-hbb[1]; top3,h3=cap(f3)
W=max(w1,wh,w3)+2*padx
barH=h3+2*bar_pady
H=pad_top+h1+gap1+hh+gap2+barH
x0=(CW-W)/2; y0=y
# card: ink @ ~92%, rounded 18
D.rounded_rectangle([x0,y0,x0+W,y0+H],radius=R,fill=INK+(235,))
# accent bar across the bottom (rounded bottom corners, squared top edge)
by=y0+H-barH
D.rounded_rectangle([x0,by,x0+W,y0+H],radius=R,fill=ACCENT+(255,))
D.rectangle([x0,by,x0+W,by+R],fill=ACCENT+(255,))
# thin accent border
D.rounded_rectangle([x0,y0,x0+W,y0+H],radius=R,outline=ACCENT+(255,),width=BORDER)
# row 1: FULL DAY SPECIAL
cy=y0+pad_top
draw_tracked(D,(CW-w1)/2,cy-top1,t1,f1,WHITE,tr1)
cy+=h1+gap1
# row 2: $899 (biggest thing, but contained)
draw_tracked(D,(CW-wh)/2,cy-hbb[1],th_,fh,WHITE,trh)
cy+=hh+gap2
# row 3: 24-HOUR ACCESS on the accent bar
draw_tracked(D,(CW-w3)/2,by+bar_pady-top3,t3,f3,WHITE,tr3)
y=y0+H
print('card', x0/K, y0/K, W/K, H/K, '| $899 cap px @1x =', hh/K)

# BALDWIN PARK AREA: outlined pill under the card (no floating type over the strips)
y+=16*K
fbp=F(LBL,19); tbp="BALDWIN PARK AREA"; trbp=4.5
wbp=tw(tbp,fbp,trbp); tbp_top,tbp_h=cap(fbp); PH=tbp_h+2*12*K; PW=wbp+2*28*K; px=(CW-PW)/2
D.rounded_rectangle([px,y,px+PW,y+PH],radius=PH/2,fill=INK+(215,),outline=ACCENT+(255,),width=round(3*K))
draw_tracked(D,(CW-wbp)/2,y+12*K-tbp_top,tbp,fbp,WHITE,trbp)
y+=PH
print('top block ends (base)',y/K)

# ---------- bottom block: bullets ("the menu") ----------
fb=F(LBL,24); trb=2; lh=46*K; y=965*K
btop,bth=cap(fb)
for line in ["UP TO 90 GUESTS","NO CATERING RESTRICTIONS","INCLUDED: CHAIRS, TABLES, PREP KITCHEN, PARKING"]:
    w=tw(line,fb,trb); r=8*K; gap=16*K
    x=(CW-(w+2*r+gap))/2
    cyc=y+bth/2
    # marker: hollow accent ring with a thin ink outline outside it (hole stays open)
    D.ellipse([x-r-1.5*K,cyc-r-1.5*K,x+r+1.5*K,cyc+r+1.5*K],outline=INK+(255,),width=round(1.5*K))
    D.ellipse([x-r,cyc-r,x+r,cyc+r],outline=ACCENT+(255,),width=round(3*K))
    draw_tracked(D,x+2*r+gap,y-btop,line,fb,WHITE,trb,stroke=1.6,stroke_fill=INK+(255,))
    y+=lh
print('bullets end (base)',(y-lh+bth)/K)

# ---------- CTA pill ----------
cta=F(LBL,24)
txt="CHECK IF YOUR DATE IS OPEN"
ar=F(ARIAL,26); arw=ar.getlength("↓"); gap=16*K
w=tw(txt,cta,2)+gap+arw; bb=cta.getbbox('H'); th=bb[3]-bb[1]; H=th+44*K; W=w+88*K; x=(CW-W)/2
y=CH-100*K-H
# soft ink shadow under the pill so it lifts off the pale floor
SD.rounded_rectangle([x,y+6*K,x+W,y+H+6*K],radius=40*K,fill=INK+(160,))
D.rounded_rectangle([x,y,x+W,y+H],radius=40*K,fill=ACCENT+(255,))
draw_tracked(D,x+44*K,y+22*K-bb[1],txt,cta,WHITE,2)
ab=ar.getbbox("↓"); D.text((x+44*K+tw(txt,cta,2)+gap, y+22*K+th/2-(ab[1]+ab[3])/2),"↓",font=ar,fill=WHITE)
print('CTA top/bottom (base)',y/K,(y+H)/K,'bottom margin',(CH-y-H)/K)

shadow=shadow.filter(ImageFilter.GaussianBlur(4*K))
out=Image.alpha_composite(img,shadow); out=Image.alpha_composite(out,layer).convert('RGB')
out.save('blue-2160x2700.png'); out.resize((1080,1350),Image.LANCZOS).save('blue-1080x1350.png'); out.resize((720,900),Image.LANCZOS).save('blue-preview.png')
print('ok')
