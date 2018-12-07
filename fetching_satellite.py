import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
from PIL import Image
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox
import image_detection


def fetch():
    INSTANCE_ID = "9cd75fc0-6958-4d2e-8161-f9dd0665281d"

    bbox = [14.672, -24.487, 15.782, -22.705]
    bBox = BBox(bbox=bbox, crs=CRS.WGS84)

    wms_true_color_request = WmsRequest(layer='TRUE_COLOR',
                                        bbox=bBox,
                                        time=('2018-11-01', '2018-12-01'),
                                        width=512, height=900,
                                        instance_id=INSTANCE_ID)
    img = wms_true_color_request.get_data()

    img = np.array(img)[..., ::-1]

    os.chdir("tmp")
    # cv2.imwrite("img", img[0].tolist())
    for i in range(img.__len__()):
        x = image_detection.white_percentage(img[i])
        # cv2.imshow("imgMod", image_detection.divide_pic(img[i]))
        # cv2.waitKey(0)
        if (x < 40):
            cv2.imshow("img", img[i])
            cv2.waitKey(0)

            string = "img" + str(i) + ".jpg"

            result = Image.fromarray(np.array(img[i])[..., ::-1])
            result.save(string)
            # cv2.imwrite(strinG, img[i].tolist())

    # print('These %d images were taken on the following dates:' % len(img))
    # for index, date in enumerate(wms_true_color_request.get_dates()):
    #     print(' - image %d was taken on %s' % (index, date))


if __name__ == '__main__':
    fetch()
