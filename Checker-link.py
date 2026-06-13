import tkinter as tk
import random
import time
import socket
import datetime
from urllib.parse import urlparse

lang = "EN"

LOGO = """ ██████╗ ██╗   ██╗██████╗  ██████╗ ██████╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗
██████╔╝██║   ██║██████╔╝██║  ███╗██████╔╝██████╔╝
██╔══██╗██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██╗
██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝"""

VALID_DOMAINS = [
    "iran.gov.ir",
    "president.ir",
    "majlis.ir",
    "mfa.gov.ir",
    "moi.ir",
    "irib.ir",
    "judiciary.ir",
    "amar.org.ir",
    "tax.gov.ir"
        "shaparak.ir",
    "khabaronline.ir",
    "police.ir",
    "ssaa.ir",
    "sahamedalat.ir",
    "medu.ir",
 "gov.ir",
    "iran.gov.ir",
    "president.ir",
    "majlis.ir",
    "mfa.gov.ir",
    "moi.ir",
    "irib.ir",
    "judiciary.ir",
    "amar.org.ir",
    "tax.gov.ir",
    "customs.gov.ir",
    "bankmarkazi.ir",
    "cbi.ir",
    "behdasht.gov.ir",
    "tamin.ir",
    "kar.ir",
    "rahvar120.ir",
    "rahvar.ir",
    "post.ir",
    "ito.gov.ir",
    "sabteahval.ir",
    "sabtemelk.ir",
    "mrud.ir",
    "rmto.ir",
    "nigc.ir",
    "nioc.ir",
    "mapna.ir",
    "bonyadmaskan.ir",
    "ghanoononline.ir",
    "farhang.gov.ir",
    "icts.ir",
    "shaparak.ir",
    "khabaronline.ir",
    "police.ir",
    "ssaa.ir",
    "sahamedalat.ir",
    "medu.ir",
    "gov.ir",
    "iran.gov.ir",
    "president.ir",
    "majlis.ir",
    "mfa.gov.ir",
    "moi.ir",
    "irib.ir",
    "judiciary.ir",
    "amar.org.ir",
    "tax.gov.ir",
    "customs.gov.ir",
    "bankmarkazi.ir",
    "cbi.ir",
    "behdasht.gov.ir",
    "tamin.ir",
    "kar.ir",
    "rahvar120.ir",
    "rahvar.ir",
    "post.ir",
    "ito.gov.ir",
    "sabteahval.ir",
    "sabtemelk.ir",
    "mrud.ir",
    "rmto.ir",
    "nigc.ir",
    "nioc.ir",
    "mapna.ir",
    "bonyadmaskan.ir",
    "ghanoononline.ir",
    "farhang.gov.ir",
    "icts.ir",
    "irna.ir",
    "isna.ir",
    "farsnews.ir",
    "mehrnews.com",
    "borna.news",
    "etemadonline.com",
    "mizanonline.ir",
    "yjc.ir",
    "tabnak.ir",
    "donest.ir",
    "snn.ir",
    "tasnimnews.com",
    "ilna.ir",
    "msc.ir",
    "msrt.ir",
    "wfa.ir",
    "cultural.gov.ir",
    "sport.gov.ir",
    "youth.gov.ir",
    "rbih.ir",
    "bim.ir",
    "imo.ir",
    "imo.gov.ir",
    "irscf.ir",
    "irscf.gov.ir",
    "ifc.ir",
    "nsr.ir",
    "nsrc.ir",
    "irtd.ir",
    "irtu.ir",
    "itc.ir",
    "itcf.ir",
    "idf.ir",
    "idpf.ir",
    "ids.ir",
    "idv.ir",
    "iec.ir",
    "iemc.ir",
    "ien.ir",
    "ies.ir",
    "ifc.ir",
    "ifid.ir",
    "ifip.ir",
    "ifir.ir",
    "ifs.ir",
    "ift.ir",
    "igmc.ir",
    "ignc.ir",
    "igs.ir",
    "igt.ir",
    "ihc.ir",
    "ihcs.ir",
    "iic.ir",
    "iicc.ir",
    "iid.ir",
    "iidc.ir",
    "iif.ir",
    "iig.ir",
    "iimc.ir",
    "iin.ir",
    "iis.ir",
    "iit.ir",
    "iiv.ir",
    "iwc.ir",
    "ixc.ir",
    "iyc.ir",
    "izc.ir",
    "jac.ir",
    "jamf.ir",
    "jarf.ir",
    "javanmardi.ir",
    "javaresh.ir",
    "javazb.ir",
    "jbc.ir",
    "jr",
    "jdmc.ir",
    "jds.ir",
    "jdt.ir",
    "jeb.ir",
    "jec.ir",
    "jed.ir",
    "jeh.ir",
    "jemc.ir",
    "jen.ir",
    "jer.ir",
    "jic.ir",
    "jid.ir",
    "j",
    "jii.ir",
    "jilc.ir",
    "jim.ir",
    "jin.ir",
    "jir.ir",
    "jis.ir",
    "jit.ir",
    "jiv.ir",
    "jizc.ir",
    "jkc.ir",
    "jlc.ir",
    "jldc.ir",
    "jlf.ir",
    "jlgc.ir",
    "jlh.ir",
    "jli.ir",
    "jlic.ir",
    "jlkc.ir",
    "jllc.ir",
    "jlm.cir",
    "jlp.ir",
    "jlq.ir",
    "jls.ir",
    "jlt.ir",
    "jlv.ir",
    "jlz.ir",
    "jmc.ir",
    "jmdc.ir",
    "jmf.ir",
    "jmgc.ir",
    "jmh.ir",
    "jmi.ir",
    "jmic.ir",
    "jmlc.ir",
    "jmn.ir",
    "jmp.ir",
    "jmq.ir",
    "jms.ir",
    "jmt.ir",
    "jmv.ir",
    "jmw.ir",
    "jmx.ir",
    "jmy.ir",
    "jmz.ir",
    "jnb.ir",
    "jnc.ir",
    "jndc.ir",
    "jnec.ir",
    "jnh.ir",
    "jni.ir",
    "jnj.ir",
    "jnk.ir",
    "jnlc.ir",
    "jnm.ir",
    "jnp.ir",
    "q.ir",
    "jns.ir",
    "jnt.ir",
    "jnv.ir",
    "jnw.ir",
    "jnx.ir",
    "jny.ir",
    "jnz.ir",
    "joc.ir",
    "jodc.ir",
    "joe.ir",
    "jofc.ir",
    "jogc.ir",
    "johc.ir",
    "joic.ir",
    "jokc.ir",
    "jol.cir",
    "jolc.ir",
    "jomc.ir",
    "jonc.ir",
    "jooc.ir",
    "jop.ir",
    "joq.ir",
    "jos.ir",
    "jot.ir",
    "jov.ir",
    "jow.ir",
    "jox.ir",
    "joy.ir",
    "joz.ir",
    "jpc.ir",
    "jpmc.ir",
    "jpn.ir",
    "jps.ir",
    "jpt.ir",
    "jpv.ir",
    "jpw.ir",
    "jpx.ir",
    "jpy.ir",
    "jpz.ir",
    "jqc.ir",
    "jqmc.ir",
    "jqn.ir",
    "jqp.ir",
    "jqq.ir",
    "jqs.ir",
    "jqt.ir",
    "jqv.ir",
    "jqw.ir",
    "jqx.ir",
    "jqc.ir",
    "jrc.ir",
    "jrdc.ir",
    "jre.ir",
    "jrfc.ir",
    "jrgc.ir",
    "jrhc.ir",
    "jric.ir",
    "jrkc.ir",
    "jrlnc.ir",
    "jrmc.ir",
    "jrn.ir",
    "jro.ir",
    "jrp.irjrv.ir",
    "jrw.ir",
    "jrx.ir",
    "jry.ir",
    "jrz.ir",
    "jsc.ir",
    "jsdc.ir",
    "jse.ir",
    "jsfc.ir",
    "jsgc.ir",
    "jshc.ir",
    "jsic.ir",
    "jskc.ir",
    "jslc.ir",
    "jsmc.ir",
    "jsnc.ir",
    "jsp.ir",
    "jsq.ir",
    "jsr.ir",
    "jst.ir",
    "jsv.ir",
    "jsw.ir",
    "jsx.ir",
    "jsy.ir",
    "jsz.ir",
    "jtc.ir",
    "jtn.ir",
    "jto.ir",
    "jtp.ir",
    "jtq.ir",
    "jts.ir",
    "jtv.ir",
    "jtw.ir",
    "jtx.ir",
    "jty.ir",
    "jtz.ir",
    "juc.ir",
    "judc.ir",
    "jufc.ir",
    "jugc.ir",
    "juhc.ir",
    "juic.ir",
    "jukc.ir",
    "julc.ir",
    "jumc.ir",
    "junc.ir",
    "juoc.ir",
    "jup.ir",
    "juq.ir",
    "jus.ir",
    "jut.ir",
    "juv.ir",
    "juw.ir",
    "jux.ir",
    "juy.ir",
    "juz.ir",
    "jvc.ir",
    "jvdc.ir",
    "jvfc.ir",
    "jvgc.ir",
    "jvhc.ir",
    "jvic.ir",
    "jvkc.ir",
    "jvlc.ir",
    "jvmc.ir",
    "jvnc.ir",
    "jvoc.ir",
    "jvp.ir",
    "jvqc.ir",
    "jvqp.ir",
    "jvqq.ir",
    "jvs.ir",
    "jvt.ir",
    "jvv.ir",
    "jvw.ir",
    "jvx.ir",
    "jvy.ir",
    "jvz.ir",
    "jwc.ir",
    "jwdc.ir",
    "jwfc.ir",
]

