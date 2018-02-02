Scale.default='minor'
r1 >> spark([0,1,2,3,4,0,5,4,3,2,1,4], dur=[2.5,.5]).every(12, 'reverse')
r2 >> sawbass([0,4,0,-3], dur=8, fmod=(0,1)) + (0,7)
r3.reset() >> play('<V  ( (-=))><g   >',rate=.2, dur=4, amp=(1.2,1.5), room=5, mix=((.1, .6),)*2)
r4 >> play(' (cC)', rate=.16, dur=6)
r5.reset() >> sawbass([4,0,5,4,3,4], oct=7, dur=[3,3,2,1,3,3]) + var([0,[-2,-4]], 15)

# Silica: 
p1 >> piano([0,[-1, 1],(2, 4)])

# ChrisLHall: 
c1 >> play('asdfghthasdfqwer', pshift=PRand([-5,0]))






r1 >> play('(xo)--',dur=PDur(3,8), pshift=PRand(-8,8))
r2 >> loop('dubbird', P[5:10] + PRand(40)*var([0,1],[12,4]), pshift=P[0,4,1,3,2] * PwRand([1,-1], [9,1]) + (0,[7,-7]), delay=Pvar([0,(0,.5)], [27,5]), chop=PwRand([0,4],[7,1]))
r3 >> play('(vi)( -)[---](o-)(mx)', dur=Pvar([PDur(5,8), .125],[15,1])).every(12, 'reverse')
r4 >> loop('dubbird', P[20:30], rate=(.2,.3,.1), chop=2, room=3, mix=.1, delay=(0,.5,1), dur=P[.5,1] * var([.5,1,2,1], [8,2,6]))
r5 >> play('         c', dur=16)
with when('foo') as w:
    w.when(lambda: r5.degree=='c')
    w.then(lambda: Group(r1,r2,r3,r4,r5).stop())
# build up to all this!





Scale.default='minor'
r1.reset() >> viola([0,4,-2,2], oct=4, dur=8, delay=(0,4,6))
r2 >> pluck([0,[-7,[-5,-3]]], sus=(.5), delay=(0,.5), dur=[1.5,2.5], chop=(4,0), room=3, mix=.4) + ((0,7) ) #+ var([0,[-7,[-5,-3]]],4))
r3 >> piano([7,4,2,0,3,2,1,0,3,2,1,0,3,2,1,2], delay=(0,[.25,.5]), chop=Pvar([[0],(4,3)],[12,4])) + (0,7,2,4)
r4 >> bass([0,2,4], dur=[1.5,.5,2], amp=.4, oct=var([5,6,7,5,4],16), delay=(0,.25,.5,1), sus=r4.dur * (.7,.7,.7,1)) + r3.degree
r5 >> bass(P[0,1,2,1,[0,4]] + var([0,-2], 48), dur=[6,2,2,[12,14],[26,24]], amp=.7, oct=(4,5))
r6 >> play('(VX)   ', dur=4, amp=1 + (r6.degree=='X')*.9)

builds = [64, 32, 64, 128, 128, 128, 224]
part = [0]
parts = [r1,r2,r3,r4,r5,r6]
def iter_part():
    i = part[0]
    part[0] += 1
    part[0] %= len(builds)
    return parts[:i+1]
def play_part():
    synths = iter_part()
    print('soloing part {} for {} beats'.format(part[0], builds[part[0]]))
    Group(*synths).solo()
    
with when('builds') as w:
    w.when(lambda: var(PRange(len(builds)), builds)==part[0])
    w.then(lambda: play_part())