
r1 >> viola([0, 4, 6], dur=8, delay=(0,2,4,6), oct=4)
r2 >> pluck([[1,-2],4,-1,0] ,sus=.25, dur=[.5,1.25,.5,.75], delay=(0,[(1,2,1.5),.75,.5])) + (0,[var([7,14],[11,1]),r1.degree+var([5,4],[48,16])])
r3 >> play('<g  ( [        --])><*   >',dur=4, pshift=var([-7,-6,-5]), delay=(0,.1,.2))




r1 >> bass(P[0,2,(4,[6,7])] + Pvar([0,1,[1,7]], 12) + PwRand([0,13,15],[6,1,1]), dur=Pvar([[.5,1], PDur(5,8)],[28,4]), delay=(0,.5,[.25,.5]), sus=r1.dur*(1.75 - PRand(10)/6 ), oct=(5,5,6), formant=linvar([3.5,6],[6,18,24]), amp=.8, room=2, mix=.3)





r1 >> piano(P[-2,5,4,2,1,2,3,2,1,0] + (0,[1,4],[3,2]), dur=[4,4,1,.5,1,.5], delay=(0,[.25,3],[.5,1]), oct=(5,5,(5,6)), sus=(2-PRand(10)/5.5))
r2.reset() >> play('([----][--])'*14 + '* ')
with when('drop?') as w:
    w.when(lambda: r2.degree=='*')
    w.then(lambda: r2 >> play('<(V )( -)[--] x - ><(g )   o   >', amp=1.5, room=2, mix=((0,.3)*2)), rate=(0, [.05,0,0,0,0,0,0,0]))
    # r2 >> play('<(V )( -)[--] x - ><(g )   o   >', amp=1.5, room=2, rate=(0,[(12, 4, .2),0,0,0]), mix=((0,.3)*2))  # rate=(0,[(10, 4, .2),3,0,2])
    # lambda: Clock.clear()

#ChrisLHall
Clock.bpm=90  # later?
c1 >> bass([0,0,0,2,2,2,1,1, 1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,2,2,2,2,2,2], dur=.5, amp=.6)
c2>> play("<x - x -- ><    o   o>", dur=.25)
c3 >>  bass([[0,4],[0,4],[0,4],[2,0],[2,0],[2,0],1,1, 1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,2,2,2,2,2,2], dur=1.5, pshift=19, amp=.4)
# later
c3.stop()
c1 >> bass([[0,2],] * 3 + [[2, 4, 2],] * 6 + [[1, -1, 8, 1, -1],] * 9, dur=.5, amp=.6)




Scale.default='minor'
Root.default=2
r1.reset() >> viola([0,2,4,3,2,1,0,1,2,3,4], dur=[.5,1.5], oct=(4,4,5), delay=(0,[.25,1]) )
r2.reset() >> pluck(r1.degree, dur=r1.dur, delay=(r1.delay, r1.delay+[(1,[.25,.5]),1,.75]), sus=.25) + (0,7)
r3 >> bass([0,4,1,3,2,1], dur=8, oct=4, delay=.5)