TEXT = {
    "EN": {
        "title": LOGO,
        "scan": "▶ EXECUTE SCAN",
        "help": "HELP",
        "error": "[ERROR] ENTER LINK",
        "report": "========== BURGERR REPORT ==========",
        "target": "[TARGET]",
        "ip": "[IP ADDRESS]",
        "status": "[STATUS]",
        "risk": "[RISK]",
        "scanning": "[*] SCANNING TARGET..."
    },
    "FA": {
        "title": "ابزار چک کننده لینک",
        "scan": "▶ شروع اسکن",
        "help": "راهنما",
        "error": "[خطا] لینک را وارد کن",
        "report": "========== گزارش ==========",
        "target": "[دامنه]",
        "ip": "[آی‌پی]",
        "status": "[وضعیت]",
        "risk": "[ریسک]",
        "scanning": "[*] در حال اسکن..."
    }
}

HELP_TEXT = {
    "EN": [
        "=========== BURGERR TOOL GUIDE ===========",
        "",
        "ABOUT:",
        "BURGERR is a lightweight link analysis tool designed",
        "to quickly check if a domain belongs to trusted sources.",
        "",
        "HOW IT WORKS:",
        "- Extracts domain from input URL",
        "- Resolves IP address",
        "- Compares domain with a trusted whitelist",
        "",
        "WHITELIST SYSTEM:",
        "Only the following domains are considered SAFE:",
        "- iran.gov.ir",
        "- president.ir",
        "- majlis.ir",
        "- mfa.gov.ir",
        "- moi.ir",
        "- irib.ir",
        "- judiciary.ir",
        "- amar.org.ir",
        "- tax.gov.ir",
        "",
        "STATUS MEANING:",
        "SAFE     → Trusted domain",
        "WARNING  → Not in whitelist",
        "ERROR    → Invalid or unreachable",
        "",
        "FEATURES:",
        "- Domain extraction",
        "- IP detection",
        "- Real-time scan UI",
        "- Matrix animation interface",
        "",
        "LIMITATIONS:",
        "- No SSL verification",
        "- No deep phishing detection",
        "- Basic logic only",
        "",
        "CREATORS:",
        "Parsa Shahsavari",
        "Mohammad Taha Khalili",
        "",
        "=========================================="
    ],
    "FA": [
        "=========== راهنمای BURGERR ===========",
        "",
        "درباره ابزار:",
        "BURGERR یک ابزار ساده برای بررسی لینک است",
        "که مشخص می‌کند آیا دامنه معتبر است یا نه",
        "",
        "نحوه کار:",
        "- استخراج دامنه از لینک",
        "- گرفتن آی‌پی سرور",
        "- مقایسه با لیست دامنه‌های معتبر",
        "وضعیت‌ها:",
        "SAFE → دامنه معتبر",
        "WARNING → خارج از لیست",
        "ERROR → خطا در بررسی",
        "",
        "امکانات:",
        "- استخراج دامنه",
        "- نمایش آی‌پی",
        "- رابط گرافیکی پویا",
        "",
        "سازندگان:",
        "پارسا شهسواری",
        "محمد طاها خلیلی",
        "",
        "===================================="
    ]
}

