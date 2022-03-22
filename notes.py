import matplotlib.pyplot as plt
"""

plt.scatter([152, 96, 167, 152, 521, 523, 345, 884, 694, 80, 252, 607, 24, 220, 55, 73, 82, 401, 198, 267, 78, 159, 249, 33, 47, 117, 87, 431, 797, 352, 77, 49, 42, 184, 31, 139, 183, 222, 112, 311, 135, 263, 75, 1208, 66, 340, 255, 141, 143, 119, 66, 161, 57, 47, 17, 654, 192, 382, 302, 734, 44, 142, 166, 275, 102, 11, 25, 88, 191, 572, 75, 128, 80, 347, 26, 364, 155, 25, 208, 199, 297, 145, 87, 254, 48, 103, 103, 94, 41, 73, 223, 40, 170, 141, 125, 220, 164, 38, 194, 27],
            [0.4, 0.8, 0.6, 1.0, 0.4, 0.6, 0.6, 1.0, 0.6, 1.0, 0.8, 1.0, 0.8, 0.6, 0.6, 0.4, 1.0, 1.0, 0.8, 1.0, 0.4, 0.8, 1.0, 0.8, 0.8, 1.0, 1.0, 0.8, 1.0, 1.0, 0.6, 0.6, 1.0, 1.0, 0.8, 0.8, 0.4, 1.0, 0.8, 1.0, 1.0, 0.8, 0.8, 0.0, 0.8, 1.0, 0.6, 0.8, 1.0, 1.0, 0.6, 0.6, 0.8, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 0.4, 0.8, 0.6, 0.6, 0.8, 0.6, 0.8, 1.0, 0.6, 0.8, 0.6, 0.8, 0.4, 0.8, 0.8, 0.8, 1.0, 1.0, 0.8, 0.4, 0.8, 0.8, 0.8, 0.8, 1.0, 1.0, 1.0, 0.6, 0.8, 0.8, 1.0, 0.8, 
            1.0, 0.8, 1.0, 0.6, 1.0, 0.2, 1.0, 1.0, 0.4],
            color='red',label = "5 Ghosts")
plt.scatter([126, 503, 95, 230, 407, 249, 236, 67, 129, 152, 129, 281, 671, 159, 231, 141, 92, 185, 145, 296, 524, 170, 440, 151, 183, 128, 111, 204, 216, 57, 165, 249, 254, 429, 230, 445, 243, 102, 386, 204, 114, 194, 169, 158, 235, 334, 134, 69, 436, 243, 123, 121, 459, 188, 126, 127, 147, 148, 153, 303, 269, 232, 142, 1379, 282, 399, 164, 165, 187,  101, 396, 170, 234, 208, 178, 133, 133, 197, 133, 136, 103, 659, 142, 224, 335, 195, 89, 215, 319, 156, 389, 560, 477, 64, 139, 562, 294, 134, 473, 180],
            [0.96, 0.56, 1.0, 0.92, 0.76, 0.84, 0.92, 0.6, 0.88, 0.72, 0.92, 0.96, 0.8, 0.96, 0.96, 1.0, 0.96, 0.96, 1.0, 0.8, 0.72, 1.0, 0.84, 0.6, 0.72, 0.8, 0.84, 0.56, 0.64, 0.88, 0.72, 0.96, 0.8, 0.72, 0.96, 0.8, 0.72, 0.88, 0.96, 0.88, 0.8, 0.96, 0.92, 0.88, 0.88, 0.84, 0.8, 0.72, 0.8, 0.8, 0.8, 0.88, 0.88, 0.84, 0.76, 0.76, 0.88, 0.96, 0.68, 1.0, 0.92, 0.92, 0.88, 0.76, 0.84, 1.0, 0.8, 0.72, 0.88, 0.92, 0.64, 0.92, 0.8, 0.88, 0.72, 0.8, 0.92, 0.96, 0.76, 0.96, 0.92, 0.72, 0.76, 0.72, 0.96, 0.8, 0.88, 1.0, 0.88, 0.72, 0.76, 0.72, 0.88, 0.72, 0.96, 0.76, 0.92, 0.96, 0.96, 0.96],
            color='blue',label = "25 Ghosts")
plt.scatter([339, 209, 257, 108, 199, 84, 172, 79, 477, 100, 355, 229, 183, 109, 94, 268, 238, 246, 85, 248, 255, 72, 159, 267, 92, 321, 201, 245, 117, 254, 190, 338, 140, 177, 521, 155, 121, 121, 127, 149, 229, 177, 193, 271, 164, 126, 148, 108, 148, 403, 295, 162, 203, 294, 224, 159, 173, 124, 209, 240, 215, 546, 116, 197, 139, 220, 1300, 222, 129, 83, 132, 90, 303, 153, 100, 537, 89, 340, 202, 174, 171, 160, 77, 172, 394, 90, 242, 109, 357, 170, 300, 102, 170, 90, 209, 143, 135, 85, 107, 251],
            [0.98, 1.0, 0.98, 0.68, 0.9, 0.96, 0.88, 0.96, 0.76, 0.76, 0.64, 0.92, 0.96, 0.8, 0.68, 0.68, 0.8, 0.76, 0.98, 0.84, 0.92, 1.0, 0.86, 0.74, 0.88, 0.72, 0.84, 0.6, 0.72, 0.52, 0.88, 0.9, 0.92, 0.84, 0.62, 0.64, 0.78, 0.78, 0.9, 0.72, 0.84, 0.94, 0.94, 0.84, 0.9, 0.82, 0.94, 0.84, 0.92, 0.86, 0.9, 0.9, 0.8, 0.92, 0.8, 0.74, 0.92, 0.7, 0.88, 0.74, 0.82, 0.86, 0.68, 0.62, 0.76, 0.86, 0.82, 0.68, 0.86, 0.86, 0.92, 0.92, 0.88, 0.88, 0.98, 0.92, 0.72, 0.86, 0.78, 0.88, 0.92, 0.88, 0.98, 0.98, 0.92, 0.88, 0.82, 0.92, 0.78, 0.94, 0.68, 0.9, 0.94, 0.94, 0.84, 0.82, 0.8, 0.76, 0.92, 0.92],
            color='purple', label='50 Gshosts')
plt.title('Accuracy vs Frames with different group sizes', fontsize='12')
plt.xlabel('Frames', fontsize='12')
plt.ylabel('Accuracy', fontsize='12')
plt.legend()
plt.show()

# ratio 0.7
aa=[0.96, 0.92, 1.0, 1.0, 0.92, 1.0, 0.84, 1.0, 0.92, 0.96]
at=[133, 132, 146, 110, 108, 80, 98, 111, 92, 155]
# ratio 0.6
ba = [0.96, 0.6, 0.76, 0.96, 0.96, 0.88, 0.88, 1.0, 0.96, 0.84]
bt = [264, 148, 200, 169, 320, 238, 158, 251, 324, 254]
# ratio 0.55
ca=[0.84, 0.92, 0.52, 0.76, 0.8, 0.92, 1.0, 0.84, 0.92, 0.76]
ct=[153, 245, 1025, 273, 283, 99, 166, 177, 154, 237]
# 0.52
da=[0.72, 0.48, 0.96, 0.64, 0.92, 0.44, 0.8, 0.64, 0.44, 0.56]
dt=[282, 317, 167, 263, 236, 402, 111, 197, 149, 388]

plt.scatter(at, aa,color='red',label = "0.7")
plt.scatter(bt, ba,color='blue',label = "0.6")
plt.scatter(ct, ca,color='green',label = "0.55")
plt.scatter(dt, da,color='purple',label = "0.52")

plt.title('', fontsize='12')
plt.xlabel('Frames', fontsize='12')
plt.ylabel('Accuracy', fontsize='12')
plt.legend()
plt.show()

# Feedback
plt.scatter([203, 239, 136, 267, 155, 713, 171, 72, 161, 429, 311, 173, 1340, 254, 175, 204, 863, 404, 163, 313, 342, 506, 171, 239, 112, 303, 245, 579, 779, 1383, 416, 113, 1268, 234, 99, 66, 207, 173, 268, 344, 525, 325, 345, 197, 220, 976, 264, 230, 175, 259, 187, 104, 554, 220, 241, 196, 158, 497, 193, 115, 121, 362, 345, 292, 347, 494, 146, 331, 1408, 129, 357, 256, 294, 388, 65, 159, 231, 773, 295, 148, 134, 454, 343, 201, 166, 661, 263, 164, 409, 919, 366, 140, 212, 461, 177, 366, 241, 2805, 526, 217],
[0.56, 0.6, 0.76, 0.68, 0.76, 0.76, 0.76, 0.88, 0.84, 0.64, 0.6, 0.36, 0.52, 0.64, 0.84, 0.76, 0.6, 0.64, 0.32, 0.4, 0.88, 0.68, 0.68, 0.72, 0.72, 0.48, 0.88, 0.64, 0.68, 0.36, 0.44, 0.64, 0.72, 0.92, 0.68, 0.6, 0.68, 0.6, 0.8, 0.72, 0.6, 0.76, 0.68, 0.4, 0.56, 0.64, 0.68, 0.88, 0.68, 0.56, 0.88, 0.72, 0.52, 0.92, 0.96, 0.72, 0.68, 0.76, 0.76, 0.84, 0.56, 0.52, 0.64, 0.8, 0.68, 0.92, 0.92, 0.64, 0.52, 0.76, 0.72, 0.36, 0.52, 0.56, 0.36, 0.76, 0.8, 0.52, 0.64, 0.6, 0.8, 0.84, 0.64, 0.76, 0.72, 0.48, 0.72, 0.84, 0.56, 0.64, 0.84, 0.16, 0.64, 0.4, 0.6, 0.52, 0.44, 0.76, 0.64, 0.64],
            color='red',label = "Positive feedback")
plt.scatter([411, 382, 127, 511, 445, 2082, 327, 1554, 224, 618, 549, 1524, 282, 809, 1420, 375, 1562, 530, 2152, 1159, 1093, 333, 685, 1244, 156, 945, 805, 592, 372, 844, 527, 439, 2222, 1054, 212, 1218, 203, 527, 535, 418, 653, 176, 497, 153, 855, 661, 537, 1245, 405, 182, 459, 375, 847, 1448, 95, 339, 285, 552, 327, 375, 1578, 1032, 126, 855, 258, 411, 1337, 445, 335, 818, 912, 158, 2005, 267, 764, 2199, 547, 459, 976, 1242, 774, 846, 1540, 1427, 2073, 331, 1384, 185, 485, 673, 318, 294, 1097, 171, 655, 910, 374, 1510, 912, 629],
            [0.68, 0.48, 0.72, 0.68, 0.76, 0.64, 0.72, 0.68, 0.76, 0.56, 0.88, 0.56, 0.76, 0.72, 0.56, 0.68, 0.64, 0.6, 0.6, 0.68, 0.76, 0.68, 0.56, 0.44, 0.68, 0.72, 0.6, 0.72, 0.64, 0.84, 0.68, 0.52, 0.68, 0.68, 0.84, 0.68, 0.48, 0.92, 0.72, 0.52, 0.52, 0.76, 0.52, 0.52, 0.36, 0.72, 0.76, 0.8, 0.8, 0.72, 0.52, 0.6, 0.52, 0.72, 0.72, 0.8, 0.68, 0.52, 0.68, 0.6, 0.72, 0.64, 0.68, 0.64, 0.76, 0.68, 0.72, 0.76, 0.84, 0.76, 0.48, 0.8, 0.8, 0.56, 0.76, 0.8, 0.52, 0.84, 0.76, 0.72, 0.84, 0.84, 0.72, 0.72, 0.76, 0.6, 0.8, 0.48, 0.56, 0.64, 0.52, 0.52, 0.6, 0.6, 0.88, 0.64, 0.68, 0.52, 0.52, 0.84],  
            color='green',label = "No feedback")

plt.title('Accuracy vs Frames With and Without Positive Feedback', fontsize='13')
plt.xlabel('Frames', fontsize='13')
plt.ylabel('Accuracy', fontsize='13')
plt.legend()
plt.show()

#Credible threshold
plt.scatter([23, 24, 37, 19, 87, 35, 12, 21, 19, 106, 29, 23, 20, 38, 101, 48, 10, 17, 24, 57, 21, 32, 21, 48, 42, 11, 21, 36, 36, 28, 23, 25, 18, 31, 21, 48, 21, 33, 45, 16, 24, 15, 90, 52, 57, 45, 19, 20, 48, 39, 18, 22, 18, 28, 26, 32, 43, 25, 30, 23, 63, 21, 31, 26, 13, 61, 22, 71, 67, 62, 24, 12, 11, 13, 16, 153, 47, 44, 17, 24, 18, 21, 24, 91, 33, 37, 26, 14, 13, 34, 40, 84, 39, 55, 58, 15, 30, 16, 84, 70],
            [0.64, 0.68, 0.72, 0.84, 0.64, 0.72, 0.76, 0.84, 0.52, 0.68, 0.6, 0.68, 0.8, 0.88, 0.48, 0.56, 0.84, 0.84, 0.6, 0.56, 0.72, 0.56, 0.48, 0.72, 0.6, 0.68, 0.6, 0.92, 0.84, 0.64, 0.88, 0.4, 0.64, 0.88, 0.68, 0.76, 0.84, 0.4, 0.68, 0.64, 0.8, 0.84, 0.48, 0.8, 0.68, 0.64, 0.48, 0.76, 0.56, 0.48, 0.76, 0.64, 0.68, 0.64, 0.8, 0.76, 0.8, 0.84, 0.6, 0.6, 0.48, 0.76, 0.6, 0.72, 0.88, 0.64, 0.84, 0.72, 0.72, 0.8, 0.6, 0.96, 0.76, 0.84, 0.68, 0.8, 0.6, 0.64, 0.76, 0.92, 0.8, 0.76, 0.68, 0.84, 0.56, 0.72, 0.8, 0.68, 0.68, 0.76, 0.68, 0.84, 0.76, 0.48, 0.8, 0.72, 1.0, 0.84, 0.72, 0.8],
            color='purple',label = "0.8")
plt.scatter([103, 125, 33, 44, 19, 49, 56, 75, 41, 43, 75, 44, 30, 42, 132, 54, 59, 58, 43, 79, 101, 50, 42, 111, 55, 180, 92, 35, 38, 90, 33, 131, 72, 94, 17, 56, 51, 58, 91, 63, 53, 84, 61, 85, 106, 55, 37, 108, 67, 103, 94, 53, 30, 36, 60, 33, 85, 29, 35, 52, 44, 125, 36, 101, 49, 195, 43, 49, 25, 75, 75, 97, 57, 109, 86, 58, 113, 63, 36, 61, 116, 60, 78, 46, 72, 56, 42, 44, 29, 70, 62, 55, 22, 72, 89, 84, 33, 63, 51, 35],
[0.52, 0.6, 0.6, 0.96, 0.68, 0.92, 0.72, 0.8, 0.76, 0.92, 0.88, 0.36, 0.72, 0.76, 1.0, 0.64, 0.84, 0.88, 0.68, 0.6, 0.72, 0.8, 0.88, 0.52, 0.6, 0.64, 0.64, 0.48, 0.6, 0.64, 0.68, 0.64, 0.8, 0.76, 0.64, 0.56, 0.48, 0.8, 0.44, 0.84, 0.88, 0.84, 0.68, 0.24, 0.76, 0.84, 0.88, 0.88, 0.64, 0.64, 0.64, 0.88, 0.76, 0.72, 0.64, 0.84, 0.72, 0.76, 0.84, 0.84, 0.76, 0.8, 0.96, 0.68, 0.96, 0.52, 0.72, 0.72, 0.88, 0.84, 0.56, 0.64, 0.72, 0.76, 0.64, 0.96, 0.8, 0.92, 0.84, 0.76, 0.8, 0.76, 0.92, 0.96, 0.68, 0.72, 0.8, 0.76, 0.68, 0.56, 0.76, 0.8, 0.8, 0.8, 0.88, 1.0, 0.84, 0.72, 0.52, 1.0],
            color='red',label = "0.9")
plt.scatter([116, 58, 151, 179, 245, 107, 98, 128, 56, 109, 58, 659, 51, 147, 109, 453, 170, 151, 72, 212, 61, 83, 112, 88, 82, 38, 57, 26, 127, 81, 170, 167, 76, 65, 83, 72, 115, 95, 79, 175, 61, 72, 77, 47, 184, 58, 45, 122, 172, 157, 64, 99, 118, 127, 126, 99, 178, 123, 239, 218, 83, 104, 79, 101, 49, 118, 138, 57, 154, 211, 134, 52, 70, 131, 106, 86, 165, 108, 44, 131, 266, 100, 140, 31, 149, 193, 46, 105, 101, 38, 90, 74, 164, 349, 110, 167, 173, 61, 117, 123],
            [0.76, 0.88, 0.92, 0.76, 0.56, 0.84, 0.92, 0.84, 0.92, 0.76, 0.76, 0.84, 0.64, 0.68, 0.8, 0.56, 0.96, 0.44, 0.92,  0.76, 0.56, 0.76, 0.6, 0.8, 0.84, 0.84, 0.96, 0.76, 1.0, 0.68, 0.72, 0.6, 0.76, 0.96, 0.84, 0.72, 0.76, 0.64, 0.88, 0.6, 0.88, 0.68, 0.84, 0.72, 0.84, 0.96, 0.68, 0.96, 0.84, 0.68, 0.72, 0.64, 0.96, 0.76, 0.88, 0.64, 0.84, 0.76, 0.88, 0.72, 0.76, 0.84, 0.76, 0.52, 0.76, 0.68, 0.8, 0.64, 0.96, 0.72, 0.44, 0.68, 0.76, 0.8, 0.88, 0.96, 0.84, 0.76, 0.68, 0.76, 0.68, 0.88, 0.52, 0.72, 0.92, 0.92, 0.92, 0.8, 0.84, 1.0, 0.68, 0.72, 0.64, 0.72, 0.8, 0.72, 0.4, 0.8, 0.96, 0.84],
            color='green',label = "0.95")
plt.scatter([126, 503, 95, 230, 407, 249, 236, 67, 129, 152, 129, 281, 671, 159, 231, 141, 92, 185, 145, 296, 524, 170, 440, 151, 183, 128, 111, 204, 216, 57, 165, 249, 254, 429, 230, 445, 243, 102, 386, 204, 114, 194, 169, 158, 235, 334, 134, 69, 436, 243, 123, 121, 459, 188, 126, 127, 147, 148, 153, 303, 269, 232, 142, 1379, 282, 399, 164, 165, 187, 
101, 396, 170, 234, 208, 178, 133, 133, 197, 133, 136, 103, 659, 142, 224, 335, 195, 89, 215, 319, 156, 389, 560, 
477, 64, 139, 562, 294, 134, 473, 180],
[0.96, 0.56, 1.0, 0.92, 0.76, 0.84, 0.92, 0.6, 0.88, 0.72, 0.92, 0.96, 0.8, 0.96, 0.96, 1.0, 0.96, 0.96, 1.0, 0.8, 0.72, 1.0, 0.84, 0.6, 0.72, 0.8, 0.84, 0.56, 0.64, 0.88, 0.72, 0.96, 0.8, 0.72, 0.96, 0.8, 0.72, 0.88, 0.96, 0.88, 0.8, 0.96, 0.92, 0.88, 0.88, 0.84, 0.8, 0.72, 0.8, 0.8, 0.8, 0.88, 0.88, 0.84, 0.76, 0.76, 0.88, 0.96, 0.68, 1.0, 0.92, 0.92, 0.88, 0.76, 0.84, 1.0, 0.8, 0.72, 0.88, 0.92, 0.64, 0.92, 0.8, 0.88, 0.72, 0.8, 0.92, 0.96, 0.76, 0.96, 0.92, 0.72, 0.76, 0.72, 0.96, 0.8, 0.88, 1.0, 0.88, 0.72, 0.76, 0.72, 0.88, 0.72, 0.96, 0.76, 0.92, 0.96, 0.96, 0.96],
            color='blue',label = "0.99")

plt.title('Accuracy vs Frames with Different Credible Thresholds', fontsize='12')
plt.xlabel('Frames', fontsize='12')
plt.ylabel('Accuracy', fontsize='12')
plt.legend()
plt.show()
# Prior
plt.scatter([203, 239, 136, 267, 155, 713, 171, 72, 161, 429, 311, 173, 1340, 254, 175, 204, 863, 404, 163, 313, 342, 506, 171, 239, 112, 303, 245, 579, 779, 1383, 416, 113, 1268, 234, 99, 66, 207, 173, 268, 344, 525, 325, 345, 197, 220, 976, 264, 230, 175, 259, 187, 104, 554, 220, 241, 196, 158, 497, 193, 115, 121, 362, 345, 292, 347, 494, 146, 331, 1408, 129, 357, 256, 294, 388, 65, 159, 231, 773, 295, 148, 134, 454, 343, 201, 166, 661, 263, 164, 409, 919, 366, 140, 212, 461, 177, 366, 241, 2805, 526, 217],
            [0.56, 0.6, 0.76, 0.68, 0.76, 0.76, 0.76, 0.88, 0.84, 0.64, 0.6, 0.36, 0.52, 0.64, 0.84, 0.76, 0.6, 0.64, 0.32, 0.4, 0.88, 0.68, 0.68, 0.72, 0.72, 0.48, 0.88, 0.64, 0.68, 0.36, 0.44, 0.64, 0.72, 0.92, 0.68, 0.6, 0.68, 0.6, 0.8, 0.72, 0.6, 0.76, 0.68, 0.4, 0.56, 0.64, 0.68, 0.88, 0.68, 0.56, 0.88, 0.72, 0.52, 0.92, 0.96, 0.72, 0.68, 0.76, 0.76, 0.84, 0.56, 0.52, 0.64, 0.8, 0.68, 0.92, 0.92, 0.64, 0.52, 0.76, 0.72, 0.36, 0.52, 0.56, 0.36, 0.76, 0.8, 0.52, 0.64, 0.6, 0.8, 0.84, 0.64, 0.76, 0.72, 0.48, 0.72, 0.84, 0.56, 0.64, 0.84, 0.16, 0.64, 0.4, 0.6, 0.52, 0.44, 0.76, 0.64, 0.64],
            color='red',label = "1")
plt.scatter([281, 885, 594, 194, 579, 178, 242, 229, 310, 259, 273, 161, 299, 733, 121, 264, 1333, 186, 798, 157, 112, 285, 287, 1398, 544, 409, 380, 483, 165, 383, 213, 449, 424, 162, 379, 213, 181, 317, 394, 181, 227, 441, 699, 388, 262, 476, 297, 477, 253, 313, 156, 219, 1114, 473, 256, 85, 218, 373, 437, 358, 291, 174, 334, 317, 114, 114, 103, 278, 342, 390, 542, 305, 114, 267, 294, 144, 318, 210, 200, 147, 154, 187, 358, 715, 625, 200, 191, 382, 475, 990, 127, 82, 151, 436, 129, 338, 485, 307, 349, 189],
            [0.6, 0.8, 0.56, 0.88, 0.76, 0.88, 0.72, 0.92, 0.72, 0.76, 0.84, 0.92, 0.76, 0.72, 0.96, 0.8, 0.96, 1.0, 0.76, 0.8, 0.84, 0.8, 0.92, 0.68, 0.72, 0.12, 1.0, 0.8, 0.52, 0.64, 0.72, 0.64, 0.36, 0.64, 0.76, 0.92, 0.84, 0.84, 0.52, 0.64, 0.84, 0.6, 0.48, 0.84, 0.84, 0.8, 0.88, 0.6, 0.76, 0.76, 0.76, 0.92, 0.56, 0.4, 0.36, 0.52, 0.44, 0.72, 0.64, 0.88, 0.28, 0.8, 0.68, 0.76, 0.8, 0.68, 0.96, 0.88, 0.92, 0.72, 0.84, 0.84, 0.56, 0.72, 0.72, 0.56, 0.8, 0.88, 0.72, 0.76, 0.8, 0.28, 0.64, 0.8, 0.8, 0.76, 0.6, 0.84, 0.56, 0.84, 0.68, 0.72, 0.64, 0.6, 0.84, 0.6, 0.32, 0.68, 0.52, 0.72],
            color='blue',label = "2")
plt.scatter([430, 291, 796, 93, 583, 224, 114, 153, 665, 119, 712, 291, 304, 277, 202, 350, 84, 475, 155, 179, 400, 152, 148, 274, 275, 352, 223, 320, 268, 503, 418, 308, 385, 288, 1240, 222, 423, 366, 158, 151, 314, 324, 812, 220, 283, 147, 620, 127, 527, 263, 126, 233, 169, 962, 1078, 854, 854, 340, 183, 520, 690, 462, 407, 693, 165, 473, 169, 349, 199, 444, 327, 408, 374, 399, 113, 149, 327, 252, 252, 288, 500, 170, 281, 289, 169, 2034, 269, 389, 408, 302, 247, 493, 189, 273, 353, 221, 140, 741, 219, 237],
            [0.6, 0.52, 0.84, 0.72, 0.72, 0.88, 0.72, 0.96, 0.64, 0.6, 0.6, 0.64, 0.8, 0.96, 0.68, 0.96, 0.52, 0.76, 0.64, 0.84, 0.68, 0.76, 0.84, 0.64, 0.76, 0.8, 0.68, 0.6, 0.72, 0.72, 0.88, 0.72, 0.72, 0.88, 0.76, 0.76, 0.88, 0.6, 0.6, 0.92, 0.8, 0.64, 0.36, 0.48, 0.6, 0.8, 0.8, 0.88, 0.84, 0.72, 0.84, 0.6, 0.76, 0.68, 0.72, 0.48, 0.84, 0.56, 0.88, 0.88, 0.76, 0.8, 0.68, 0.4, 0.68, 0.76, 0.84, 0.72, 0.56, 0.36, 0.56, 0.68, 0.76, 0.6, 0.92, 0.6, 0.56, 0.72, 0.92, 0.32, 0.56, 0.68, 0.56, 1.0, 0.88, 0.68, 0.44, 0.16, 0.2, 0.36, 0.84, 0.8, 0.6, 0.6, 0.72, 0.88, 0.52, 0.8, 0.44, 0.6],
            color='green', label = "5")
plt.scatter([357, 273, 271, 227, 236, 338, 618, 661, 152, 386, 963, 158, 198, 465, 181, 352, 409, 384, 463, 264, 542, 174, 783, 202, 332, 375, 133, 420, 206, 389, 219, 1259, 186, 339, 136, 71, 339, 280, 176, 251, 235, 1061, 201, 187, 135, 394, 593, 544, 201, 1002, 302, 226, 273, 286, 1258, 225, 611, 142, 176, 248, 690, 692, 357, 1152, 378, 1258, 151, 223, 996, 314, 390, 305, 574, 436, 647, 401, 92, 186, 508, 629, 456, 1031, 282, 347, 132, 869, 570, 158, 292, 278, 287, 464, 1090, 492, 242, 229, 218, 352, 273, 443],
            [0.4, 0.92, 0.6, 1.0, 0.88, 0.6, 0.64, 0.76, 0.96, 1.0, 0.52, 0.6, 0.8, 1.0, 0.56, 0.84, 0.84, 0.48, 0.4, 0.96, 0.76, 0.84, 0.32, 0.6, 0.64, 0.76, 0.96, 0.84, 0.8, 0.92, 0.64, 0.6, 0.6, 0.72, 0.36, 0.84, 0.76, 0.44, 0.92, 0.8, 1.0, 0.6, 0.76, 0.88, 0.96, 0.68, 0.92, 0.64, 0.72, 0.8, 0.64, 0.96, 0.76, 0.68, 0.6, 0.68, 0.72, 0.84, 0.8, 0.8, 0.8, 0.8, 0.68, 0.52, 0.64, 0.64, 0.84, 0.88, 0.64, 0.88, 0.76, 0.52, 0.92, 0.8, 0.72, 0.52, 0.72, 0.8, 0.72, 0.88, 0.64, 0.6, 0.64, 0.52, 0.68, 0.8, 0.96, 0.88, 0.84, 0.32, 0.64, 0.72, 0.24, 0.76, 0.92, 0.8, 0.88, 0.6, 0.72, 0.92],
            color='orange', label = "10")
plt.scatter([311, 405, 314, 327, 427, 284, 353, 227, 550, 1463, 471, 587, 216, 516, 143, 122, 660, 341, 388, 411, 625, 412, 164, 282, 1193, 339, 399, 574, 317, 492, 403, 609, 420, 852, 375, 450, 669, 237, 315, 502, 614, 570, 506, 528, 267, 443, 458, 735, 262, 113, 581, 537, 326, 365, 178, 492, 354, 1074, 191, 191, 535, 412, 312, 1622, 337, 394, 230, 533, 193, 732, 624, 347, 256, 293, 395, 343, 269, 372, 222, 843, 181, 710, 439, 1223, 321, 325, 140, 580, 700, 377, 1206, 884, 369, 370, 322, 483, 345, 723, 244, 997],
            [0.76, 0.8, 0.52, 0.68, 0.88, 0.68, 0.88, 0.76, 0.72, 0.72, 0.64, 0.84, 0.96, 0.76, 0.56, 0.68, 0.6, 0.6, 0.6, 0.88, 0.6, 0.96, 0.92, 0.72, 0.64, 0.76, 0.88, 0.72, 0.8, 0.76, 0.72, 0.76, 0.48, 0.2, 0.88, 0.72, 0.44, 0.52, 0.6, 0.6, 0.64, 0.92, 0.68, 0.92, 0.68, 1.0, 0.8, 0.88, 0.88, 0.96, 0.48, 0.72, 0.52, 0.56, 0.88, 0.72, 0.8, 0.56, 0.96, 0.6, 0.36, 0.8, 0.8, 0.76, 0.64, 0.64, 1.0, 0.8, 0.68, 0.64, 0.72, 1.0, 0.92, 0.96, 0.68, 0.76, 0.88, 0.88, 0.8, 0.64, 0.68, 0.8, 0.44, 0.64, 0.6, 1.0, 0.84, 0.44, 0.88, 1.0, 0.56, 0.52, 0.72, 0.8, 0.76, 0.84, 0.92, 0.8, 1.0, 0.64],
            color='purple', label = "20")
plt.title('Accuracy vs Frames with Different Prior Values', fontsize='13')
plt.xlabel('Frames', fontsize='13')
plt.ylabel('Accuracy', fontsize='13')
plt.legend()
plt.show()
"""
x =[1.0, 0.75, 1.0, 0.0, 0.25, 1.0, 1.0, 1.0, 0.5, 0.75, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.5, 1.0, 0.5, 1.0, 0.5, 0.25, 1.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.0, 1.0, 0.25, 0.0, 0.75, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.75, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.5, 0.0, 0.75, 0.25, 1.0, 0.5, 1.0, 0.75, 0.0, 0.0, 0.25, 1.0, 0.75, 0.25, 1.0, 1.0, 0.75, 0.25, 1.0, 0.75, 1.0, 0.75, 0.75, 0.5, 1.0, 0.25, 1.0, 1.0, 0.25, 0.5, 0.75, 0.0, 1.0, 0.75, 0.25, 1.0, 0.5, 1.0, 0.5, 1.0, 0.5, 0.75, 1.0, 0.0, 1.0, 0.5, 1.0, 0.0]
print(sum(x)/len(x))
y = [1.0, 0.75, 0.25, 0.25, 0.0, 0.5, 0.25, 0.75, 1.0, 0.5, 0.5, 0.0, 1.0, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5, 0.75, 0.5, 0.25, 0.5, 0.75, 0.5, 0.25, 1.0, 0.5, 0.25, 0.75, 0.5, 0.5, 1.0, 0.25, 0.5, 0.75, 0.25, 1.0, 1.0, 0.25, 0.5, 0.75, 0.5, 1.0, 0.5, 0.25, 1.0, 0.5, 0.25, 0.25, 1.0, 1.0, 0.75, 0.5, 0.75, 0.25, 0.75, 0.75, 
0.5, 1.0, 0.25, 0.75, 1.0, 0.5, 0.75, 0.75, 0.0, 0.5, 0.5, 0.75, 1.0, 0.75, 0.75, 1.0, 0.75, 1.0, 0.5, 0.5, 0.75, 
0.5, 0.75, 0.5, 0.0, 1.0, 0.25, 0.75, 0.25, 1.0, 0.75, 1.0, 1.0, 0.75, 0.75, 0.5, 0.75, 0.75]
print(sum(y)/len(y))
plt.scatter([112, 251, 33, 83, 311, 306, 200, 96, 64, 96, 205, 61, 47, 76, 42, 15, 51, 33, 103, 37, 1915, 37, 64, 66, 30, 337, 4, 94, 38, 241, 95, 245, 62, 9, 42, 18, 18, 458, 100, 137, 27, 130, 160, 23, 32, 11, 32, 42, 80, 45, 9, 67, 14, 44, 112, 258, 87, 9, 124, 107, 111, 161, 465, 51, 321, 26, 10, 231, 62, 32, 161, 22, 253, 21, 495, 77, 104, 841, 105, 142, 84, 81, 41, 298, 95, 17, 80, 183, 98, 116, 37, 22, 17, 50, 64, 138, 475, 25, 15, 76],
            [1.0, 0.75, 1.0, 0.0, 0.25, 1.0, 1.0, 1.0, 0.5, 0.75, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.5, 1.0, 0.5, 1.0, 0.5, 0.25, 1.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.0, 1.0, 0.25, 0.0, 0.75, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.75, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.5, 0.0, 0.75, 0.25, 1.0, 0.5, 1.0, 0.75, 0.0, 0.0, 0.25, 1.0, 0.75, 0.25, 1.0, 1.0, 0.75, 0.25, 1.0, 0.75, 1.0, 0.75, 0.75, 0.5, 1.0, 0.25, 1.0, 1.0, 0.25, 0.5, 0.75, 0.0, 1.0, 0.75, 0.25, 1.0, 0.5, 1.0, 0.5, 1.0, 0.5, 0.75, 1.0, 0.0, 1.0, 0.5, 1.0, 0.0],
            color="pink", label="Line Map")
