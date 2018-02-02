slist = [0,0,1,2,(1,2),(1,2,3),3]
i1 >> play('(x(h{euy[aa]s[xo-mnbv*]'+'[hh][hhh]p[pp]'*2+'}))(-[--])' , amp=linvar([1.5,2],[1.5,1,2]), pshift=P[0,4,2,7,11].amen(), dur=Pvar([[PDur(5,8), PDur([7,5],8), PDur([5,[3,7]],8)], .5],[4,2,6])/var([1,2], [64,8]), chop=var([0,0,0,4,0,0,16], 8), bits=var([0,5],[12,4]), delay=(0,var([var([.25,.5],8),0], [20])), crush=var([0,var([12,8,32],[4,4,2,2,1,1])],[12,4])).every(7, 'stutter', 4) + var(slist, 12)
i2 >> loop('dubbird', PRand(45), amp=(.5,1),bits=(4, 6), pshift=P[0,-2,3,6,12,4] + (0,.4), dur=PDur([3,5],8) | PDur(5,12), delay = (0,PDur(3,8)*2))




Scale.default='minor'

dur = P[P[[.5,.5,.5,1,.5,3]*2] | P[.5,.5,.5,1,.5,1,.5,1,.5,2,.5,3.5] ]
durm = var([1,2], sum(dur) * 4)
dur *= durm
p1.reset() >> spark(P[6,4,5,6,[-1,0],5,4,2,3,4,-1,3] | P[6,4,5,6,[0,-1],7,6,5,2,4,-1,3], oct=(6,7), dur=dur, formant=(3,5), sus=p1.dur/var([2,3],sum(dur)*durm))
p3.reset() >> sawbass(P[6,4,5,6,[-1,0],5,4,2,3,4,-1,3] | P[6,4,5,6,[0,-1],7,6,5,2,4,-1,3], oct=(6,7), dur=dur, formant=(3,5), sus=p1.dur/var([1,4],sum(dur)*durm))
p1.amplify=var([0,1], sum(dur) * 2 * durm)
p3.amplify=var([1,0], sum(dur) * 2 * durm)

p2 >> play('<h><->', pshift=(var([0,4,2,7,11]),0), sus=p2.dur*.8, amp=.7) + ([0,1,2,3], var([0,1,2,3]))