def toggle_lang():
    global lang
    lang = "FA" if lang == "EN" else "EN"
    update_ui()

def update_ui():
    title_label.config(text=TEXT[lang]["title"])
    scan_btn.config(text=TEXT[lang]["scan"])
    help_btn.config(text=TEXT[lang]["help"])

def normalize(url):
    if "://" not in url:
        url = "http://" + url
    return url

def scan(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        ip = socket.gethostbyname(domain)

        for valid in VALID_DOMAINS:
            if domain == valid or domain.endswith("." + valid):
                return domain, ip, "SAFE", "#00ff9c"

        return domain, ip, "WARNING", "#ffcc00"

    except:
        return "UNKNOWN", "UNKNOWN", "ERROR", "red"

WIDTH, HEIGHT = 750, 620
FONT = 14
cols = WIDTH // FONT
drops = [random.randint(0, HEIGHT) for _ in range(cols)]

def matrix():
    canvas.delete("m")
    for i in range(cols):
        x = i * FONT
        y = drops[i]
        canvas.create_text(x, y, text=random.choice("01"),
                           fill="#0ea5e9",
                           font=("Courier", FONT),
                           tags="m")
        drops[i] += FONT
        if drops[i] > HEIGHT:
            drops[i] = 0
    root.after(30, matrix)

r, g, b = 255, 0, 0
mode = 0

def rgb():
    global r, g, b, mode
    if mode == 0:
        g += 5
        if g >= 255: mode = 1
    elif mode == 1:
        r -= 5
        if r <= 0: mode = 2
    elif mode == 2:
        b += 5
        if b >= 255: mode = 3
    elif mode == 3:
        g -= 5
        if g <= 0: mode = 4
    elif mode == 4:
        r += 5
        if r >= 255: mode = 5
    elif mode == 5:
        b -= 5
        if b <= 0: mode = 0

    title_label.config(fg=f"#{r:02x}{g:02x}{b:02x}")
    root.after(50, rgb)

def write(lines, color="#38bdf8"):
    result.config(state="normal")
    result.delete("1.0", "end")

    for line in lines:
        for c in line + "\n":
            result.insert("end", c)
            root.update()
            time.sleep(0.002)

    result.config(fg=color)
    result.config(state="disabled")

def run():
    url = entry.get()
    if not url:
        write([TEXT[lang]["error"]], "red")
        return

    url = normalize(url)

    write([TEXT[lang]["scanning"]])

    domain, ip, status, color = scan(url)

    out = [
        "",
        TEXT[lang]["report"],
        f"{TEXT[lang]['target']} {domain}",
        f"{TEXT[lang]['ip']} {ip}",
        f"{TEXT[lang]['status']} {status}",
        f"{TEXT[lang]['risk']} {'LOW' if status=='SAFE' else 'MEDIUM'}"
    ]

    write(out, color)

def show_help():
    write(HELP_TEXT[lang])

root = tk.Tk()
root.title("BURGERR")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="black")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="#020617", highlightthickness=0)
canvas.place(x=0, y=0)

