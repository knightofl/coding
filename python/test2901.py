import selectivesearch
import cv2
import matplotlib.pyplot as plt
import numpy as np


def compute_iou(cand_box, gt_box):
    cand_box_area = (cand_box[2]-cand_box[0]) * (cand_box[3]-cand_box[1])
    gt_box_area = (gt_box[2]-gt_box[0]) * (gt_box[3]-gt_box[1])

    x1 = np.maximum(cand_box[0], gt_box[0])
    y1 = np.maximum(cand_box[1], gt_box[1])
    x2 = np.minimum(cand_box[2], gt_box[2])
    y2 = np.minimum(cand_box[3], gt_box[3])

    intersection = np.maximum(x2-x1, 0) * np.maximum(y2-y1, 0)
    union = cand_box_area + gt_box_area - intersection
    iou = intersection / union
    return iou


img = cv2.imread('./tmp/iu.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 8))
plt.imshow(img_rgb)
plt.show()

_, regions = selectivesearch.selective_search(
    img_rgb, scale=280, min_size=3000)
print(regions)

cand_rects = [cand['rect'] for cand in regions]
print(cand_rects)

gt_box = [410, 260, 650, 1080]
choice_rgb_cand = (125, 255, 51)
choice_rgb_gt = (255, 0, 0)

img_rgb_copy = img_rgb.copy()

for rect in cand_rects:
    left = rect[0]
    top = rect[1]
    right = rect[2] + left
    bottom = rect[3] + top

    img_rgb_copy = cv2.rectangle(img_rgb_copy,
        (left, top), (right, bottom), color=choice_rgb_cand, thickness=2)

plt.figure(figsize=(8, 8))
plt.imshow((img_rgb_copy))
plt.show()

img_rgb_copy = cv2.rectangle(img_rgb, (gt_box[0], gt_box[1]),
    (gt_box[2], gt_box[3]), color=choice_rgb_gt, thickness=2)
plt.figure(figsize=(8, 8))
plt.imshow((img_rgb_copy))
plt.show()

cand_rects.sort()

for index, cand_box in enumerate(cand_rects):
    cand_box = list(cand_box)
    cand_box[2] = cand_box[2] + cand_box[0]
    cand_box[3] = cand_box[3] + cand_box[1]

    iou = compute_iou(cand_box, gt_box)

    if iou > 0.5:
        print('index : ', index, 'iou : ', iou, 'rectangle : ',
            (cand_box[0], cand_box[1], cand_box[2], cand_box[3]))
        img_rgb_copy = cv2.rectangle(img_rgb, (cand_box[0], cand_box[1]),
            (cand_box[2], cand_box[3]), choice_rgb_cand, thickness=5)
        text = "%d : %.2f" % (index, iou)
        img_rgb_copy = cv2.putText(img_rgb, text, (cand_box[0]+100, cand_box[1]+10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.4, color=choice_rgb_cand, thickness=2)

plt.figure(figsize=(8, 8))
plt.imshow(img_rgb_copy)
plt.show()
