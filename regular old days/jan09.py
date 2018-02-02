""" suggestions
console output pane/pop-in pane
initial file/commands to run (for example to add sample paths)
"""

Samples.addPath('/Users/irdumb/Projects/Discord/Red-DiscordBot/data/foxdot/samples')


Scale.default='minor'
p1 >> play('xn    ', amp=.5, rate=(.8,.1), dur=PDur(5,8))
# l1 >> loop('red', (P[10:20],P[30:50]), chop=(0,(.8,0)),  rate=(0,(1.2,0, -1)), amp=(1,.6))
p2 >> play('(Vo)( -){[--][----]} ', dur=.5, amp=1.1) + PRand(8)

bb >> bass([0,4,2,3,1], dur=8, chop=[[(4,6),4],8], amp=P[[.7,1],1]*.9, room=2, mix=(.2,.5))
sp.reset() >> soprano([4,3,6,1,0], dur=PDur(3,8) * 12, amp=.4, bits=(7,8), oct=(6,5))
pp.reset() >> piano([4,3,6,1,0], dur=[1.5,1.5,1.5,1.5,2], bits=4, amp=.5, chop=(0,(3,4)), room=4, mix=(0,.4), formant=Pvar([0,1,(0,1),1], 24)) + var([0,bb.pitch],32)
pl.reset() >> pluck(dur=PDur(3,8) | P[2]).follow(pp)
ran = PRand(320)
vvv = P(P[120:140] * -1 +140, P[120:140] + var([0,ran], 32) )
offset = 0 # 120 ..
samp = 'bender' # morgan seapig spstick .. red ?
lb.reset() >> loop(samp, vvv + offset, rate=(0,(0,var([0,1.05], 64))), amp=P(1,1)) # amp=P(1,1.5) ..
# @Axas
l1 >> glass([2,1,3], amp=0.9, spin=1, decay=2)
l2 >> razz([1,2,1,2,4,5], amp=0.6, blur=1, delay=1, dur=PRand(0,8))

l3 >> dirt([0], amp=.2, delay=2, dur=[1.5,.125,.375], sus=l3.dur*1.25, chop=2) + bb.pitch
bb.amplify=1
