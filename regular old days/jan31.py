Scale.default='minor'
thing = P[0,1,2,3,4,3,0,4,0,2,1,0]
tdur = [1,1,1,1,8,1,rest(1),1,rest(1),.5,.5,3]
p1.reset() >> gong((thing, thing.reverse()), dur=tdur, delay=(0,[3,1], [.5,1.5], [2,6])) + (0,7,[2,4],6)
p2.reset() >> sawbass(Pvar([var([0,4],8),var([[0,7],4,7,9,13,11,16,15,14], [var([8,4],128)])],[256]), dur=.25, amp=.75, delay=(0,1/3), formant=linvar([2,4],[6,9])) + ([0,6],[0,2,4],-7, 7)
p3.reset() >> bass([7,4,3,6,4,3,2,1], dur=[3,4,2,1,8,2,1,1], oct=(5,6), amp=var([0,.5],[110]), delay=((0,.125),[.5,[.75,.25]]))+ ((0,4),[var([0,2,4],32),var([0,4],32)])
p4 >> play('(xxx[Vx]) ( o) x (  [ [----]]) ', dur=1, room=2, amp=.8, mix=(0,.3)) + 2
Clock.bpm=140  # ?



