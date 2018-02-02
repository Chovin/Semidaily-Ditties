

Samples.addPath('/Users/irdumb/Projects/Discord/Red-DiscordBot/data/foxdot/samples')
Scale.default='minor'

r1 >> loop('quakesfx', (P[0:10] + 80.7 + var([0, PRand(100)], 24), var([PRand(100), 0], 32) +  PRange(20,0,-1)),
    rate=(1,.9), chop=P[0,4,(0,3)] * var([0,1],PRand(2,16)),
    amp=PRand([0,1,1,1]))
r2 >> play('(Vo){   -}{[--][---]   [----]}( -)', room=(0,1), formant=(0,1),
    amp=1.25, dur=(PDur([3,5],8),.5),
    rate=(1,(0,[2,4,8])),
    delay=(0,(0, PRand([0,.5,1])) ),
    chop=(PRand([0,0,0,4,8,16]),0)
    ) + 2
bbb =  var([0,7,4],12)
r3 >> dirt([0,0,2,4,2], dur=PDur(var([3,5],[24,8]),8), formant=(0,2), oct=5) + bbb
r4 >> play('< V>< (-[---])>', dur=r3.dur/2, formant=r3.formant * 2) + bbb
r5 >> pluck(PChain({
    0: [0,1],
    1: [2,0],
    2: [3,1],
    3: [4,2],
    4: [4,5,3,2],
    5: [4]
    }) + (0, var(PRand([0,2,4])), var(PRand([0,1,5,6,7,9,3]))),
    dur=var([2,4],[PRand([4,8,12],PRand([4,4,4,4,8]))])/var([1,2],48),
    formant=2, delay=(0,PwRand([.25,1],[5,1]), .5),
    chop=var([0,4],32), room=2)




Scale.default='minor'
# , var([PRand(100), 0], 32) +  PRange(20,0,-1)
r1 >> loop('quakesfx', (P[0:10] + 80.7  + var([0, PRand(100)], 24) ,  var([PRand(100), 0], 32) +  PRange(20,0,-1)),
    rate=(1,.9), chop=P[0,4,(0,3)] * var([0,1],PRand(2,16)),
    amp=PRand([0,1,1,1]))
r2 >> play('(Vo){   -}{[--][---]   [----]}( -)', room=(0,1), formant=(0,1),
    amp=1.25, dur=(PDur([3,5],8),.5),
    rate=(1,(0,[2,4,8])),
    delay=(0,(0, PRand([0,.5,1])) ),
    chop=(PRand([0,0,0,4,8,16]),0)
    ) + 2
bbb =  var([0,7,4],12)
r3 >> dirt([[[0,4],0],0,[2,1],[4,[3,6]],[2,[1,5]]], dur=PDur(var([3,5],[24,8]),8), formant=(0,linvar([0,2],24)), oct=5, amp=.7, chop=r3.dur*var([2,4],[48,12])*var([0,1],32)) + bbb
r4 >> play('<V ><(-[---]) >', dur=r3.dur/2, formant=r3.formant * 2) + bbb
r5 >> pluck(PChain({
    0: [0,1],
    1: [2,0],
    2: [3,1],
    3: [4,2],
    4: [4,5,3,2],
    5: [4]
    }) + (0, var(PRand([0,2,4])), var(PRand([0,1,5,6,7,9,3]))),
    dur=var([2,4],[PRand([4,8,12],PRand([4,4,4,4,8]))])/var([1,2],48),
    formant=2, delay=(0,PwRand([.25,1],[5,1]), .5),
    chop=var([0,4],32), room=2) + [0,bbb]
