import numpy as np
from cv2 import cv2
import matplotlib

def merge_lines(height, lines):
    print('--------------------------\n {}'.format(lines))

    line1 = 0
    line2 = 0

    for i in range(len(lines)):
        line1 += lines[i][0]
        line2 += lines[i][1]

    line1 /= len(lines)
    line2 /= len(lines)

    line = (line1, line2)

    print(line)

    slope, intercept = line

    y2 = int(height*0.5)
    x1 = int((height - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
        
    return np.array([x1, height, x2, y2])

class LaneFinder():
    def __init__(self):
        return

    def find_lanes(self, img):
        # Resize previes screen
        height = img.shape[0]
        width = img.shape[1]
        img = cv2.resize(img, (int(width * 0.6), int(height * 0.6)))

        # Gray and Canny
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blured = cv2.GaussianBlur(gray, (3, 3), 0)
        lines_masked = cv2.Canny(blured, 250, 300)

        # Generate triangle of interest and find lines inside it
        height = lines_masked.shape[0]
        width = lines_masked.shape[1]

        triangle = np.array([[(0, height), (width, height), (width/2, height/2)]])
        mask = np.zeros_like(lines_masked)
        cv2.fillPoly(mask, np.array(triangle, dtype=np.int32), 255)

        masked_img = cv2.bitwise_and(lines_masked, mask)
        lines = cv2.HoughLinesP(masked_img, 1, np.pi/180, 50, maxLineGap=350)

        # Draw center of screen line
        cv2.line(img, (int(width/2), 0), (int(width/2), height), (0, 0, 255), 3)

        # Draw lane lines
        negative = []
        positive = []

        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            params = np.polyfit((x1, x2), (y1, y2), 1)
            slope = params[0]
            intercept = params[1]

            #cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

            if slope < 0:
                negative.append((slope, intercept))
            else:
                positive.append((slope, intercept))

        print(negative, positive)

        #left_lane = average_line(negative)
        #right_lane = average_line(positive)

        left_lane = merge_lines(height, negative)
        right_lane = merge_lines(height, positive)
        line_of_interest = np.array([0, int(height*(22/30)), width, int(height*(22/30))])

        print(left_lane, line_of_interest)
        

        cv2.line(img, (left_lane[0], left_lane[1]), (left_lane[2], left_lane[3]), (0, 255, 0), 3)
        cv2.line(img, (right_lane[0], right_lane[1]), (right_lane[2], right_lane[3]), (0, 255, 0), 3)
        cv2.line(img, (line_of_interest[0], line_of_interest[1]), (line_of_interest[2], line_of_interest[3]), (255, 0, 0), 3)
        #print(negative, positive)
        #print(left_lane, right_lane)


        return img