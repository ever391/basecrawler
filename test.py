# coding:utf8
import re

html = '&amp;'
from html.entities import entitydefs, name2codepoint


print(re.search('&(?P<entityName>[a-zA-Z]{2,10});', html).group("entityName"))

print(chr(name2codepoint['amp']))

decodedEntityName = re.sub('&(?P<entityName>[a-zA-Z]{2,10});',
                                   lambda matched: chr(name2codepoint[matched.group("entityName")]),
                                   html)
print(type(decodedEntityName))
decodedCodepointInt = re.sub('&#(?P<codePointInt>\d{2,5});',
                             lambda matched: chr(int(matched.group("codePointInt"))), decodedEntityName)
decodedCodepointHex = re.sub('&#x(?P<codePointHex>[a-fA-F\d]{2,5});',
                             lambda matched: chr(int(matched.group("codePointHex"), 16)),
                             decodedCodepointInt)

decodedHtml = decodedCodepointHex
decodedEncoding=''
if (decodedEncoding):
    decodedHtml = decodedHtml.encode(decodedEncoding, 'ignore')

print(decodedHtml)