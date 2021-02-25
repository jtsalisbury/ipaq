
import synthetic_detection

fake = synthetic_detection.Synthetic_Detector()
fake2 = synthetic_detection.Synthetic_Detector()

image = []
image.append(fake.get_object_at_ang(-4))
image.append(fake2.get_object_at_ang(4))


lidar = [
        {
            "distance": 0.00000,
            "theta": 0.00000
        },
        {
            "distance": 0.0000,
            "theta": 2.0000
        },
        {
            "distance": 5.00000,
            "theta": 4.00000
        },
        {
            "distance": 5.00000,
            "theta": 6.00000
        },
        {
            "distance": 5.0000,
            "theta": 8.0000
        },
        {
            "distance": 0.00000,
            "theta": 10.00000
        },
        {
            "distance": 0.00000,
            "theta": 12.00000
        },
        {
            "distance": 0.0000,
            "theta": 14.0000
        },
        {
            "distance": 0.00000,
            "theta": 16.00000
        },
        {
            "distance": 0.00000,
            "theta": 18.00000
        },
        {
            "distance": 0.00000,
            "theta": 20.00000
        },
        {
            "distance": 0.0000,
            "theta": 22.0000
        },
        {
            "distance": 0.00000,
            "theta": 24.00000
        },
        {
            "distance": 0.00000,
            "theta": 26.00000
        },
        {
            "distance": 0.0000,
            "theta": 28.0000
        },
        {
            "distance": 0.00000,
            "theta": 30.00000
        },
        {
            "distance": 0.00000,
            "theta": 32.00000
        },
        {
            "distance": 0.0000,
            "theta": 34.0000
        },
        {
            "distance": 0.00000,
            "theta": 36.00000
        },
        {
            "distance": 0.00000,
            "theta": 38.00000
        },
        {
            "distance": 0.00000,
            "theta": 40.00000
        },
        {
            "distance": 0.0000,
            "theta": 42.0000
        },
        {
            "distance": 0.00000,
            "theta": 44.00000
        },
        {
            "distance": 0.00000,
            "theta": 46.00000
        },
        {
            "distance": 0.0000,
            "theta": 48.0000
        },
        {
            "distance": 0.00000,
            "theta": 50.00000
        },
        {
            "distance": 0.00000,
            "theta": 52.00000
        },
        {
            "distance": 0.0000,
            "theta": 54.0000
        },
        {
            "distance": 0.00000,
            "theta": 56.00000
        },
        {
            "distance": 0.00000,
            "theta": 58.00000
        },
        {
            "distance": 0.00000,
            "theta": 60.00000
        },
        {
            "distance": 0.0000,
            "theta": 62.0000
        },
        {
            "distance": 0.00000,
            "theta": 64.00000
        },
        {
            "distance": 0.00000,
            "theta": 66.00000
        },
        {
            "distance": 0.0000,
            "theta": 68.0000
        },
        {
            "distance": 0.00000,
            "theta": 70.00000
        },
        {
            "distance": 0.00000,
            "theta": 72.00000
        },
        {
            "distance": 0.0000,
            "theta": 74.0000
        },
        {
            "distance": 0.00000,
            "theta": 76.00000
        },
        {
            "distance": 0.00000,
            "theta": 78.00000
        },
        {
            "distance": 0.00000,
            "theta": 0.00000
        },
        {
            "distance": 0.0000,
            "theta": 80.0000
        },
        {
            "distance": 0.00000,
            "theta": 82.00000
        },
        {
            "distance": 0.00000,
            "theta": 84.00000
        },
        {
            "distance": 0.0000,
            "theta": 86.0000
        },
        {
            "distance": 0.00000,
            "theta": 88.00000
        },
        {
            "distance": 0.00000,
            "theta": 90.00000
        },
        {
            "distance": 0.0000,
            "theta": 92.0000
        },
        {
            "distance": 0.00000,
            "theta": 94.00000
        },
        {
            "distance": 0.00000,
            "theta": 96.00000
        },
        {
            "distance": 0.00000,
            "theta": 98.00000
        },
        {
            "distance": 0.0000,
            "theta": 100.0000
        },
        {
            "distance": 0.00000,
            "theta": 102.00000
        },
        {
            "distance": 0.00000,
            "theta": 104.00000
        },
        {
            "distance": 0.0000,
            "theta": 106.0000
        },
        {
            "distance": 0.00000,
            "theta": 108.00000
        },
        {
            "distance": 0.00000,
            "theta": 110.00000
        },
        {
            "distance": 0.0000,
            "theta": 112.0000
        },
        {
            "distance": 0.00000,
            "theta": 114.00000
        },
        {
            "distance": 0.00000,
            "theta": 116.00000
        },
        {
            "distance": 0.00000,
            "theta": 118.00000
        },
        {
            "distance": 0.0000,
            "theta": 120.0000
        },
        {
            "distance": 0.00000,
            "theta": 122.00000
        },
        {
            "distance": 0.00000,
            "theta": 124.00000
        },
        {
            "distance": 0.0000,
            "theta": 126.0000
        },
        {
            "distance": 0.00000,
            "theta": 128.00000
        },
        {
            "distance": 0.00000,
            "theta": 130.00000
        },
        {
            "distance": 0.0000,
            "theta": 132.0000
        },
        {
            "distance": 0.00000,
            "theta": 134.00000
        },
        {
            "distance": 0.00000,
            "theta": 136.00000
        },
        {
            "distance": 0.00000,
            "theta": 138.00000
        },
        {
            "distance": 0.0000,
            "theta": 140.0000
        },
        {
            "distance": 0.00000,
            "theta": 142.00000
        },
        {
            "distance": 0.00000,
            "theta": 144.00000
        },
        {
            "distance": 0.0000,
            "theta": 146.0000
        },
        {
            "distance": 0.00000,
            "theta": 148.00000
        },
        {
            "distance": 0.00000,
            "theta": 150.00000
        },
        {
            "distance": 0.0000,
            "theta": 152.0000
        },
        {
            "distance": 0.00000,
            "theta": 154.00000
        },
        {
            "distance": 0.00000,
            "theta": 156.00000
        },
        {
            "distance": 0.00000,
            "theta": 158.00000
        },
        {
            "distance": 0.0000,
            "theta": 160.0000
        },
        {
            "distance": 0.00000,
            "theta": 162.00000
        },
        {
            "distance": 0.00000,
            "theta": 164.00000
        },
        {
            "distance": 0.0000,
            "theta": 166.0000
        },
        {
            "distance": 0.00000,
            "theta": 168.00000
        },
        {
            "distance": 0.00000,
            "theta": 170.00000
        },
        {
            "distance": 0.0000,
            "theta": 172.0000
        },
        {
            "distance": 0.00000,
            "theta": 174.00000
        },
        {
            "distance": 0.00000,
            "theta": 176.00000
        },
        {
            "distance": 0.00000,
            "theta": 178.00000
        },
        {
            "distance": 0.0000,
            "theta": 180.0000
        },
        {
            "distance": 0.00000,
            "theta": 182.00000
        },
        {
            "distance": 0.00000,
            "theta": 184.00000
        },
        {
            "distance": 0.0000,
            "theta": 186.0000
        },
        {
            "distance": 0.00000,
            "theta": 188.00000
        },
        {
            "distance": 0.00000,
            "theta": 190.00000
        },
        {
            "distance": 0.0000,
            "theta": 192.0000
        },
        {
            "distance": 0.00000,
            "theta": 194.00000
        },
        {
            "distance": 0.00000,
            "theta": 196.00000
        },
        {
            "distance": 0.00000,
            "theta": 198.00000
        },
        {
            "distance": 0.0000,
            "theta": 200.0000
        },
        {
            "distance": 0.00000,
            "theta": 202.00000
        },
        {
            "distance": 0.00000,
            "theta": 204.00000
        },
        {
            "distance": 0.0000,
            "theta": 206.0000
        },
        {
            "distance": 0.00000,
            "theta": 208.00000
        },
        {
            "distance": 0.00000,
            "theta": 210.00000
        },
        {
            "distance": 0.0000,
            "theta": 212.0000
        },
        {
            "distance": 0.00000,
            "theta": 214.00000
        },
        {
            "distance": 0.00000,
            "theta": 216.00000
        },
        {
            "distance": 0.00000,
            "theta": 218.00000
        },
        {
            "distance": 0.0000,
            "theta": 220.0000
        },
        {
            "distance": 0.00000,
            "theta": 222.00000
        },
        {
            "distance": 0.00000,
            "theta": 224.00000
        },
        {
            "distance": 0.0000,
            "theta": 226.0000
        },
        {
            "distance": 0.00000,
            "theta": 228.00000
        },
        {
            "distance": 0.00000,
            "theta": 230.00000
        },
        {
            "distance": 0.0000,
            "theta": 232.0000
        },
        {
            "distance": 0.00000,
            "theta": 234.00000
        },
        {
            "distance": 0.00000,
            "theta": 0.00000
        },
        {
            "distance": 0.00000,
            "theta": 236.00000
        },
        {
            "distance": 0.0000,
            "theta": 238.0000
        },
        {
            "distance": 0.00000,
            "theta": 240.00000
        },
        {
            "distance": 0.00000,
            "theta": 242.00000
        },
        {
            "distance": 0.0000,
            "theta": 244.0000
        },
        {
            "distance": 0.00000,
            "theta": 246.00000
        },
        {
            "distance": 0.00000,
            "theta": 248.00000
        },
        {
            "distance": 0.0000,
            "theta": 250.0000
        },
        {
            "distance": 0.00000,
            "theta": 252.00000
        },
        {
            "distance": 0.00000,
            "theta": 254.00000
        },
        {
            "distance": 0.00000,
            "theta": 256.00000
        },
        {
            "distance": 0.0000,
            "theta": 258.0000
        },
        {
            "distance": 0.00000,
            "theta": 260.00000
        },
        {
            "distance": 0.00000,
            "theta": 262.00000
        },
        {
            "distance": 0.0000,
            "theta": 264.0000
        },
        {
            "distance": 0.00000,
            "theta": 266.00000
        },
        {
            "distance": 0.00000,
            "theta": 268.00000
        },
        {
            "distance": 0.0000,
            "theta": 270.0000
        },
        {
            "distance": 0.00000,
            "theta": 272.00000
        },
        {
            "distance": 0.00000,
            "theta": 274.00000
        },
        {
            "distance": 0.00000,
            "theta": 276.00000
        },
        {
            "distance": 0.0000,
            "theta": 278.0000
        },
        {
            "distance": 0.00000,
            "theta": 280.00000
        },
        {
            "distance": 0.00000,
            "theta": 282.00000
        },
        {
            "distance": 0.0000,
            "theta": 284.0000
        },
        {
            "distance": 0.00000,
            "theta": 286.00000
        },
        {
            "distance": 0.00000,
            "theta": 288.00000
        },
        {
            "distance": 0.0000,
            "theta": 290.0000
        },
        {
            "distance": 0.00000,
            "theta": 292.00000
        },
        {
            "distance": 0.00000,
            "theta": 294.00000
        },
        {
            "distance": 0.00000,
            "theta": 296.00000
        },
        {
            "distance": 0.0000,
            "theta": 298.0000
        },
        {
            "distance": 0.00000,
            "theta": 300.00000
        },
        {
            "distance": 0.00000,
            "theta": 302.00000
        },
        {
            "distance": 0.0000,
            "theta": 304.0000
        },
        {
            "distance": 0.00000,
            "theta": 306.00000
        },
        {
            "distance": 0.00000,
            "theta": 308.00000
        },
        {
            "distance": 0.0000,
            "theta": 310.0000
        },
        {
            "distance": 0.00000,
            "theta": 312.00000
        },
        {
            "distance": 0.00000,
            "theta": 314.00000
        },
        {
            "distance": 0.00000,
            "theta": 316.00000
        },
        {
            "distance": 0.0000,
            "theta": 318.0000
        },
        {
            "distance": 0.00000,
            "theta": 320.00000
        },
        {
            "distance": 0.00000,
            "theta": 322.00000
        },
        {
            "distance": 0.0000,
            "theta": 324.0000
        },
        {
            "distance": 0.00000,
            "theta": 326.00000
        },
        {
            "distance": 0.00000,
            "theta": 328.00000
        },
        {
            "distance": 0.0000,
            "theta": 330.0000
        },
        {
            "distance": 0.00000,
            "theta": 332.00000
        },
        {
            "distance": 0.00000,
            "theta": 334.00000
        },
        {
            "distance": 0.00000,
            "theta": 336.00000
        },
        {
            "distance": 0.0000,
            "theta": 338.0000
        },
        {
            "distance": 0.00000,
            "theta": 340.00000
        },
        {
            "distance": 0.00000,
            "theta": 342.00000
        },
        {
            "distance": 0.0000,
            "theta": 344.0000
        },
        {
            "distance": 0.00000,
            "theta": 346.00000
        },
        {
            "distance": 0.00000,
            "theta": 348.00000
        },
        {
            "distance": 0.0000,
            "theta": 350.0000
        },
        {
            "distance": 0.00000,
            "theta": 352.00000
        },
        {
            "distance": 0.00000,
            "theta": 354.00000
        },
        {
            "distance": 5.00000,
            "theta": 356.00000
        },
        {
            "distance": 0.00000,
            "theta": 358.00000
        }
    ]