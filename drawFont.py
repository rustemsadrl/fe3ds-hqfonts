from PIL import Image, ImageDraw, ImageFont
import sys
import os
import numpy as np
import regex as re

multiplier = 4
fontJapanese = ImageFont.truetype(r'C:/Fonts/NotoSerifJP-SemiBold.otf', 52)
testNumber = ImageFont.truetype(r'C:/Fonts/NotoSerifJP-SemiBold.otf', 5)

textColor = (0,0,0,255)
#textColor = (255,255,0,127)
testBox = (255,0,0,127)
testBlue = (0,0,255,127)
testBoxBlue = (0,0,255,127)

img0 = Image.new('RGBA', (4096,4096), (0,0,0,0))
draw0 = ImageDraw.Draw(img0)
img1 = Image.new('RGBA', (4096,4096), (0,0,0,0))
draw1 = ImageDraw.Draw(img1)

with open(r'D:/code/feFonts/fontSystem.txt', 'r', encoding="utf-8-sig") as jpSystem:
	for line in jpSystem:
		fontCharacter = chr(int('0x'+line.split("\t")[0],16))
		whichTexture = line.split("\t")[1]
		x = int(line.split("\t")[2])*multiplier
		y = (int(line.split("\t")[3])-12+int(line.split("\t")[7]))*multiplier+1
		sizeX = int(line.split("\t")[4])*multiplier
		sizeY = (int(line.split("\t")[5])+1)*multiplier
		offset = fontJapanese.getoffset(fontCharacter)
		allX = x
		allY = y-12#16
		if (whichTexture == '0'):
			'''draw0.rectangle((x,y,x+sizeX,y), testBoxBlue)
			draw0.rectangle((x,y+4,x+sizeX,y+4), testBoxBlue)
			draw0.text((x,y-2+4), "4", font=testNumber, fill=textColor)
			draw0.rectangle((x,y+8,x+sizeX,y+8), testBoxBlue)
			draw0.rectangle((x,y+12,x+sizeX,y+12), testBoxBlue)
			draw0.rectangle((x,y+16,x+sizeX,y+16), testBoxBlue)
			draw0.text((x,y-2+16), "16", font=testNumber, fill=textColor)
			draw0.rectangle((x,y+20,x+sizeX,y+20), testBoxBlue)
			draw0.rectangle((x,y+24,x+sizeX,y+24), testBoxBlue)
			draw0.rectangle((x,y+28,x+sizeX,y+28), testBoxBlue)
			draw0.rectangle((x,y+32,x+sizeX,y+32), testBoxBlue)
			draw0.text((x,y-2+32), "32", font=testNumber, fill=textColor)
			draw0.rectangle((x,y+36,x+sizeX,y+36), testBoxBlue)
			draw0.rectangle((x,y+40,x+sizeX,y+40), testBoxBlue)
			draw0.rectangle((x,y+44,x+sizeX,y+44), testBoxBlue)
			draw0.rectangle((x,y+48,x+sizeX,y+48), testBoxBlue)
			draw0.rectangle((x,y+52,x+sizeX,y+52), testBoxBlue)
			draw0.rectangle((x,y+56,x+sizeX,y+56), testBoxBlue)
			draw0.rectangle((x,y,x+4,y+4), testBox)'''
			draw0.text((allX,allY), fontCharacter, font=fontJapanese, fill=textColor)#-16
		else:
			'''draw1.rectangle((x,y,x+sizeX,y), testBoxBlue)
			draw1.rectangle((x,y+4,x+sizeX,y+4), testBoxBlue)
			draw1.text((x,y-2+4), "4", font=testNumber, fill=textColor)
			draw1.rectangle((x,y+8,x+sizeX,y+8), testBoxBlue)
			draw1.rectangle((x,y+12,x+sizeX,y+12), testBoxBlue)
			draw1.rectangle((x,y+16,x+sizeX,y+16), testBoxBlue)
			draw1.text((x,y-2+16), "16", font=testNumber, fill=textColor)
			draw1.rectangle((x,y+20,x+sizeX,y+20), testBoxBlue)
			draw1.rectangle((x,y+24,x+sizeX,y+24), testBoxBlue)
			draw1.rectangle((x,y+28,x+sizeX,y+28), testBoxBlue)
			draw1.rectangle((x,y+32,x+sizeX,y+32), testBoxBlue)
			draw1.text((x,y-2+32), "32", font=testNumber, fill=textColor)
			draw1.rectangle((x,y+36,x+sizeX,y+36), testBoxBlue)
			draw1.rectangle((x,y+40,x+sizeX,y+40), testBoxBlue)
			draw1.rectangle((x,y+44,x+sizeX,y+44), testBoxBlue)
			draw1.rectangle((x,y+48,x+sizeX,y+48), testBoxBlue)
			draw1.rectangle((x,y+52,x+sizeX,y+52), testBoxBlue)
			draw1.rectangle((x,y+56,x+sizeX,y+56), testBoxBlue)
			draw1.rectangle((x,y,x+4,y+4), testBox)'''
			draw1.text((allX,allY), fontCharacter, font=fontJapanese, fill=textColor)

img0.save(os.getcwd() + '/tex0.png')
img1.save(os.getcwd() + '/tex1.png')
sys.exit('Done')
