Scale.default='minor'
movem = PChain({
    0: 1,
    1: [0,2],
    2: 0
})

mv >> piano(movem, dur=mv.degree.map({
    0: 16,
    1: 24,
    2: 8
}))

mv.amplify=.2  # in case we want to map something onto amp later
r1deg1 = [0,0,1,2,4,5,4,2,4,3,1,4,3,1]

r1.reset() >> dirt(mapvar(mv.degree, {
    0: r1deg1,
    1: [7,0,7,0,6,-1,6,-1,5,4,3,2,4,3,2,[3,[9,12]]],
    2: P[7,6,5,4,5,4,3,4,3,2,1,0,0,0,0,0,0,0,0] + 7,
}, default=r1deg1),
dur=mapvar(mv.degree, {
    0: [.25,[.5,1,.75]],
    2: [.25]*18+ [3.5]
}, default=[.25,[.5,1,.75]]), oct=(4,5,6), delay=(0,.25, .5)) # ??




# timing seems to be broken
Scale.default='minor'
movem = PChain({
    0: 1,
    1: 2,
    2: 0
})

mv >> piano(movem, dur=mapvar(mv.degree, {
    0: 16,
    1: 24,
    2: 16
}))
mv.amplify=1  # in case we want to map something onto amp later
r1deg1 = [0,0,1,2,4,5,4,2,4,3,1,4,3,1]

mp >> piano(mv.degree * 7 + [0,1,2,3], dur=1)

r1.reset() >> dirt(mapvar(mv.degree, {
    0: r1deg1,
    1: [7,0,7,0,6,-1,6,-1,5,4,3,2,4,3,2,[3,[9,12]]],
    2: [13,0,14,0,11,0,12,0,9,7,6,12,4,3,5,2,1,0]
}, default=r1deg1),
dur=[.25,[.5,1,.75]], oct=(4,5,6), delay=(0,.25, .5))
