import csv
import pandas as pd

def openfile(form,num):
    result= []

    with open(f'./dataReplacePOS/{form}.csv', encoding="utf8") as csvfile: 
     opencsvform1 = csv.reader(csvfile)
     next(opencsvform1, None)

     for row in opencsvform1:
       prints= row[num]
       rather=prints.replace("('ค่อนข้าง', 'ADJ')","('ค่อนข้าง', 'AUX')")
       crowded= rather.replace("('แออัด', 'NOUN')","('แออัด', 'ADJ')").replace("('แออัด', 'VERB')","('แออัด', 'ADJ')").replace("('แออัด', 'PROPN')","('แออัด', 'ADJ')")
       fun = crowded.replace("('สนุก', 'VERB')","('สนุก', 'ADV')").replace("('สนุก', 'NOUN')","('สนุก', 'ADV')")
       beautiful = fun.replace("('สวย', 'NOUN')","('สวย', 'ADJ')").replace("('สวย', 'VERB')","('สวย', 'ADJ')").replace("('สวยงาม', 'VERB')","('สวยงาม', 'ADJ')").replace("('สวยงาม', 'NOUN')","('สวยงาม', 'ADJ')")
       personin = beautiful.replace("('คนใน', 'VERB')","('คนใน', 'NOUN')")
       way = personin.replace("('ทาง', 'ADP')","('ทาง', 'NOUN')")
       enjoy = way.replace("('เพลิดเพลิน', 'NOUN')","('เพลิดเพลิน', 'VERB')").replace("('เพลิดเพลิน', 'PROPN')","('เพลิดเพลิน', 'VERB')")
       afternoon = enjoy.replace("('บ่าย', 'ADJ')","('บ่าย', 'NOUN')")
       smell = afternoon.replace("('กลิ่น', 'PROPN')","('กลิ่น', 'NOUN')")
       popular = smell.replace("('นิยม', 'VERB')","('นิยม', 'NOUN')")
       of = popular.replace("('ของ', 'ADP')","('ของ', 'NOUN')")
       at = of.replace("('อย่าง', 'PART')","('อย่าง', 'NOUN')").replace("('อย่า', 'NOUN')","('อย่า', 'VERB')")
       surprised = at.replace("('ประหลาดใจ', 'NOUN')","('ประหลาดใจ', 'VERB')") 
       clean = surprised.replace("('สะอาด', 'NOUN')","('สะอาด', 'VERB')").replace("('สะอาด', 'ADJ')","('สะอาด', 'VERB')")
       miss=clean.replace("('พลาด', 'NOUN')","('พลาด', 'VERB')")
       travel = miss.replace("('ท่องเที่ยว', 'NOUN')","('ท่องเที่ยว', 'VERB')")
       relax= travel.replace("('ผ่อนคลาย', 'NOUN')","('ผ่อนคลาย', 'VERB')")
       good=relax.replace("('ดี', 'NOUN')","('ดี', 'ADJ')").replace("('ดี', 'PROPN')"," ('ดี', 'ADJ')").replace("('ดี', 'DET')","('ดี', 'ADJ')").replace("('ดี', 'AUX')","('ดี', 'ADJ')").replace("('ดี', 'VERB')","('ดี', 'ADJ')")
       cool=good.replace("('ยอดเยี่ยม', 'NOUN')","('ยอดเยี่ยม', 'ADJ')").replace("('เยี่ยม', 'NOUN')","('เยี่ยม', 'ADJ')")
       watch=cool.replace("('ชม', 'NOUN')","('ชม', 'VERB')")
       amazing=watch.replace("('น่าตื่นตาตื่นใจ', 'VERB') ","('น่าตื่นตาตื่นใจ', 'VERB') ")
       free=amazing.replace("('ฟรี', 'NOUN')","('ฟรี', 'ADJ')").replace("('ฟรี', 'VERB')","('ฟรี', 'ADJ')") 
       more=free.replace("('เพิ่มเติม', 'NOUN')","('เพิ่มเติม', 'ADJ')").replace("('เพิ่มเติม', 'VERB')","('เพิ่มเติม', 'ADJ')")
       somuch=more.replace("('มากมาย', 'NOUN')","('มากมาย', 'ADJ')")
       bearish=somuch.replace("('หยาบคาย', 'NOUN')","('หยาบคาย', 'ADJ')")
       go=bearish.replace("('ไป', 'PART')","('ไป', 'VERB')")
       right= go.replace("('ถูกต้อง', 'NOUN')","('ถูกต้อง', 'VERB')")
       ride=right.replace("('ขับ', 'NOUN'),","('ขับ', 'VERB'),")
       pls=ride.replace("('โปรด', 'NOUN')","('โปรด', 'ADJ')").replace("('โปรด', 'CCONJ')","('โปรด', 'ADJ')")
       oh=pls.replace("('น่าอัศจรรย์', 'ADJ')","('น่าอัศจรรย์', 'VERB')").replace("('อัศจรรย์', 'NOUN')","('อัศจรรย์', 'ADJ')").replace("('อัศจรรย์', 'PART')","('อัศจรรย์', 'ADJ')")
       cute=oh.replace("('น่ารัก', 'VERB')","('น่ารัก', 'ADJ')")
       none=cute.replace("('ว่าง', 'VERB')","('ว่าง', 'ADJ')")
       sure=none.replace("('ชัดเจน', 'NOUN')","('ชัดเจน', 'ADJ')")
       dontcare=sure.replace("('หยิ่งผยอง', 'NOUN')","('หยิ่งผยอง', 'ADJ')").replace("('หยิ่ง', 'NOUN')","('หยิ่ง', 'ADJ')")
       little=dontcare.replace("('น้อย', 'NOUN')","('น้อย', 'ADJ')")
       near=little.replace("('ใกล้เคียง', 'NOUN')","('ใกล้เคียง', 'ADJ')")
       odd=near.replace("('แปลกประหลาด', 'VERB')","('แปลกประหลาด', 'ADJ')").replace("('แปลก', 'NOUN')","('แปลก', 'ADJ')")
       ontop=odd.replace("('ด้านบน', 'VERB')","('ด้านบน', 'NOUN')")
       passes=ontop.replace("('เคย', 'AUX')","('เคย', 'ADJ')").replace("('เคย', 'NOUN')","('เคย', 'ADJ')")
       real=passes.replace("('จริง', 'NOUN')","('จริง', 'ADJ')")
       scear=real.replace("('ผยอง', 'NOUN')","('ผยอง', 'VERB')")
       ready=scear.replace("('เตรียมพร้อม', 'NOUN')","('เตรียมพร้อม', 'VERB')")
       like=ready.replace("('คุ้มค่า', 'NOUN')","('คุ้มค่า', 'VERB')")
       quiets=like.replace("('เงียบ', 'NOUN')","('เงียบ', 'VERB')")
       forgets=quiets.replace("('ลืม', 'NOUN')","('ลืม', 'VERB')")
       love=forgets.replace("('นิยม', 'VERB')","('นิยม', 'NOUN')")
       fit= love.replace("('เหมาะสม', 'NOUN')","('เหมาะสม', 'VERB')")
       no=fit.replace("('ไม่ใช่', 'NOUN')","('ไม่ใช่', 'VERB')")
       yes=no.replace("('ใช่', 'NOUN')","('ใช่', 'NOUN')")
       home=yes.replace("('ที่อยู่', 'VERB')","('ที่อยู่', 'NOUN')")
       about=home.replace("('ประมาณ', 'NOUN')","('ประมาณ', 'VERB')")
       perfect=about.replace("('สมบูรณ์แบบ', 'NOUN')","('สมบูรณ์แบบ', 'VERB')")
       careful=perfect.replace("('ระวัง', 'NOUN')","('ระวัง', 'VERB')").replace("('ระมัดระวัง', 'NOUN')","('ระมัดระวัง', 'VERB')")
       recommend=careful.replace("('แนะนำ', 'NOUN')","('แนะนำ', 'VERB')")
       draw=recommend.replace("('ลาก', 'NOUN')","('ลาก', 'VERB')")
       rent=draw.replace("('เช่า', 'NOUN')","('เช่า', 'VERB')")
       down=rent.replace("('ลง', 'NOUN')","('ลง', 'VERB')")
       can=down.replace("('สามารถ', 'NOUN')","('สามารถ', 'VERB')")
       different=can.replace("('แตกต่าง', 'NOUN')","('แตกต่าง', 'VERB')")
       cover=different.replace("('คุ้ม', 'NOUN')","('คุ้ม', 'VERB')")
       only=cover.replace("('เฉพาะ', 'APD')","('เฉพาะ', 'VERB')")
       peacful=only.replace("('สงบ', 'NOUN')","('สงบ', 'VERB')").replace("('เงียบสงบ', 'PART')","('เงียบสงบ', 'ADJ')")
       taken=peacful.replace("('ถ่าย', 'NOUN')","('ถ่าย', 'VERB')")
       cry=taken.replace("('เสียดาย', 'NOUN')","('เสียดาย', 'VERB')")
       delicious=cry.replace("('อร่อย', 'NOUN')","('อร่อย', 'ADJ')")
       tryagain=delicious.replace("('พยายาม', 'NOUN')","('พยายาม', 'VERB')")
       kun=tryagain.replace("('กันเอง', 'NOUN')","('กันเอง', 'ADV')")
       mores=kun.replace("('อีก', 'DET')","('อีก', 'ADV')")
       sures=mores.replace("('แน่นอน', 'NOUN')","('แน่นอน', 'ADV')")
       letgo=sures.replace("('ไป', 'AUX')","('ไป', 'ADV')").replace("('ไป', 'PART')","('ไป', 'ADV')")
       same=letgo.replace("('เช่นกัน', 'VERB')","('เช่นกัน', 'ADV')")
       another=same.replace("('ๆ', 'NOUN')","('ๆ', 'PUNCT')").replace("('ๆ', 'SYM')","('ๆ', 'PUNCT')")
       many=another.replace("('หลาย', 'NOUN')","('หลาย', 'ADV')").replace("('หลาย', 'PART')","('หลาย', 'ADV')").replace("('หลาย', 'DET')","('หลาย', 'ADV')").replace("('หลาย', 'VERB')","('หลาย', 'ADV')")
       thats=many.replace("('นี่', 'NOUN')","('', 'ADV')").replace("('', 'PART')","('', 'ADV')").replace("('', 'DET')","('', 'ADV')").replace("('', 'VERB')","('', 'ADV')")
       trues=thats.replace("('แท้จริง', 'NOUN')","('แท้จริง', 'ADV')").replace("('แท้จริง', 'PART')","('แท้จริง', 'ADV')").replace("('แท้จริง', 'DET')","('แท้จริง', 'ADV')").replace("('แท้จริง', 'VERB')","('แท้จริง', 'ADV')")
       yet=trues.replace("('ยัง', 'NOUN')","('ยัง', 'ADV')").replace("('ยัง', 'PART')","('ยัง', 'ADV')").replace("('ยัง', 'DET')","('ยัง', 'ADV')").replace("('ยัง', 'VERB')","('ยัง', 'ADV')")
       back=yet.replace("('หลัง', 'NOUN')","('หลัง', 'ADV')").replace("('หลัง', 'PART')","('หลัง', 'ADV')").replace("('หลัง', 'DET')","('หลัง', 'ADV')").replace("('หลัง', 'VERB')","('หลัง', 'ADV')")
       romantic=back.replace("('โรแมนติก', 'NOUN')","('โรแมนติก', 'ADJ')").replace("('โรแมนติก', 'PART')","('โรแมนติก', 'ADJ')").replace("('โรแมนติก', 'DET')","('โรแมนติก', 'ADJ')").replace("('โรแมนติก', 'VERB')","('โรแมนติก', 'ADJ')")
       po=romantic.replace("('พอ', 'NOUN')","('พอ', 'ADV')").replace("('พอ', 'PART')","('พอ', 'ADV')").replace("('พอ', 'DET')","('พอ', 'ADV')").replace("('พอ', 'VERB')","('พอ', 'ADV')")
       nan=po.replace("('แน่น', 'NOUN')","('แน่น', 'ADV')").replace("('แน่น', 'PART')","('แน่น', 'ADV')").replace("('แน่น', 'DET')","('แน่น', 'ADV')").replace("('แน่น', 'VERB')","('แน่น', 'ADV')")
       morethen=nan.replace("('เกินไป', 'VERB')","('เกินไป', 'ADV')")
       bad=morethen.replace("('เลวร้าย', 'NOUN')","('เลวร้าย', 'ADJ')").replace("('เลวร้าย', 'VERB')","('เลวร้าย', 'ADJ')")
       most=bad.replace("('เกิน', 'VERB')","('เกิน', 'ADV')")
       phuket=most.replace("('ภูเก็ต', 'PROPN')","('ภูเก็ต', 'NOUN')")
       reason=phuket.replace("('สมเหตุสมผล', 'NOUN')","('สมเหตุสมผล', 'ADV')").replace("('สมเหตุสมผล', 'PART')","('สมเหตุสมผล', 'ADV')").replace("('สมเหตุสมผล', 'DET')","('สมเหตุสมผล', 'ADV')").replace("('สมเหตุสมผล', 'VERB')","('สมเหตุสมผล', 'ADV')")
       view=reason.replace("('มุมมอง', 'VERB')","('มุมมอง', 'NOUN')")
       ever=view.replace("('เคย', 'NOUN')","('เคย', 'ADV')").replace("('เคย', 'AUX')","('เคย', 'ADV')").replace("('เคย', 'DET')","('เคย', 'ADV')").replace("('เคย', 'VERB')","('เคย', 'ADV')")
       give=ever.replace("('ให้', 'SCONJ')","('ให้', 'VERB')")
       crazy=give.replace("('บ้า', 'NOUN')","('บ้า', 'VERB')")
       ride=crazy.replace("('ขี่', 'NOUN')","('ขี่', 'VERB')")
       swim=ride.replace("('ว่าย', 'NOUN')","('ว่าย', 'VERB')")
       stand=swim.replace("('โดดเด่น', 'NOUN')","('โดดเด่น', 'ADJ')")
       nid=stand.replace("('หน่อย', 'NOUN')","('หน่อย', 'ADV')")
       thai=nid.replace("('ไทย', 'PROPN')","('ไทย', 'NOUN')")
       care=thai.replace("('ดูแลรักษา'', 'NOUN')","('ดูแลรักษา'', 'VERB')")
       find=care.replace("('ค้นหา', 'NOUN')","('ค้นหา', 'VERB')")
       hot=find.replace("('ร้อน', 'NOUN')","('ร้อน', 'VERB')")
       cook=hot.replace("('ปรุง', 'NOUN')","('ปรุง', 'VERB')")
       warm=cook.replace("('อบอุ่น', 'NOUN')","('อบอุ่น', 'VERB')")
       forward=warm.replace("('ล่วงหน้า', 'NOUN')","('ล่วงหน้า', 'ADV')")
       bath=forward.replace("('อาบ', 'NOUN')","('อาบ', 'VERB')")
       comford=bath.replace("('สบาย', 'NOUN')","('สบาย', 'VERB')")
       hire=comford.replace("('จ้าง', 'NOUN')","('จ้าง', 'VERB')")
       up=hire.replace("('ขึ้น', 'NOUN')","('ขึ้น', 'VERB')")
       but=up.replace("('แต่', 'NOUN')","('แต่', 'VERB')")
       pump=but.replace("('สูบ', 'NOUN')","('สูบ', 'VERB')")
       expensive=pump.replace("('แพง', 'NOUN')","('แพง', 'ADJ')")
       versions=expensive.replace("('หลากหลาย', 'NOUN')","('หลากหลาย', 'ADJ')")
       push=versions.replace("('ดึง', 'NOUN')","('ดึง', 'VERB')")
       maps=push.replace("('แผนที่', 'SCONJ')","('แผนที่', 'NOUN')")
       many=maps.replace("('มาก', 'NOUN')","('มาก', 'ADV')")
       worry=many.replace("('กังวล', 'NOUN')","('กังวล', 'VERB')")
       ex=worry.replace("('เช่น', 'NOUN')","('เช่น', 'CONJ')")
       slip=ex.replace("('ลื่น', 'NOUN')","('ลื่น', 'VERB')")
       goup=slip.replace("('ปีน', 'NOUN')","('ปีน', 'VERB')")
       wow=goup.replace("('ว้าว', 'NOUN')","('ว้าว', 'INT')")
       tired=wow.replace("('เหนื่อย', 'NOUN')","('เหนื่อย', 'VERB')")
       stop=tired.replace("('จอด', 'NOUN')","('จอด', 'VERB')")
       easy=stop.replace("('ง่ายดาย', 'NOUN')","('ง่ายดาย', 'ADV')")
       sun=easy.replace("('พระอาทิตย์', 'PROPN')","('พระอาทิตย์', 'NOUN')")
       cold=sun.replace("('เย็น', 'NOUN')","('เย็น', 'VERB')")
       croos=cold.replace("('ตรงข้าม', 'NOUN')","('ตรงข้าม', 'ADV')").replace("('ข้ามถนน', 'VERB')","('ข้ามถนน', 'NOUN')")
       rest=croos.replace("('พัก', 'NOUN')","('พัก', 'VERB')")
       risky=rest.replace("('เสี่ยง', 'NOUN')","('เสี่ยง', 'VERB')")
       refishing=risky.replace("('สดชื่น', 'NOUN')","('สดชื่น', 'VERB')")
       book=refishing.replace("('จอง', 'NOUN')","('จอง', 'VERB')")
       longs=book.replace("('ยาว', 'NOUN')","('ยาว', 'VERB')")
       out=longs.replace("('นอก', 'NOUN')","('นอก', 'PREP')")
       okk=out.replace("('เหมาะ', 'NOUN')","('เหมาะ', 'VERB')")
       thens=okk.replace("('จึง', 'SCONJ')","('จึง', 'ADV')")
       standup=thens.replace("('ยืน', 'NOUN')","('ยืน', 'VERB')")
       veryok=standup.replace("('เรียบร้อย', 'NOUN')","('เรียบร้อย', 'VERB')")
       ty=veryok.replace("('ขอบคุณ', 'NOUN')","('ขอบคุณ', 'VERB')")
       learn=ty.replace("('เรียนรู้', 'NOUN')","('เรียนรู้', 'VERB')")
       bhuda=learn.replace("('พุทธ', 'PROPN')","('พุทธ', 'NOUN')")
       khod=bhuda.replace("('ถอด', 'NOUN')","('ถอด', 'VERB')")
       fast=khod.replace("('เร็ว', 'NOUN')","('เร็ว', 'ADV')")
       slow=fast.replace("('ช้า', 'NOUN')","('ช้า', 'ADV')")
       commemorative=slow.replace("('ระลึก', 'NOUN')","('ระลึก', 'VERB')")
       respect=commemorative.replace("('เคารพ', 'NOUN')","('เคารพ', 'VERB')")
       hight=respect.replace("('สูง', 'NOUN')","('สูง', 'VERB')")
       busy=hight.replace("('พลุกพล่าน', 'NOUN')","('พลุกพล่าน', 'VERB')")
       wat=busy.replace("('พบปะ', 'NOUN')","('พบปะ', 'VERB')")
       bhudda=wat.replace("('พระพุทธเจ้า', 'PROPN')","('พระพุทธเจ้า', 'NOUN')")
       allow=bhudda.replace("('อนุญาต', 'NOUN')","('อนุญาต', 'VERB')")
       hahaha=allow.replace("('หัวเราะ', 'NOUN')","('หัวเราะ', 'VERB')")
       stupid=hahaha.replace("('โง่เขลา', 'NOUN')","('โง่เขลา', 'VERB')")
       chaotic=stupid.replace("('วุ่นวาย', 'NOUN')","('วุ่นวาย', 'VERB')")
       darty=chaotic.replace("('สกปรก', 'NOUN')","('สกปรก', 'VERB')")
       hate=darty.replace("('เกลียด', 'NOUN')","('เกลียด', 'VERB')")
       violate=hate.replace("('ละเมิด', 'NOUN')","('ละเมิด', 'VERB')")
       bigest=violate.replace("('กว้างใหญ่', 'NOUN')","('กว้างใหญ่', 'ADJ')").replace("('กว้าง', 'VERB')","('กว้าง', 'ADJ')")
       scaers=bigest.replace("('กลัว', 'PROPN')","('กลัว', 'VERB')").replace("('กลัว', 'NOUN')","('กลัว', 'VERB')")
       exchange=scaers.replace("('แลก', 'NOUN')","('แลก', 'VERB')")
       coconut=exchange.replace("('มะพร้าว', 'VERB')","('มะพร้าว', 'NOUN')")
       cake=coconut.replace("('เค้ก', 'VERB')","('เค้ก', 'NOUN')")
       temple=cake.replace("('วัด', 'VERB')","('วัด', 'NOUN')")
       tantawan=temple.replace("('ทานตะวัน', 'VERB')","('ทานตะวัน', 'NOUN')")
       weam=tantawan.replace("('สวม', 'NOUN')","('สวม', 'VERB')")
       grass=weam.replace("('แว่น', 'NOUN')","('แว่น', 'VERB')")
       sacred=grass.replace("('ศักดิ์สิทธิ์', 'PROPN')","('ศักดิ์สิทธิ์', 'ADJ')")
       ban=sacred.replace("('ห้าม', 'NOUN')","('ห้าม', 'VERB')")
       holiday=ban.replace("('นักขัตฤกษ์', 'VERB')","('นักขัตฤกษ์', 'NOUN')")
       eng=holiday.replace("('อังกฤษ', 'PROPN')","('อังกฤษ', 'NOUN')")
       traveler=eng.replace("('นักท่องเที่ยว', 'VERB')","('นักท่องเที่ยว', 'NOUN')")
       fogus=traveler.replace("('ความสนใจ', 'VERB')","('ความสนใจ', 'NOUN')")
       drink=fogus.replace("('ดื่ม', 'NOUN')","('ดื่ม', 'VERB')")
       shop=drink.replace("(''ร้านค้า', 'PROPN')","(''ร้านค้า', 'NOUN')")
       drinker=shop.replace("('เครื่องดื่ม', 'VERB')","('เครื่องดื่ม', 'NOUN')")
       pub=drinker.replace("('ผับ', 'VERB')","('ผับ', 'NOUN')")
       bar=pub.replace("('สถานบันเทิง', 'PROPN')","('สถานบันเทิง', 'NOUN')")
       ciggaret=bar.replace("('สูบบุหรี่', 'NOUN')","('สูบบุหรี่', 'VERB')")
       control=ciggaret.replace("('ผู้ควบคุม', 'VERB')","('ผู้ควบคุม', 'NOUN')")
       selling=control.replace("('การค้าขาย', 'VERB')","('การค้าขาย', 'NOUN')")
       sleep=selling.replace("('นอน', 'NOUN')","('นอน', 'VERB')")
       nonsensical=sleep.replace("('ไร้สาระ', 'VERB')","('ไร้สาระ', 'ADJ')")
       halfhour=nonsensical.replace("('ครึ่งชั่วโมง', 'VERB')","('ครึ่งชั่วโมง', 'NOUN')")
       follow=halfhour.replace("('ติดตาม', 'NOUN')","('ติดตาม', 'VERB')").replace("('ติดตาม', 'ADP')","('ติดตาม', 'VERB')")
       wind=follow.replace("('กังหันลม', 'VERB')","('กังหันลม', 'NOUN')")
       mountend=wind.replace("('ภูเขา', 'PROPN')","('ภูเขา', 'NOUN')")
       lookbad=mountend.replace("('น่าเศร้า', 'NOUN')","('น่าเศร้า', 'ADJ')")
       shit=lookbad.replace("('ไร้สาระ', 'NOUN')","('ไร้สาระ', 'ADJ')")
       anouthers=shit.replace(", (',,', 'NOUN')","").replace(", (',', 'PUNCT')","").replace(", (',,', 'ADJ'),","").replace("], [(']', 'SYM')","").replace(", (',.,', 'NOUN')","").replace(", (',-,', 'NOUN')","").replace(", (',s,', 'NOUN')","").replace(", (',.]', 'ADV')","")
       
       result.append(anouthers)
     return result
     
def SaveToCsvfile():

    nums=[0,1,2,3,4,5]
    forms=["form1","form2","form3","form4"]
    for form in forms:
       for num in nums :

         infomation = openfile(form,num)
         with open(f'./resultReplacePOS/{form}_row_{num}.csv', mode='w',encoding="utf8",newline='') as savecsvfile:
          fieldnames = [num]
          writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
          writer.writeheader()
          for row in infomation :
           writer.writerow({num:row})        
          print("success to save csv > ",form," in > ",num+1 )
  

def SaveCSVall(form):

    dict = {'patong_google': openfile(form,0), 'patong_trip': openfile(form,1),
            'promthep_google': openfile(form,2), 'promthep_trip': openfile(form,3),
            'wat_google': openfile(form,4), 'wat_trip': openfile(form,5),
            }

    df = pd.DataFrame(dict)
    df.to_csv(f'./ResultQuiz1/{form}.csv', index=False)
    
    print("Success to save all > ",form)

def main():

   filecsvs=["form1","form2","form3","form4"]
   SaveToCsvfile()
   
   for form in filecsvs:
       SaveCSVall(form)

main()