matrix()

frame = tk.Frame(root, bg="#020617")
frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(frame,
                       text=TEXT[lang]["title"],
                       font=("Courier", 10 if lang=="EN" else 18, "bold"),
                       bg="#020617",
                       justify="center")
title_label.pack(pady=10)

rgb()

entry = tk.Entry(frame, width=50,
                 bg="#0f172a",
                 fg="#38bdf8")
entry.pack(pady=10)

scan_btn = tk.Button(frame, text=TEXT[lang]["scan"],
                     command=run,
                     bg="#1d4ed8",
                     fg="white")
scan_btn.pack(pady=5)

help_btn = tk.Button(frame, text=TEXT[lang]["help"],
                     command=show_help,
                     bg="#334155",
                     fg="white")
help_btn.pack(pady=5)

result = tk.Text(frame, height=12, width=65,
                 bg="black", fg="#38bdf8")
result.pack(pady=10)
result.config(state="disabled")

tk.Button(root, text="EN/FA",
          command=toggle_lang,
          bg="#1e293b", fg="white").place(relx=0.95, rely=0.02)

tk.Label(root,
         text="Parsa Shahsavari & Mohammad Taha Khalili",
         fg="#38bdf8",
         bg="#020617").place(relx=0.99, rely=0.98, anchor="se")

root.mainloop()