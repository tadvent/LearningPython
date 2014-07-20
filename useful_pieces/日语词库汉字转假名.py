#coding=gbk

import os,sys

def parser(linestr):
    pos1 = linestr.find('||')
    if (-1 == pos1):
        return None
    pos2 = linestr.find('||',pos1 + 2)
    if (-1 == pos2):
        return None
    kanji = (linestr[:pos1]).strip()
    secondpart = (linestr[pos1 + 2:pos2]).split(None,1)
    if (secondpart[0] != "假名"):
        return None
    if len(secondpart) < 2:
        return None
    pos3 = (secondpart[1]).find("解释")
    if -1 == pos3:
        return kanji, (secondpart[1]).strip(), ""
    else :
        return kanji, (secondpart[1])[:pos3].strip(), (secondpart[1])[pos3:].rstrip()

def ProcessFile(filepath):
    rootname, extpart = os.path.splitext(filepath)
    fromfile = open(filepath,"r",encoding="utf-8")
    tofile = open(rootname + "假名" + extpart, "w", encoding="utf-8")
    bNewLine = True
    sCurStr = ""
    for linestr in fromfile:
        if bNewLine:
            sCurStr = ""
            pos = linestr.find("||")
            if -1 == pos:
                continue
            sCurStr = linestr
            pos = linestr.find("||", pos + 2)
            if -1 == pos:
                bNewLine = False
                continue
        else :
            sCurStr += linestr
            pos = linestr.find("||")
            if -1 == pos:
                continue
            else :
                bNewLine = True

        rst = parser(sCurStr)
        if None == rst:
            continue
        (kanji, kana, tail) = rst
        if "" == kanji:
            continue
        if "" == tail:
            toline = kana + "||漢字 " + kanji + "||\n"
        else :
            toline = kana + "||漢字 " + kanji + "\n" + tail + "||\n"
        tofile.write(toline)

    fromfile.close()
    tofile.close()

if __name__ == "__main__":
    filepath = input("Input file path:")
    ProcessFile(filepath)