plt.scatter([114, 680, 257, 314, 23, 123, 17, 425, 245, 143, 378, 186, 372, 275, 154, 64, 106, 103, 338, 190, 1264, 52, 1211,  156, 117, 242, 330, 30, 272, 107, 103, 179, 3164, 27, 112, 98, 80, 270, 105, 296, 315, 197, 368, 21, 55, 120, 123, 2662, 347, 330, 644, 112, 33, 238, 76, 706, 496, 87, 1460, 92, 246, 673, 416, 904, 80, 209, 52, 129, 116, 856, 79, 518, 215, 146, 817, 73, 272, 154, 116, 710, 42, 67, 602, 929, 630, 442, 335, 222, 54, 495, 14, 2147, 225, 552, 824, 193, 82, 155, 116, 382],
            [1.0, 0.75, 0.25, 0.25, 0.0, 0.5, 0.25, 0.75, 1.0, 0.5, 0.5, 0.0, 1.0, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5, 0.75, 0.5, 0.25, 0.5, 0.75, 0.5, 0.25, 1.0, 0.5, 0.25, 0.75, 0.5, 0.5, 1.0, 0.25, 0.5, 0.75, 0.25, 1.0, 1.0, 0.25, 0.5, 0.75, 0.5, 1.0, 0.5, 0.25, 1.0, 0.5, 0.25, 0.25, 1.0, 1.0, 0.75, 0.5, 0.75, 0.25, 0.75, 0.75, 0.5, 1.0, 0.25, 0.75, 1.0, 0.5, 0.75, 0.75, 0.0, 0.5, 0.5, 0.75, 1.0, 0.75, 0.75, 1.0, 0.75, 1.0, 0.5, 0.5, 0.75, 0.5, 0.75, 0.5, 0.0, 1.0, 0.25, 0.75, 0.25, 1.0, 0.75, 1.0, 1.0, 0.75, 0.75, 0.5, 0.75, 0.75],
            color="navy", label="Pac-Man map")
plt.title('', fontsize='13')
plt.xlabel('Frames', fontsize='13')
plt.ylabel('Accuracy', fontsize='13')
plt.legend()
plt.show()
plt.title('Accuracy vs Frames with Different Prior Values', fontsize='13')
plt.xlabel('Frames', fontsize='13')
plt.ylabel('Accuracy', fontsize='13')
plt.legend()
plt.show()