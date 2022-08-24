
import  re

def Renamer_TG(name, subadd = True, hsub = False):
    orgname = name.replace(".AlphaDL", "").replace("(","").replace(")","").replace(" ",".").replace("AD","",1).replace(".AM]","",).replace(".LT]","",)
    orgname = orgname.replace(".-",".").replace("-.",".").replace("..",".")
    orgname = re.sub(r"(\.*\d{3,4}MB)","",orgname)
    orgname = re.sub(r"(\.*HQ)","",orgname)
    orgname = re.sub(r"\.*AAC\.*\d*\.*\d*","",orgname)
    orgname = orgname.replace("HEVC-", "").replace("H264-","").replace("x264-","").replace(".HEVC", "").replace(".H264","").replace(".x264","").replace("[","").replace(".MX]","").replace(".in","").replace(".ph","").replace(".li","").replace("HEVC", "").replace("H264","").replace("x264","").replace(".hevc","")
    orgname = orgname.replace("webdl","WEB-DL").replace("web-dl","WEB-DL").replace("webrip","WEBRip").replace("web","WEB").replace("bluray","BluRay").replace("hdtv","HDTV")
    orgname = orgname.replace("rmteam","RMT").replace("RMTeam","RMT")

    if re.findall(r"(\..{3,4})$", orgname):
        regex = re.search(r"(\..{3,4})$", orgname)
        orgname = orgname.replace(regex.group(1),".AlphaDL%s"%regex.group(1))

    if re.findall(r"[Ss]\d{1,3}.?[Ee]\d{1,3}",orgname):
        orgname = orgname.replace((re.search(r"([Ss]\d{1,3}.?[Ee]\d{1,3})", orgname)).group(1), (re.search(r"([Ss]\d{1,3}.?[Ee]\d{1,3})", orgname)).group(1).upper())

    if re.findall(r"[Ss]\d{1,3}.?[Ee]\d{1,3}(.*)\.\d{3,4}p", orgname):
        regex = re.search(r"[Ss]\d{1,3}.?[Ee]\d{1,3}(.*)\.\d{3,4}p", orgname)
        orgname = orgname.replace(regex.group(1),".Dual") if "dual"in regex.group(1).lower() else orgname.replace(regex.group(1),"")

    if subadd and not re.findall(r"softsub", orgname.lower()) and not hsub:
        if re.findall(r"\d{3,4}p(.*)\..{3,4}$", orgname):
            regex = re.search(r"\d{3,4}p(.*)\..{3,4}$", orgname)
            orgname = orgname.replace(regex.group(1),".SoftSub%s"%regex.group(1))
            
    if hsub:
        if re.findall(r"\d{3,4}p(.*)\..{3,4}$", orgname):
            regex = re.search(r"\d{3,4}p(.*)\..{3,4}$", orgname)
            orgname = orgname.replace(regex.group(1),".HardSub%s"%regex.group(1))

    if not subadd and re.findall(r"softsub", orgname.lower()):
        regex = re.search(r"([Ss][Oo][Ff][Tt][Ss][Uu][Bb])", orgname)
        orgname = orgname.replace(regex.group(1),"")

    if re.findall(r"[Ss]\d{1,3}.?[Ee]\d{1,3}.*\.\d{3,4}p",orgname):
        orgname = orgname.replace((re.search(r"(.*)\.[Ss]\d{1,3}.?[Ee]\d{1,3}",orgname)).group(1), (re.search(r"(.*)\.[Ss]\d{1,3}.?[Ee]\d{1,3}",orgname)).group(1).title())
        if len(orgname) > 64:
            parts = (re.search(r"(.*)\.[Ss]\d{1,3}.?[Ee]\d{1,3}",orgname)).group(1).split(".")
            parts.reverse()
            for part in parts:
                if not re.findall(r"\d{4}",part):
                    if len(orgname) > 64:
                        orgname = orgname.replace(part, part[0].upper())

    if not re.findall(r"[Ss]\d{1,3}.?[Ee]\d{1,3}",orgname):
        if re.findall(r"\.\d{3,4}p",orgname):
            orgname = orgname.replace((re.search(r"(.*)\.\d{3,4}p",orgname)).group(1), (re.search(r"(.*)\.\d{3,4}p",orgname)).group(1).title())
            if len(orgname) > 64:
                parts = (re.search(r"(.*)\.\d{3,4}p",orgname)).group(1).split(".")
                parts.reverse()
                for part in parts:
                    if not re.findall(r"\d{4}",part):
                        if len(orgname) > 64:
                            orgname = orgname.replace(part, part[0].upper())
    
    if len(orgname) > 64:
        orgname = orgname.replace("AlphaDL", "AD")

    orgname = orgname.replace(".-",".").replace("-.",".").replace("..",".")

    return orgname
