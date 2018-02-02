Scale.default='minor'
p1 >> piano([0,1,2,3,4,0,3,0,(-1,1,-4),3,2,1],dur=1).stop()
p2.reset() >> piano([0,[P[4,3,2,1].shuffle(),[-1,-3]]], dur=6, sus=(1,7), delay=(0,1)) + (0,7)
p3 >> piano(PChain({
0:[1,2,4,6,-1],
2:[4,0,1],
4:[0],
6:[0,4],
1:[2,0,-1],
-1:[-3,1,0,2],
-3:[-1,0]})+p2.degree, dur=Pvar([PDur(5,8),PDur(3,8)]), amp=1. - (PRand(5)/5)/2., echo=1, decay=2, room=5, mix=(0,.7))
p4.reset()  >> bass(p2.degree%7, dur=[8,2,6], oct=5, chop=P(4,3)*8, formant=2).stop() + (0,[-2,4])
p5 >> sawbass((p3.degree + (0,[-3,2],[1,4]) + [0,-3,-7,0,3,7])%11, dur=Pvar([PRand(16),PRand(8)],64)/2, sus=.5, delay=(0,.125,.25)*PRand([0,1,1,0,2]), oct=6, room=2, mix=(.5), amp=var([0,1.5],256))
p6 >> spark([0,[2,4]],oct=((3,4),)*4, dur=16, delay=(0,1,2,3), sus=6, amp=Pvar([[0],P(PRange(4,0,-1)/4)], [512,256]), room=2, mix=((0,.3),)*4, chop=var([0,8],128))
p7 >> play('zcmsherky?\/', rate=.05, amp=.2, dur=2, room=2, mix=.3) + PRand(8)





Scale.default='minor'
p1.reset() >> pluck(var([0,4,0,3,2,1],[2]) + var([0,-2],[16]) + (0,0,[2,4,[7,12]]), 
dur=1/3, amp=P[PRand(5)/5/2, .0] + .5, bits=(8,7), crush=12, room=2, mix=(0,.5))
p2 >> sawbass(p1.degree + (0,PwRand([0,6],[5,1]),[2,4]), dur=PRand([2,4,8]), chop=3, delay=(0,1,2), oct=(5,6,6), amp=linvar([0,0,1,1], [16]))
p3 >> bass([0,4,[-2,-1]], dur=8, formant=[3,1,3,2], echo=.1, decay=2, amp=[1,.8])
p4 >> spark(var([4,4,var([3,2,0],[12,4])], var([2,4], [16])), dur=[.25,.5,var([1.25,3.25],16)], bits=6, oct=6)

solos = [p1, p4, Group(p1,p2), p3]
def rotate_solos(solos, sdur=32, wdur=128, start=0, wait=False):
    if wait:
        print('waiting')
        return Clock.future(wdur, rotate_solos, args=(solos, sdur, wdur, start, not wait))
    Clock.future(sdur, rotate_solos, args=(solos, sdur, wdur, (start+1)%len(solos), not wait))
    print('soloing {}'.format(solos[start]))
    Clock.future(sdur, (lambda start: solos[start].solo(0)), args=(start))
    solos[start].solo()

def start_at(dur, func, *args):
    if var([0,1], dur) == 1:
        print('boop')
        Clock.future(0, func, args=args)
    else:
        Clock.future(1, start_at, args=(dur, func, *args))

start_at(32, rotate_solos, solos)