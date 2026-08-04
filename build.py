# -*- coding: utf-8 -*-
"""Uzbuve index.html no src/ failiem. Palaid: python build.py (vajadzigs Python 3)."""
import io, re, os

BASE = os.path.dirname(os.path.abspath(__file__))

def rd(*p):
    return io.open(os.path.join(BASE, *p), encoding="utf-8").read()

core = rd("src", "site_core.html").replace("/*__FONTS__*/", rd("src", "fonts_embed.css"))

m_title = re.search(r"<title>(.*?)</title>", core, re.S)
title = m_title.group(1).strip() if m_title else "ArtefyCraft"
m_style = re.search(r"<style>(.*?)</style>", core, re.S)
style = m_style.group(1) if m_style else ""
body = core
if m_title:
    body = body.replace(m_title.group(0), "", 1)
if m_style:
    body = body.replace("<style>" + m_style.group(1) + "</style>", "", 1)
body = body.strip()

doc = rd("src", "page_wrapper.html").format(title=title, style=style, body=body)
out = os.path.join(BASE, "index.html")
with io.open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(doc)
print("OK:", out, len(doc), "chars")
