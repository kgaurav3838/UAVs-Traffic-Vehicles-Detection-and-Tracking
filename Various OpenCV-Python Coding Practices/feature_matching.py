import cv2

cereal = cv2.imread('../data/reeses_puffs.png', 0)
cereals = cv2.imread('../data/many_cereals.jpg', 0)

cv2.imshow('cereal', cereal)
cv2.waitKey(0)
cv2.imshow('cereals', cereals)
cv2.waitKey(0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(cereal, None)
kp2, des2 = orb.detectAndCompute(cereals, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
cerealMatches = cv2.drawMatches(cereal, kp1, cereals, kp2, matches[:25], None, flags=2)
cv2.imshow('img', cerealMatches)
cv2.waitKey(0)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(cereal, None)
kp2, des2 = sift.detectAndCompute(cereals, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
good = []
for match1, match2 in matches:
    if match1.distance < 0.75 * match2.distance:
        good.append([match1])
siftMatches = cv2.drawMatchesKnn(cereal, kp1, cereals, kp2, good, None, flags=2)
cv2.imshow('img', siftMatches)
cv2.waitKey(0)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
good = []
for match1, match2 in matches:
    if match1.distance < 0.7 * match2.distance:
        good.append([match1])

flannMatches = cv2.drawMatchesKnn(cereal, kp1, cereals, kp2, good, None, flags=0)
cv2.imshow('img', flannMatches)
cv2.waitKey(0)
